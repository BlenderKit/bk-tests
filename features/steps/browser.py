from behave import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chromedriver_py import binary_path

@given('user has Chrome running')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=binary_path)

@when('user opens BlenderKit')
def step_impl(context):
    context.driver.get("https://devel.blenderkit.com")

@then('page will include "{text}"')
def step_impl(context, text):
    assert text in context.driver.page_source


@then('pagedd will include "{text}"')
def step_impl(context):
    
    elem = context.driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in context.driver.page_source
    context.driver.close()