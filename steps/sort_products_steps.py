from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@when('I sort products by price (low to high)')
def step_impl(context):
    sort_dropdown = Select(context.driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    sort_dropdown.select_by_value('lohi')
    time.sleep(1)

@then('the products should be displayed in ascending order of price')
def step_impl(context):
    product_prices = context.driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    prices = [float(price.text[1:]) for price in product_prices]
    assert prices == sorted(prices)
    time.sleep(1)

@when('I sort products by price (high to low)')
def step_impl(context):
    sort_dropdown = Select(context.driver.find_element(By.CLASS_NAME, 'product_sort_container'))
    sort_dropdown.select_by_value('hilo')
    time.sleep(1)

@then('the products should be displayed in descending order of price')
def step_impl(context):
    product_prices = context.driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
    prices = [float(price.text[1:]) for price in product_prices]
    assert prices == sorted(prices, reverse=True)
    time.sleep(1)