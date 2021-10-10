from behave import *

elements = {
    'LOG IN button': '/html/body/nav/div/div/div/div[2]/div/ul[1]/li/a',
    'USERNAME input': '//*[@id="id_username"]',
    'PASSWORD input': '//*[@id="id_password"]',
    'LOG IN submit': '/html/body/div[2]/div/div[2]/form/input[3]',
    'PROFILE dropdown': '//*[@id="profile-dropdown"]',
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

@step('user types <{variable}> into element "{alias}"')
def step_impl(context, variable, alias):
    element = elements[alias]
    elem = context.driver.find_element_by_xpath(element)
    elem.send_keys(context.variables[variable])

@step('user types "{text}" into element "{alias}"')
def step_impl(context, text, alias):
    element = elements[alias]
    elem = context.driver.find_element_by_xpath(element)
    elem.send_keys(text)
