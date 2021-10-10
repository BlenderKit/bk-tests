from behave import *

elements = {
    'LOG IN button': '/html/body/nav/div/div/div/div[2]/div/ul[1]/li/a',
    'USERNAME input': '//*[@id="id_username"]',
    'PASSWORD input': '//*[@id="id_password"]'
}

@step('page includes element "{alias}"')
def step_impl(context, alias):
    element = elements[alias]
    assert None != context.driver.find_element_by_xpath(element)

@step('user clicks on element "{alias}"')
def step_impl(context, alias):
    element = elements[alias]
    elem = context.driver.find_element_by_xpath(element)
    assert None != elem
    elem.click()
