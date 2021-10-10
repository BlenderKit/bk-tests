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

@step('they are on Homepage')
def step_impl(context):
    URL = context.driver.current_url
    assert URL.endswith("blenderkit.com/")

@step('wait')
def step_impl(context):
    while True:
        pass
