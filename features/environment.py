import os
from pathlib import Path
import shutil

from behave import fixture
from behave.model_core import Status

from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
  context.variables = {}
  context.variables["BK_TARGET"] = os.getenv("BK_TARGET")
  context.variables["BK_USERNAME"] = os.getenv("BK_USERNAME")
  context.variables["BK_PASSWORD"] = os.getenv("BK_PASSWORD")
  context.variables["PP_USERNAME"] = os.getenv("PP_USERNAME")
  context.variables["PP_PASSWORD"] = os.getenv("PP_PASSWORD")

  if context.variables["BK_TARGET"] in [None, "devel", "dev"]:
    context.variables["BK_TEST_TYPE"] = "dev"
    context.variables["BK_TARGET"] = "https://devel.blenderkit.com"
    assert None != context.variables["BK_USERNAME"], "please set BK_USERNAME env variable"
    assert None != context.variables["BK_PASSWORD"], "please set BK_PASSWORD env variable"

  elif context.variables["BK_TARGET"] in ["staging", "stage"]:
    context.variables["BK_TEST_TYPE"] = "stage"
    context.variables["BK_TARGET"] = "https://staging.blenderkit.com"
    context.variables["BK_USERNAME"] = os.getenv("BK_USERNAME_STAGE", context.variables["BK_USERNAME"])
    context.variables["BK_PASSWORD"] = os.getenv("BK_PASSWORD_STAGE", context.variables["BK_PASSWORD"])
    context.variables["PP_USERNAME"] = os.getenv("PP_USERNAME_STAGE", context.variables["PP_USERNAME"])
    context.variables["PP_PASSWORD"] = os.getenv("PP_PASSWORD_STAGE", context.variables["PP_PASSWORD"])
    assert None != context.variables["BK_USERNAME"], "please set BK_USERNAME_STAGE or BK_USERNAME env variable (first if set overwrites second)"
    assert None != context.variables["BK_PASSWORD"], "please set BK_PASSWORD_STAGE or BK_PASSWORD env variable (first if set overwrites second)"

  elif context.variables["BK_TARGET"] in ["production", "prod"]:
    context.variables["BK_TEST_TYPE"] = "prod"
    context.variables["BK_TARGET"] = "https://blenderkit.com"
    context.variables["BK_USERNAME"] = os.getenv("BK_USERNAME_PROD", context.variables["BK_USERNAME"])
    context.variables["BK_PASSWORD"] = os.getenv("BK_PASSWORD_PROD", context.variables["BK_PASSWORD"])
    context.variables["PP_USERNAME"] = os.getenv("PP_USERNAME_PROD", context.variables["PP_USERNAME"])
    context.variables["PP_PASSWORD"] = os.getenv("PP_PASSWORD_PROD", context.variables["PP_PASSWORD"])
    assert None != context.variables["BK_USERNAME"], "please set BK_USERNAME_PROD or BK_USERNAME env variable (first if set overwrites second)"
    assert None != context.variables["BK_PASSWORD"], "please set BK_PASSWORD_PROD or BK_PASSWORD env variable (first if set overwrites second)"

  print("INFO: running the tests on server {}".format(context.variables["BK_TARGET"]))
  print("For different target set env variable BK_TARGET to full URL or use shortcuts: devel, stage, production.")
  print("When left empty the target is devel by default.")

  if os.path.isdir("screenshots"):
    shutil.rmtree("screenshots")

def before_feature(context, feature):
  options = set_chrome_options()
  context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
  context.featureDirectory = "screenshots/{feature}".format(feature=feature.filename)
  Path(context.featureDirectory).mkdir(parents=True, exist_ok=True)

def after_feature(context, feature):
  context.driver.close()

def before_scenario(context, scenario):
  test_type = context.variables["BK_TEST_TYPE"]
  if test_type == "prod" and "dev" in context.tags:
    scenario.skip(f"Test type '{test_type}' and scenario tagged as 'dev'")
  if test_type == "dev" and "prod" in context.tags:
    scenario.skip(f"Test type '{test_type}' and scenario tagged as 'prod'")

def after_step(context, step):
  if step.status == Status.failed:
    context.driver.save_screenshot("{fd}/{line}-{status}-{name}.png".format(
      fd=context.featureDirectory,
      line=step.line,
      status=step.status,
      name=step.name))

def set_chrome_options() -> None:
  chrome_options = Options()
  chrome_options.add_argument("--window-size=1920,1080")

  if os.environ.get('BK_IS_DOCKER', False):
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}

  return chrome_options
