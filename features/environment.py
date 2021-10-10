from behave import fixture

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chromedriver_py import binary_path

def before_feature(context, feature):
  context.driver = webdriver.Chrome(executable_path=binary_path)
