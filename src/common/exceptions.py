"""自定义异常类集合"""

class AutomationException(Exception):
    """框架基础异常类"""
    pass

class PageNotFoundException(AutomationException):
    """页面未找到异常"""
    pass

class ElementNotFoundException(AutomationException):
    """元素未找到异常"""
    pass

class TimeoutException(AutomationException):
    """超时异常"""
    pass

class TestDataException(AutomationException):
    """测试数据异常"""
    pass

class ConfigurationException(AutomationException):
    """配置异常"""
    pass
    