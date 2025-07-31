import allure
import pytest
from src.page_objects.login_page import LoginPage
from src.page_objects.home_page import HomePage
from src.common.test_data import test_data
from src.common.assertions import assertions

@allure.feature("登录功能")
class TestLogin:
    
    @allure.story("使用正确的用户名和密码登录")
    @allure.title("成功登录系统")
    def test_login_success(self, driver, base_url):
        # 获取测试数据
        test_case = test_data.get_test_case_data("login_cases.xlsx", "login_001")
        
        # 执行登录操作
        login_page = LoginPage(driver)
        login_page.login(test_case["username"], test_case["password"])
        
        # 验证登录结果
        home_page = HomePage(driver)
        assertions.assert_url_contains(driver, "/home", "登录后应跳转到首页", driver)
        assertions.assert_true(home_page.is_user_menu_displayed(), "用户菜单应显示", driver)
        assertions.assert_equal(
            home_page.get_username(), 
            test_case["expected_username"], 
            "用户名显示不正确", 
            driver
        )
    
    @allure.story("使用错误的密码登录")
    @allure.title("登录失败并显示错误信息")
    def test_login_with_wrong_password(self, driver):
        # 获取测试数据
        test_case = test_data.get_test_case_data("login_cases.xlsx", "login_002")
        
        # 执行登录操作
        login_page = LoginPage(driver)
        login_page.login(test_case["username"], test_case["password"])
        
        # 验证错误信息
        assertions.assert_true(
            login_page.is_error_message_displayed(), 
            "错误提示应显示", 
            driver
        )
        assertions.assert_contains(
            login_page.get_error_message(), 
            test_case["expected_message"], 
            "错误提示信息不正确", 
            driver
        )
    
    @allure.story("使用空用户名登录")
    @allure.title("登录失败并提示用户名不能为空")
    def test_login_with_empty_username(self, driver):
        # 执行登录操作
        login_page = LoginPage(driver)
        login_page.open()
        login_page.enter_username("")
        login_page.enter_password("any_password")
        login_page.click_login_button()
        
        # 验证错误信息
        assertions.assert_true(
            login_page.is_error_message_displayed(), 
            "错误提示应显示", 
            driver
        )
        assertions.assert_contains(
            login_page.get_error_message(), 
            "用户名不能为空", 
            "错误提示信息不正确", 
            driver
        )
    
    @pytest.mark.skip(reason="暂未实现忘记密码功能")
    @allure.story("忘记密码功能")
    @allure.title("点击忘记密码链接跳转到密码重置页面")
    def test_forgot_password_link(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_forgot_password()
        
        assertions.assert_url_contains(
            driver, 
            "/forgot-password", 
            "点击忘记密码后应跳转到密码重置页面", 
            driver
        )
    