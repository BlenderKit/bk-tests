from behave import *

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

@step('they are on "{location}"')
def step_impl(context, location):
    URL = context.driver.current_url
    assert location in URL

@step('wait')
def step_impl(context):
    while True:
        pass

"""    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in context.driver.page_source
    context.driver.close()
"""
