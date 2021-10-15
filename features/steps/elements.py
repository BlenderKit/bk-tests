from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

elements = {
    'LOG IN button': '/html/body/nav/div/div/div/div[2]/div/ul[1]/li/a',
    'USERNAME input': '//*[@id="id_username"]',
    'PASSWORD input': '//*[@id="id_password"]',
    'LOG IN submit': '/html/body/div[2]/div/div[2]/form/input[3]',
    'PROFILE dropdown': '//*[@id="profile-dropdown"]',
}

def waitForElementToLoad(context, element):
    elem = WebDriverWait(context.driver, 30, poll_frequency=5).until(
        EC.presence_of_element_located((By.XPATH, element)),
        'Timed out waiting for element to be located.')
    return elem

def waitForElementToBeClickable(context, element):
    elem = WebDriverWait(context.driver, 30, poll_frequency=5).until(
        EC.element_to_be_clickable((By.XPATH, element)),
        'Timed out waiting for element to be clickable.')
    return elem

@step('page contains element "{alias}"')
def step_impl(context, alias):
    element = elements[alias]
    waitForElementToLoad(context, element)

@step('user clicks on element "{alias}"')
def step_impl(context, alias):
    element = elements[alias]
    elem = waitForElementToBeClickable(context, element)
    elem.click()

@step('user types <{variable}> into element "{alias}"')
def step_impl(context, variable, alias):
    element = elements[alias]
    elem = waitForElementToLoad(context, element)
    elem.send_keys(context.variables[variable])

@step('user types "{text}" into element "{alias}"')
def step_impl(context, text, alias):
    element = elements[alias]
    elem = waitForElementToLoad(context, element)
    elem.send_keys(text)
