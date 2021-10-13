from os import environ
from behave import fixture

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
  context.variables = {}
  context.variables["USERNAME"] = environ.get('BK_USERNAME')
  context.variables["PASSWORD"] = environ.get('BK_PASSWORD')
  assert None != context.variables["USERNAME"], "please set BK_USERNAME env variable"
  assert None != context.variables["PASSWORD"], "please set BK_PASSWORD env variable"

def before_feature(context, feature):
  context.driver = webdriver.Chrome(ChromeDriverManager().install())

def after_feature(context, feature):
  context.driver.close()
