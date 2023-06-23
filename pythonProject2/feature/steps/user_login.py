import time
from behave import *
from selenium.webdriver.common.by import By
from selenium import webdriver
import pdb

@given('Launch Chrome Browser for Vetcare')
def launchBrowser(context):
    #context.driver=webdriver.Chrome(executable_path="C:\\murtuza\\chromedriver_win32\chromedriver.exe")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    #time.sleep(10)
    #context.driver=webdriver.chrome()

@when('open login page')
def open_login_page(context):
    #pdb.set_trace()  # Set breakpoint here
    #breakpoint()
    context.driver.get("https://user-dev.petcareclub.vet/murtuza/")
    context.driver.implicitly_wait(10)


@when('Enter username "{user}" and password "{pwd}"')
def enter_username_and_password(context, user, pwd):
    username_field = context.driver.find_element(By.XPATH, "//input[@formcontrolname='email']")
    username_field.send_keys(user)
    password_field = context.driver.find_element(By.XPATH, "//input[@formcontrolname='password']")
    password_field.send_keys(pwd)

@When('Click on Login button')
def verify_successful_login(context):
    main_page_element = context.driver.find_element(By.XPATH, "/html/body/app-root/app-signin/div/div/div[1]/div/form/button")
    main_page_element.click()


@then('user must sucessfully login on the main page')
def sucessfully_login_main_page(context):
    try:
        status = context.driver.find_element(By.ID, "drawerLogoImage").is_displayed()
        context.driver.implicitly_wait(10)
    except:
        #context.driver.close()
        assert False, "Test Failed"
    if status:
        #context.driver.close()
        assert True, "Test Passed"

@When('the user clicks the text button')
def call_to_vet(context):
    #breakpoint()
    #pdb.set_trace()  # Set breakpoint here
    try:
        #context.driver.get("https://user-dev.petcareclub.vet/murtuza/main/home")
        status = context.driver.find_element(By.XPATH, "/html/body/app-root/app-drawer/mat-drawer-container/mat-drawer-content/app-home/div/div[3]/div[2]/app-recent-chats/div/div/div/div[2]/div/div/div[2]/div[2]")
        status.click()
        time.sleep(5)
    except:
        #context.driver.close()
        assert False, "Test Failed"
    if status == "Contact a Vet":
        #context.driver.close()
        assert True, "Test Passed"


@then('The user start the text chat')
def text_chat(context):
    try:
        status = context.driver.find_element(By.XPATH, "/html/body/app-root/app-drawer/mat-drawer-container/mat-drawer-content/app-talk-to-vet/div/div[2]/div/div/div/div/div/button")
        status.click()
        time.sleep(10)
    except:
        assert False, "Go to last chat"
    if status:
        assert True, "Test Passed"

@then('Type text message')
def chat(context):
    try:
        status = context.driver.find_element(By.ID, "msg-field")
        status.send_keys("Test message")
        time.sleep(5)
    except:
        assert False, "Test Fail"
    if status:
        assert True, "Test Passed"

@then('send button')
def send(context):
    try:
        status = context.driver.find_element(By.ID, "send_1_").click()
        time.sleep(5)
    except:
        assert False, "Test Fail"
    if status:
        assert True, "Test Passed"



@then(u'the user can perform further actions')
def further_action(context):
    text = context.driver.find_element(By.XPATH, "/html/body/app-root/app-drawer/mat-drawer-container/mat-drawer-content/app-conversation/div/div[2]/div[1]/div/div[2]/button")
    text.click()
    time.sleep(10)
    assert True, "Test Passed"

#context.driver.implicitly_wait(3)
 #   while True:
  #      context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
   #     time.sleep(3)