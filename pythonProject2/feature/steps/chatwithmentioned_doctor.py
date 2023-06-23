import time
import pdb
from behave import *
from selenium.webdriver.common.by import By
from selenium import webdriver


@given('Launch Chrome Browser for user')
def launchBrowser(context):
    # context.driver=webdriver.Chrome(executable_path="C:\\murtuza\\chromedriver_win32\chromedriver.exe")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    # time.sleep(10)
    # context.driver=webdriver.chrome()


@when('open log_in page')
def open_login_page(context):
    context.driver.get("https://user-dev.petcareclub.vet/murtuza/")
    context.driver.implicitly_wait(10)


@when('Please Enter username "{user}" and password "{pwd}"')
def enter_username_and_password(context, user, pwd):
    #pdb.set_trace()
    username_field = context.driver.find_element(By.XPATH, "//input[@formcontrolname='email']")
    username_field.send_keys(user)
    password_field = context.driver.find_element(By.XPATH, "//input[@formcontrolname='password']")
    password_field.send_keys(pwd)


@When('Now Click on Login button')
def verify_successful_login(context):
    main_page_element = context.driver.find_element(By.XPATH,
                                                    "/html/body/app-root/app-signin/div/div/div[1]/div/form/button")
    main_page_element.click()


@then('Now user must sucessfully login on the main page')
def sucessfully_login_main_page(context):
    try:
        status = context.driver.find_element(By.ID, "drawerLogoImage").is_displayed()
        context.driver.implicitly_wait(10)
    except:
        # context.driver.close()
        assert False, "Test Failed"
    if status:
        # context.driver.close()
        assert True, "Test Passed"


@When('after the user clicks the text button')
def call_to_vet(context):
    try:
        # context.driver.get("https://user-dev.petcareclub.vet/murtuza/main/home")
        status = context.driver.find_element(By.XPATH, '/html/body/app-root/app-drawer/mat-drawer-container/mat-drawer-content/app-home/div/div[1]/div/div[2]/button')
        status.click()
        context.driver.implicitly_wait(10)
        #time.sleep(2)
    except:
        # context.driver.close()
        assert False, "Test Failed"
    if status == "Contact a Vet":
        # context.driver.close()
        assert True, "Test Passed"


@When('then The user start the text chat')
def text_chat(context):
    try:
        status = context.driver.find_element(By.XPATH, "/html/body/app-root/app-drawer/mat-drawer-container/mat-drawer-content/app-talk-to-vet/div/div[2]/div/div/div/div/div/button")
        status.click()
        context.driver.implicitly_wait(10)
        time.sleep(3)
    except:
        assert False, "Test Failed"
    if status:
        assert True, "Test Passed"
        pass

@When('select chat type')
def star_chat_with_specific_vet(context):
    try:
        status = context.driver.find_element(By.XPATH, "//button[@class='mat-focus-indicator primary-btn mat-stroked-button mat-button-base']")
        status.click()
        context.driver.implicitly_wait(10)
        time.sleep(4)
    except:
            #assert False, "test failed"
        pass
    if context.driver.find_element(By.XPATH, "//button[@class='mat-focus-indicator w-100 primary-btn mt-4 border-top mat-flat-button mat-button-base']").click():
        time.sleep(10)
        context.driver.implicitly_wait(10)
        assert True, "Test Passed"
"""
@When('select chat type')
def chat_with_specificvet(context):
        status = context.driver.find_element(By.XPATH, "//button[@class='mat-focus-indicator primary-btn mat-stroked-button mat-button-base']")
        status.click()
        time.sleep(5)
"""

@When('now Type text message')
def chat(context):
    try:
        status = context.driver.find_element(By.ID, "msg-field")
        status.send_keys("Test message")
        time.sleep(5)
    except:
        assert False, "Test Fail"
    if status:
        context.driver.implicitly_wait(10)
        assert True, "Test Passed"


@then('click on send button')
def send(context):
    try:
        status = context.driver.find_element(By.ID, "send_1_").click()
        time.sleep(4)
    except:
        assert False, "Test Fail"
    if status:
        assert True, "Test Passed"
        context.driver.implicitly_wait(10)


@then(' user can perform further actions')
def further_action(context):
    try:
        text = context.driver.find_element(By.XPATH, "/html/body/app-root/app-drawer/mat-drawer-container/mat-drawer-content/app-conversation/div/div[2]/div[1]/div/div[2]/button")
        text.click()
        time.sleep(10)
    except:
        assert False, "Test Fail"

    assert True, "Test Passed"

# context.driver.implicitly_wait(3)
#   while True:
#      context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)
