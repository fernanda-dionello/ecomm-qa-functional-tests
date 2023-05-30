from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@when('I click on the logout button')
def step_impl(context):
    burguer_button = context.driver.find_element(By.ID, 'react-burger-menu-btn');
    burguer_button.click();
    time.sleep(1)
    context.driver.implicitly_wait(10);
    logout_button = context.driver.find_element(By.ID, 'logout_sidebar_link');
    logout_button.click();
    time.sleep(1)

@then('I should be logged out successfully')
def step_impl(context):
    login_button = context.driver.find_element(By.ID, 'login-button')
    assert login_button.is_displayed()
    time.sleep(1)

@then('redirected to the login page')
def step_impl(context):
    assert context.driver.current_url == "https://www.saucedemo.com/"
    time.sleep(1)
    context.driver.quit()
