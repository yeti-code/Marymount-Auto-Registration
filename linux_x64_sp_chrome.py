from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


print("Welcome to the MU Course register bot! Don't forget that before you run me, you need to have an already pre-approved plan on canvas.")

user = input("Please enter your username: ")
password = input("Please enter your password: ")

print("You need to validate what you have entered: ", user, password)

creds_arg = str("y")

creds_input = input("If your information is correct press y, if it isn't correct hit n. ")

while creds_input != str("y"):
    print("Sending you back to re-enter information...: ")

    user = input("Please enter your username: ")
    password = input("Please enter your password: ")

    print("You need to validate what you have entered: ", user, password)

    creds_input = input("If your information is correct press y, if it isn't correct hit n. ")


def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="/r")
        time.sleep(1)
        t -= 1

t = input("You need to select how many seconds you want the bot to wait until execution... For example 3 hours is 10800 seconds.: ")

countdown(int(t))

print("Starting the bot!")



driver = webdriver.Chrome()



driver.get('https://selfservice.marymount.edu/Student/Account/Login?ReturnUrl=%2fStudent%2fPlanning%2fDegreePlans')


driver.implicitly_wait(5)

user_box = driver.find_element_by_id("UserName")
user_box.send_keys(user)

pass_box = driver.find_element_by_id("Password")
pass_box.send_keys(password)

click_login = driver.find_element_by_id("login-button")
click_login.click()

driver.implicitly_wait(10)

click_register = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"register-button")))
driver.execute_script("arguments[0].click();", click_register)



print("You should be registered now, but please do not forget to double check!!!")

print("Exiting script instance in 5 seconds. Thanks for using me!")

driver.implicitly_wait(5)