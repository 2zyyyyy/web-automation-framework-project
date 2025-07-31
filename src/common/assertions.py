import allure
from src.common.logger import logger
from src.common.utils import take_screenshot

class Assertions:
    """自定义断言类，增强断言功能并集成日志和报告"""
    
    @staticmethod
    @allure.step("断言相等: 实际值 '{actual}' 应该等于 预期值 '{expected}'")
    def assert_equal(actual, expected, message=None, driver=None):
        """断言两个值相等"""
        try:
            assert actual == expected, message or f"实际值: {actual} 不等于 预期值: {expected}"
            logger.info(f"断言成功: {actual} == {expected}")
        except AssertionError as e:
            logger.error(f"断言失败: {str(e)}")
            # 如果提供了driver，测试失败时截图
            if driver:
                take_screenshot(driver, "assert_equal_failure")
            # 将失败信息添加到allure报告
            allure.attach(str(actual), name="实际值")
            allure.attach(str(expected), name="预期值")
            raise
    
    @staticmethod
    @allure.step("断言不相等: 实际值 '{actual}' 应该不等于 预期值 '{expected}'")
    def assert_not_equal(actual, expected, message=None, driver=None):
        """断言两个值不相等"""
        try:
            assert actual != expected, message or f"实际值: {actual} 等于 预期值: {expected}"
            logger.info(f"断言成功: {actual} != {expected}")
        except AssertionError as e:
            logger.error(f"断言失败: {str(e)}")
            if driver:
                take_screenshot(driver, "assert_not_equal_failure")
            allure.attach(str(actual), name="实际值")
            allure.attach(str(expected), name="预期值")
            raise
    
    @staticmethod
    @allure.step("断言包含: 实际值 '{actual}' 应该包含 预期值 '{expected}'")
    def assert_contains(actual, expected, message=None, driver=None):
        """断言实际值包含预期值"""
        try:
            assert expected in actual, message or f"实际值: {actual} 不包含 预期值: {expected}"
            logger.info(f"断言成功: {actual} 包含 {expected}")
        except AssertionError as e:
            logger.error(f"断言失败: {str(e)}")
            if driver:
                take_screenshot(driver, "assert_contains_failure")
            allure.attach(str(actual), name="实际值")
            allure.attach(str(expected), name="预期值")
            raise
    
    @staticmethod
    @allure.step("断言为真: '{condition}' 应该为 True")
    def assert_true(condition, message=None, driver=None):
        """断言条件为真"""
        try:
            assert condition, message or "条件应为True，但实际为False"
            logger.info(f"断言成功: 条件为True")
        except AssertionError as e:
            logger.error(f"断言失败: {str(e)}")
            if driver:
                take_screenshot(driver, "assert_true_failure")
            allure.attach(str(condition), name="实际条件结果")
            raise
    
    @staticmethod
    @allure.step("断言为假: '{condition}' 应该为 False")
    def assert_false(condition, message=None, driver=None):
        """断言条件为假"""
        try:
            assert not condition, message or "条件应为False，但实际为True"
            logger.info(f"断言成功: 条件为False")
        except AssertionError as e:
            logger.error(f"断言失败: {str(e)}")
            if driver:
                take_screenshot(driver, "assert_false_failure")
            allure.attach(str(condition), name="实际条件结果")
            raise
    
    @staticmethod
    @allure.step("断言URL包含: '{url}' 应该包含 '{expected}'")
    def assert_url_contains(driver, expected, message=None):
        """断言当前URL包含预期字符串"""
        actual_url = driver.current_url
        try:
            assert expected in actual_url, message or f"URL: {actual_url} 不包含: {expected}"
            logger.info(f"断言成功: URL {actual_url} 包含 {expected}")
        except AssertionError as e:
            logger.error(f"断言失败: {str(e)}")
            take_screenshot(driver, "assert_url_contains_failure")
            allure.attach(actual_url, name="实际URL")
            allure.attach(expected, name="预期包含内容")
            raise
    
    @staticmethod
    @allure.step("断言元素可见: {locator} 应该可见")
    def assert_element_visible(element, locator=None, message=None, driver=None):
        """断言元素可见"""
        try:
            assert element.is_displayed(), message or f"元素 {locator or ''} 不可见"
            logger.info(f"断言成功: 元素 {locator or ''} 可见")
        except AssertionError as e:
            logger.error(f"断言失败: {str(e)}")
            if driver:
                take_screenshot(driver, "assert_element_visible_failure")
            allure.attach(str(locator), name="元素定位器")
            raise

# 实例化断言工具
assertions = Assertions()
    