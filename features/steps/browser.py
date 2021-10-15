from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

elements = {
    'LOG IN button': '/html/body/nav/div/div/div/div[2]/div/ul[1]/li/a',
    'USERNAME input': '//*[@id="id_username"]',
    'PASSWORD input': '//*[@id="id_password"]'
}

@given('user has Chrome running')
def step_impl(context):
    assert None != context.driver

@when('user opens BlenderKit')
def step_impl(context):
    assert None == context.driver.get("https://devel.blenderkit.com")

@then('page will include text "{text}"')
def step_impl(context, text):
    assert text in context.driver.page_source

def waitForPageToLoad(context, location):
    regex = r'http(?:s|)://.*blenderkit.com' + location
    WebDriverWait(context.driver, 30, poll_frequency=5).until(
        EC.url_matches(regex),
        'Timed out waiting for page to load. URL does not match: {expected}, current URL {current}'.format(expected=regex,current=context.driver.current_url))

@step('they are on "{location}"')
def step_impl(context, location):
    waitForPageToLoad(context, location)
    
@step('they are on Homepage')
def step_impl(context):
    waitForPageToLoad(context, "/")

@step('wait')
def step_impl(context):
    while True:
        pass
