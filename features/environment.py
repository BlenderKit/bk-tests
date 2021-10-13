from os import environ

from selenium.webdriver.chrome import options
from behave import fixture

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
  context.variables = {}
  context.variables["USERNAME"] = environ.get('BK_USERNAME')
  context.variables["PASSWORD"] = environ.get('BK_PASSWORD')
  assert None != context.variables["USERNAME"], "please set BK_USERNAME env variable"
  assert None != context.variables["PASSWORD"], "please set BK_PASSWORD env variable"

def before_feature(context, feature):
  options = set_chrome_options()
  context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def after_feature(context, feature):
  context.driver.close()

def set_chrome_options() -> None:
  chrome_options = Options()

  if environ.get('BK_IS_DOCKER', False):
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}

  return chrome_options
