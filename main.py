from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

URL = "https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f"
email_input = "*****@gmail.com"
password_input = input("What is your password? If you don't remember your password, type N.\n")
search = input("What coding related question do you want to search for?\n")
ask_question = input("Do you want to ask a question? Y/N\n")
# forgot_email_url = "https://stackoverflow.com/users/account-recovery"


chrome_driver_path = "/Users/dejimakinde/Desktop/Coding Folder/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)


def logging_in():
    email = driver.find_element_by_id("email")
    email.send_keys(email_input)

    password = driver.find_element_by_id("password")
    password.send_keys(password_input)

    log_in = driver.find_element_by_id("submit-button")
    log_in.click()

    sleep(5)

    searching = driver.find_element_by_css_selector(".ps-relative input")
    searching.send_keys(search)
    sleep(2)
    searching.send_keys(Keys.ENTER)

    if ask_question == "Y":
        question_button = driver.find_element_by_link_text("Ask Question")
        question_button.click()
    else:
        pass


if password_input == "N":
    get_password = driver.find_element_by_link_text("Forgot password?")
    get_password.click()
    account_recovery = driver.find_element_by_id("email")
    account_recovery.send_keys(email_input)
    recovery_button = driver.find_element_by_id("submit-button")
    recovery_button.click()
else:
    logging_in()
