from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")

@when('I enter valid credentials')
def step_impl(context):
    username_input = context.driver.find_element(By.ID, 'user-name')
    password_input = context.driver.find_element(By.ID, 'password')
    username_input.send_keys('standard_user')
    time.sleep(1)
    password_input.send_keys('secret_sauce')
    time.sleep(1)

@when('click on the login button')
def step_impl(context):
    login_button = context.driver.find_element(By.ID, 'login-button')
    login_button.click()
    time.sleep(1)

@then('I should be logged in successfully')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html")
    )
    time.sleep(1)

@then('redirected to the products page')
def step_impl(context):
    assert context.driver.current_url == "https://www.saucedemo.com/inventory.html"
    time.sleep(1)
    context.driver.quit()
