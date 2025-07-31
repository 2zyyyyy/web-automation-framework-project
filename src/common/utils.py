import os
import time
from datetime import datetime
from src.common.logger import logger

def take_screenshot(driver, name_prefix="screenshot"):
    """
    截取当前页面截图并保存
    :param driver: 浏览器驱动实例
    :param name_prefix: 截图文件名前缀
    :return: 截图文件路径
    """
    try:
        # 截图目录
        screenshot_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
            'screenshots'
        )
        
        # 确保目录存在
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        
        # 生成唯一的文件名
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        screenshot_name = f"{name_prefix}_{timestamp}.png"
        screenshot_path = os.path.join(screenshot_dir, screenshot_name)
        
        # 截图并保存
        driver.save_screenshot(screenshot_path)
        logger.info(f"截图成功，保存路径: {screenshot_path}")
        return screenshot_path
    except Exception as e:
        logger.error(f"截图失败: {str(e)}")
        return None

def wait_for(condition, timeout=10, interval=0.5, message="条件未满足"):
    """
    等待条件满足
    :param condition: 要满足的条件(函数)
    :param timeout: 超时时间(秒)
    :param interval: 检查间隔(秒)
    :param message: 超时错误信息
    :return: 条件的返回值
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        result = condition()
        if result:
            return result
        time.sleep(interval)
    raise TimeoutError(f"{message} (超时 {timeout} 秒)")

def get_project_root():
    """获取项目根目录路径"""
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    