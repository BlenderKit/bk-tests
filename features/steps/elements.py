import time
from decimal import *

from behave import *
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

elements = {
    # TOP HEADER
    'nav item MODELS': '/html/body/nav/div/div/div/div[1]/div/ul/li[1]/a',
    'nav item MATERIALS': '/html/body/nav/div/div/div/div[1]/div/ul/li[2]/a', 
    'nav item ADD-ONS': '/html/body/nav/div/div/div/div[1]/div/ul/li[3]/a',
    'nav item AUTHORS': '/html/body/nav/div/div/div/div[1]/div/ul/li[4]/a',
    'nav item SUBSCRIBE': '/html/body/nav/div/div/div/div[1]/ul/li[2]/a',
    'nav item WORKS': '//*[@id="navbarSupportedContent"]/div/div[1]/ul/li[4]/a',
    'LOG IN button': '/html/body/nav/div/div/div/div[2]/div/ul[1]/li/a',
    'PROFILE dropdown': '//*[@id="profile-dropdown"]',

    # ASSET-GALLERY
    'SEARCH field': '//*[@id="mySearch"]',
    'SEARCH submit': '//*[@id="mySearch"]/following-sibling::button',
    'FIRST SEARCH RESULT':'/html/body/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div/a',
    # asset-popup
    'ASSET POPUP': '//*[@id="assetModalDetail"]/div/div[1]/div',
    'ASSET POPUP NAME': '//*[@id="assetModalDetail"]/div/div/div/div[1]/div[1]/div[1]/h1',
    'ASSET POPUP DESCRIPTION': '//*[@id="assetModalDetail"]/div/div/div/div[1]/div[1]/div[1]/div[1]',
    'ASSET POPUP LICENSE': '//*[@id="assetModalDetail"]/div/div/div/div[1]/div[1]/div[1]/div[4]/a/img',
    'ASSET POPUP PLAN': '//*[@id="assetModalDetail"]/div/div/div/figure/div/a[1]',
    'ASSET POPUP AUTHOR NAME': '//*[@id="assetModalDetail"]/div/div/div/div[1]/div[1]/div[2]/div/a[2]',
    'ASSET POPUP AUTHOR AVATAR': '//*[@id="assetModalDetail"]/div/div/div/div[1]/div[1]/div[2]/div/a[1]/img',
    'ASSET POPUP GET MODEL button': '//*[@id="assetModalDetail"]/div/div/div/figure/div/a[2]',
    'ASSET POPUP CLOSE': '//*[@id="assetModalDetail"]/div/div/button',

    # WORKS /gallery

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
    
    'COUNTRY select': '//*[@id="id_country"]',
    'TAX PERCENTAGE span': '//*[@id="id_tax"]',
    'TAX VALUE span' : '//*[@id="id_tax_total"]/span[2]',
    'ORIGINAL PRICE span': '//*[@id="id_price"]/span[2]',
    'DISCOUNT PERCENTAGE span': '//*[@id="id_discount_percentage"]',
    'DISCOUNT VALUE span' : '//*[@id="id_discount"]/span[2]',
    'TOTAL PRICE span' : '//*[@id="id_total"]/span[2]',
 
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

    #DISCLAIMERS
    'PRICE DISCLAIMER close': '//*[@id="price-disclaimer"]',
    'DISCOUNT DISCLAIMER close': '//*[@id="discount_disclaimer"]',
}

def getSearchResultXPathByName(name:str) -> str:
  return "//a[contains(text(), '{0}') and contains(@class, 'pop')]".format(name)

def getWorkXPathByName(name:str) -> str:
  return "//a[contains(text(), '{0}') and contains(@class, 'pop')]".format(name)

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

@step('page contains clickable element "{alias}"')
def step_impl(context, alias):
    element = elements[alias]
    waitForElementToBeClickable(context, element)

@step('element "{alias}" contains text "{text}"')
def step_impl(context, alias, text):
    element = elements[alias]
    elem = waitForElementToLoad(context, element)
    assert text == elem.text, "condition: text==elem.text; values: text={text}, elem.text={elemText}; FAILED: {text} != {elemText}".format(text=text, elemText=elem.text)

@step('user clicks on element "{alias}"')
def step_impl(context, alias):
    element = elements[alias]
    elem = waitForElementToLoad(context, element)
    context.driver.execute_script("arguments[0].scrollIntoView();", elem)
    waitForElementToBeClickable(context, element)
    time.sleep(1) #ugly
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

@step('user selects "{option}" in dropdown menu "{alias}"')
def step_impl(context, option, alias):
    element = elements[alias]
    elem = waitForElementToLoad(context, element)
    select = Select(elem)
    select.select_by_visible_text(option)

@step('discount, tax and total price are calculated correctly')
def step_impl(context):
    discountPercentage = waitForElementToLoad(context, elements["DISCOUNT PERCENTAGE span"])
    discountPercentage = Decimal(discountPercentage.text)
    discountValue = waitForElementToLoad(context, elements["DISCOUNT VALUE span"])
    discountValue = Decimal(discountValue.text)

    taxPercentage = waitForElementToLoad(context, elements["TAX PERCENTAGE span"])
    taxPercentage = Decimal(taxPercentage.text)
    taxValue = waitForElementToLoad(context, elements["TAX VALUE span"])
    taxValue = Decimal(taxValue.text)

    originalPrice = waitForElementToLoad(context, elements["ORIGINAL PRICE span"])
    originalPrice = Decimal(originalPrice.text)
    totalPrice = waitForElementToLoad(context, elements["TOTAL PRICE span"])
    totalPrice = Decimal(totalPrice.text)

    expectedDiscountValue = originalPrice * discountPercentage / 100
    discountOK = expectedDiscountValue == discountValue

    expectedTaxValue = (originalPrice - discountValue) * taxPercentage / 100
    expectedTaxValueRounded = round(expectedTaxValue, 2)
    taxOK = expectedTaxValueRounded == taxValue  

    expectedTotalPrice = originalPrice - expectedDiscountValue + expectedTaxValue
    expectedTotalPrice = round(expectedTotalPrice, 2)
    totalOK = expectedTotalPrice == totalPrice 

    assert discountOK and taxOK and totalOK, """discountOK and taxOK and totalOK
    {discountOK}: expectedDiscountValue={expectedDiscountValue} == discountValue={discountValue}
    {taxOK}: expectedTaxValueRounded={expectedTaxValueRounded} == taxValue={taxValue}
    {totalOK}: expectedTotalPrice={expectedTotalPrice} == totalPrice={totalPrice}""".format(
        expectedDiscountValue=expectedDiscountValue,
        discountValue=discountValue,
        discountOK=discountOK,
        expectedTaxValueRounded=expectedTaxValueRounded,
        taxValue=taxValue,
        taxOK=taxOK,
        expectedTotalPrice=expectedTotalPrice,
        totalPrice=totalPrice,
        totalOK=totalOK
    )

@step('search result named "{name}" is present')
def step_impl(context, name):
  xpath = getSearchResultXPathByName(name)
  waitForElementToLoad(context, xpath)

@step('user clicks on search result named "{name}"')
def step_impl(context, name):
  xpath = getSearchResultXPathByName(name)
  element = waitForElementToBeClickable(context, xpath)
  element.click()

@step('user clicks on work named "{name}"')
def step_impl(context, name):
  xpath = getWorkXPathByName(name)
  element = waitForElementToBeClickable(context, xpath)
  context.driver.execute_script("arguments[0].scrollIntoView(false);", element)
  time.sleep(1) #ugly
  element.click()

@step('user is logged in')
def step_impl(context):
    context.execute_steps(u"""
        Given user navigates to "/accounts/login/"
          And page contains element "USERNAME input"
          And page contains element "PASSWORD input"
         When user types <BK_USERNAME> into element "USERNAME input"
          And user types <BK_PASSWORD> into element "PASSWORD input"
          And user clicks on element "LOG IN submit"
         Then they are on Homepage
          And page contains element "PROFILE dropdown"
    """)

@step('user closes disclaimers')
def step_impl(context):
  assert None == context.driver.get(context.variables["BK_TARGET"])

  try:
    element = waitForElementToBeClickable(context, elements["PRICE DISCLAIMER close"])
    #little bit hacky (cannot find the X button through xPath - it is populated via ::before)
    ActionChains(context.driver).move_to_element_with_offset(element, element.size["width"]-14, 0).click().perform()
  except:
    print("Price disclaimer not closed")

  try:
    element = waitForElementToBeClickable(context, elements["DISCOUNT DISCLAIMER close"])
    ActionChains(context.driver).move_to_element_with_offset(element, element.size["width"]-14, 0).click().perform()
  except:
    print("Discount disclaimer not closed")
    