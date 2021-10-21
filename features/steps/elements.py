import time
from behave import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains

elements = {
    # TOP HEADER
    'SUBSCRIBE button': '/html/body/nav/div/div/div/div[1]/ul/li[2]/a',
    'LOG IN button': '/html/body/nav/div/div/div/div[2]/div/ul[1]/li/a',
    'PROFILE dropdown': '//*[@id="profile-dropdown"]',

    # LOGIN PAGE /accounts/login/
    'USERNAME input': '//*[@id="id_username"]',
    'PASSWORD input': '//*[@id="id_password"]',
    'LOG IN submit': '/html/body/div[2]/div/div[2]/form/input[3]',

    # SUBSCRIPTION PAGE
    'YEARLY switch': '/html/body/div[2]/div[2]/div/div/div/div/div[2]/div[3]/div[4]',
    'GET PLAN button': '/html/body/div[2]/div[2]/div/div/div/div/div[2]/div[5]/h4/a',
    #choosing plan
    'MONTHLY SUBS button': '/html/body/div[2]/div/div[2]/form/div/div[1]/div/div/div/div[3]/label/span',
    '30DAY GLIMPSE button': '/html/body/div[2]/div/div[2]/form/div/div[1]/div/div/div/div[2]/label/span',
    'PAYPAL SANDBOX switch': '/html/body/div[2]/div/div[2]/form/div/div[2]/div[3]/div/div/div/div[5]/label/h3',
    'TO PAYMENT button': '//*[@id="proceed_to_payment_btn"]',
    #paypal
    'PAYPAL MAIL input': '//*[@id="email"]',
    'PAYPAL PASS input': '//*[@id="password"]',
    'PAYPAL NEXT button': '//*[@id="btnNext"]',
    'PAYPAL LOGIN button': '//*[@id="btnLogin"]',
    'PAYMENT SUBMIT button': '//*[@id="payment-submit-btn"]',
    #welcome to Full Plan
    'INVOICE link': '//*[@id="order_printable_documents"]',

}

def waitForElementToLoad(context, element):
    elem = WebDriverWait(context.driver, 30, poll_frequency=5).until(
        EC.presence_of_element_located((By.XPATH, element)),
        'Timed out waiting for element to be located.')
    return elem

def waitForElementToBeClickable(context, element):
    elem = WebDriverWait(context.driver, 10, poll_frequency=5).until(
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
    elem = waitForElementToLoad(context, element)
    context.driver.execute_script("arguments[0].scrollIntoView();", elem)
    waitForElementToBeClickable(context, element)
    time.sleep(1)
    elem.click()

@step('user types <{variable}> into element "{alias}"')
def step_impl(context, variable, alias):
    element = elements[alias]
    elem = waitForElementToLoad(context, element)
    waitForElementToBeClickable(context, element)
    elem.send_keys(context.variables[variable])

@step('user types "{text}" into element "{alias}"')
def step_impl(context, text, alias):
    element = elements[alias]
    elem = waitForElementToLoad(context, element)
    waitForElementToBeClickable(context, element)
    elem.send_keys(text)
