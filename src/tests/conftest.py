import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from src.common.config import Config
from src.common.logger import logger
from src.common.utils import take_screenshot

# 配置文件实例
config = Config()

@pytest.fixture(scope="session")
def browser_type():
    """返回浏览器类型"""
    return config.get_browser_type()

@pytest.fixture(scope="function")
def driver(browser_type):
    """创建浏览器驱动，每个测试函数执行前创建，执行后关闭"""
    logger.info(f"开始初始化 {browser_type} 浏览器驱动")
    
    # 根据配置创建相应的浏览器驱动
    if browser_type == 'chrome':
        options = ChromeOptions()
        if config.is_headless():
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
        # 添加其他常用配置
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
    elif browser_type == 'firefox':
        options = FirefoxOptions()
        if config.is_headless():
            options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"不支持的浏览器类型: {browser_type}")
    
    # 设置窗口大小
    window_size = config.get_window_size()
    width, height = map(int, window_size.split(','))
    driver.set_window_size(width, height)
    
    logger.info(f"{browser_type} 浏览器驱动初始化完成")
    yield driver
    
    # 测试结束后关闭浏览器
    logger.info(f"关闭 {browser_type} 浏览器驱动")
    driver.quit()

@pytest.fixture(scope="function")
def base_url():
    """返回基础URL"""
    return config.get_base_url()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    钩子函数：测试失败时自动截图并添加到allure报告
    """
    outcome = yield
    rep = outcome.get_result()
    
    # 只有当测试失败且有driver fixture时才截图
    if rep.when == "call" and rep.failed:
        for fixture_name in item.fixturenames:
            if fixture_name == "driver":
                driver = item.funcargs[fixture_name]
                screenshot_path = take_screenshot(driver, "test_failure")
                if screenshot_path:
                    # 添加截图到allure报告
                    with allure.step("测试失败截图"):
                        allure.attach.file(
                            screenshot_path,
                            name="失败截图",
                            attachment_type=allure.attachment_type.PNG
                        )
                break

def pytest_collection_modifyitems(items):
    """
    钩子函数：修改测试用例集合
    可以在这里实现用例排序、筛选等功能
    """
    logger.info(f"共收集到 {len(items)} 个测试用例")
    # 示例：按用例名称排序
    items.sort(key=lambda x: x.name)
    