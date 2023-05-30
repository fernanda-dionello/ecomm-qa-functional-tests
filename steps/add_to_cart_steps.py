from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('I am logged in')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    username_input = context.driver.find_element(By.ID, 'user-name')
    password_input = context.driver.find_element(By.ID, 'password')
    username_input.send_keys('standard_user')
    time.sleep(1)
    password_input.send_keys('secret_sauce')
    time.sleep(1)
    login_button = context.driver.find_element(By.ID, 'login-button')
    login_button.click()
    time.sleep(1)
    WebDriverWait(context.driver, 10).until(
        EC.url_to_be("https://www.saucedemo.com/inventory.html")
    )
    time.sleep(1)

@when('I add an item to the cart')
def step_impl(context):
    add_to_cart_button = context.driver.find_element(By.XPATH, "//button[text()='Add to cart']")
    add_to_cart_button.click()
    time.sleep(1)

@then('the item should be added successfully')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Remove']"))
    )
    time.sleep(1)

@then('the cart count should increase')
def step_impl(context):
    cart_count = context.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert cart_count.text == "1"
    time.sleep(1)
    context.driver.quit()
