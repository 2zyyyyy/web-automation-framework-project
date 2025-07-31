from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from src.common.logger import logger
from src.common.config import Config
from src.common.utils import take_screenshot
from src.common.exceptions import ElementNotFoundException, TimeoutException

class BasePage:
    """基础页面类，封装Selenium常用操作，作为所有页面对象的基类"""
    
    def __init__(self, driver):
        self.driver = driver
        self.config = Config()
        self.timeout = self.config.get_timeout()
        self.base_url = self.config.get_base_url()
    
    def open(self, url=None):
        """打开页面"""
        if url:
            self.driver.get(url)
            logger.info(f"打开页面: {url}")
        elif self.base_url:
            self.driver.get(self.base_url)
            logger.info(f"打开基础页面: {self.base_url}")
    
    def find_element(self, locator):
        """查找单个元素，带显式等待"""
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                ec.presence_of_element_located(locator)
            )
            logger.info(f"找到元素: {locator}")
            return element
        except TimeoutException:
            msg = f"超时未找到元素: {locator}"
            logger.error(msg)
            take_screenshot(self.driver)
            raise TimeoutException(msg)
        except NoSuchElementException:
            msg = f"未找到元素: {locator}"
            logger.error(msg)
            take_screenshot(self.driver)
            raise ElementNotFoundException(msg)
    
    def find_elements(self, locator):
        """查找多个元素，带显式等待"""
        try:
            elements = WebDriverWait(self.driver, self.timeout).until(
                ec.presence_of_all_elements_located(locator)
            )
            logger.info(f"找到 {len(elements)} 个元素: {locator}")
            return elements
        except TimeoutException:
            msg = f"超时未找到元素: {locator}"
            logger.error(msg)
            take_screenshot(self.driver)
            raise TimeoutException(msg)
    
    def click(self, locator):
        """点击元素"""
        element = self.find_element(locator)
        element.click()
        logger.info(f"点击元素: {locator}")
    
    def send_keys(self, locator, text):
        """输入文本"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        logger.info(f"向元素 {locator} 输入文本: {text}")
    
    def get_text(self, locator):
        """获取元素文本"""
        text = self.find_element(locator).text
        logger.info(f"获取元素 {locator} 的文本: {text}")
        return text
    
    def is_displayed(self, locator):
        """判断元素是否可见"""
        try:
            displayed = self.find_element(locator).is_displayed()
            logger.info(f"元素 {locator} 可见性: {displayed}")
            return displayed
        except:
            return False
    
    def get_current_url(self):
        """获取当前页面URL"""
        url = self.driver.current_url
        logger.info(f"当前页面URL: {url}")
        return url
    
    def refresh(self):
        """刷新当前页面"""
        self.driver.refresh()
        logger.info("刷新页面")
    
    def back(self):
        """返回上一页"""
        self.driver.back()
        logger.info("返回上一页")
    
    def maximize_window(self):
        """最大化窗口"""
        self.driver.maximize_window()
        logger.info("窗口最大化")
    