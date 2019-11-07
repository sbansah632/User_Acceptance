from behave import *
from selenium import webdriver

use_step_matcher("re")


@given("User is on the patient management app homepage")
def step_impl(context):
    context.browser = webdriver.Chrome("C:/Users/sbansah/PycharmProjects/User_Acceptance/venv/ChromeDriver/chromedriver")
    context.browser.get("http://localhost:3000/")


@When('User  enters "Veronica" in the "firstName" field')
def step_impl(context):
    first_name_entry = context.browser.find_element_by_name('firstName')
    first_name_entry.send_keys("Veronica")


@step('User enters "Ann" in the "middleName" field')
def step_impl(context):
    middle_name_entry = context.browser.find_element_by_name('middleName')
    middle_name_entry.send_keys("Ann")


@step('User enters "Bansah" in the "lastName" field')
def step_impl(context):
    last_name_entry = context.browser.find_element_by_name('lastName')
    last_name_entry.send_keys("Bansah")


@step('User enters "024-763-2527" in the "phoneNumber" field')
def step_impl(context):
    phone_number_entry = context.browser.find_element_by_name('phoneNumber')
    phone_number_entry.send_keys("024-763-2527")


@step('User enters "03 - 27 - 90" in the "dob" field')
def step_impl(context):
    dob_entry = context.browser.find_element_by_name('dob')
    dob_entry.send_keys("03 - 27 - 90")


@step('User enters "Egret Lane" in the "address" field')
def step_impl(context):
    address_entry = context.browser.find_element_by_name('address')
    address_entry.send_keys("Egret Lane")


@step('User clicks on the Add New User button')
def step_impl(context):
    add_new_user = context.browser.find_element_by_css_selector('a.sc-EHOje.bnotRN')
    add_new_user.click()


@Then("Patient card is created")
def step_impl(context):
    assert context.browser.find_element_by_css_selector('main.sc-dnqmqq.kPXXsQ').is_displayed()




