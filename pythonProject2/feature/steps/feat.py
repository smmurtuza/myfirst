import time
from selenium.webdriver.common.by import By
from behave import *
import contextlib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@given('Launch Chrome Browser')
def launchBrowser(context):
    #context.driver=webdriver.Chrome(executable_path="C:\\murtuza\\chromedriver_win32\chromedriver.exe")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    #time.sleep(10)
    #context.driver=webdriver.chrome()

@when('open vetcare user page')
def open_vetcareuser_Page(context):
    context.driver.get("https://user-dev.petcareclub.vet/testahsan")
    #raise NotImplementedError(u'STEP: When open vetcare user page')


@then('Verify that the logo present on page')
def verify_logo(context):
    #status=context.driver.find_element_by_id("logoImage").is_displayed()
    #status = context.driver.find_element_by_id("logoImage").is_displayed()
    status = context.driver.find_element(By.ID, "logoImage").is_displayed()

    assert status is True

@then('close program')
def closeBrowser(context):
    context.driver.close()


#@given('we have behave installed')
#def step_impl(context):
 #   print("user id: murtuza.com")
  #  pass
"""
@when('we implement a test')
def step_impl(context):
    assert 2==4, "This eq is not correct"

@then('behave will test it for us!')
def step_impl(context):
    print("Login Sucessful")

@step("correct profile opened")
def step_impl(context):
    print("correct profile opened")
"""