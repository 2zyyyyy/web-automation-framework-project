from selenium.webdriver.common.by import By
from src.page_objects.base_page import BasePage

class LoginPage(BasePage):
    """登录页面对象"""
    
    # 元素定位器
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "忘记密码")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = f"{self.base_url}/login"
    
    def open(self, url=None):
        """打开登录页面"""
        super().open(self.page_url)
    
    def enter_username(self, username):
        """输入用户名"""
        self.send_keys(self.USERNAME_INPUT, username)
    
    def enter_password(self, password):
        """输入密码"""
        self.send_keys(self.PASSWORD_INPUT, password)
    
    def click_login_button(self):
        """点击登录按钮"""
        self.click(self.LOGIN_BUTTON)
    
    def login(self, username, password):
        """完整登录流程"""
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
    
    def get_error_message(self):
        """获取错误提示信息"""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_message_displayed(self):
        """判断错误提示是否显示"""
        return self.is_displayed(self.ERROR_MESSAGE)
    
    def click_forgot_password(self):
        """点击忘记密码链接"""
        self.click(self.FORGOT_PASSWORD_LINK)
    