import re, time
from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@step('user has Chrome running')
def step_impl(context):
    assert None != context.driver

#TODO: parametrize the base URL of tested server
@step('user opens BlenderKit')
def step_impl(context):
    assert None == context.driver.get(context.variables["BK_TARGET"])

#TODO: parametrize the base URL of tested server
@step('user navigates to "{location}"')
def step_impl(context, location):
    url = context.variables["BK_TARGET"] + location
    assert None == context.driver.get(url)

@step('page includes text "{text}"')
def step_impl(context, text):
    print(context.driver.page_source)
    print(context.driver.current_url)
    print("text:",text)
    if text in context.driver.page_source:
        print("text is present")
    assert text in context.driver.page_source

def waitForPageToLoad(context, location):
    regex = r'http(?:s|)://.*blenderkit.com' + re.escape(location)
    WebDriverWait(context.driver, 30, poll_frequency=5).until(
        EC.url_matches(regex),
        'Timed out waiting for page to load. URL does not match: {expected}, current URL {current}'.format(expected=regex,current=context.driver.current_url))

@step('they are on "{location}"')
def step_impl(context, location):
    waitForPageToLoad(context, location)
    
@step('they are on Homepage')
def step_impl(context):
    waitForPageToLoad(context, "/")

@step('user waits for "{seconds}" seconds')
def step_impl(context, seconds):
  time.sleep(int(seconds))

@step('user waits forever')
def step_impl(context):
  while True:
    time.sleep(10)
