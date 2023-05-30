from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('there is an item in the cart')
def step_impl(context):
    add_to_cart_button = context.driver.find_element(By.XPATH, "//button[text()='Add to cart']")
    add_to_cart_button.click()
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[text()='Remove']"))
    )

@when('I remove the item from the cart')
def step_impl(context):
    remove_button = context.driver.find_element(By.XPATH, "//button[text()='Remove']")
    remove_button.click()

@then('the item should be removed successfully')
def step_impl(context):
    WebDriverWait(context.driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, "//button[text()='Remove']"))
    )

@then('the cart count should decrease')
def step_impl(context):
    cart_count = context.driver.find_elements(By.CLASS_NAME, 'shopping_cart_badge')
    print('cart_count', cart_count);
    assert len(cart_count) == 0
    context.driver.quit()
