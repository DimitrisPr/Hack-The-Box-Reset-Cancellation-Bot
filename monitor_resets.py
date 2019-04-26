import string
import time
import threading
from selenium import webdriver
driver = webdriver.Chrome('./chromedriver') 

#--------Change these-------#

username = 'your_email_here'
password = 'yur_password_here'
machine_name = "the_machine_name_here"

#----------------------------#

login_url = "https://www.hackthebox.eu/login"

def main():
    driver.get(login_url)
    login()

def login():

        #login & redirect to shoutbox
        login_form = driver.find_element_by_name('email')
        login_form.send_keys(username)
        login_form = driver.find_element_by_name('password')
        login_form.send_keys(password)
        login_form.submit()
        driver.get("https://www.hackthebox.eu/home/shoutbox")
        
        print("I monitor and cancel resets... You root it!")

        time.sleep(5) #make sure page is loaded

        #Every 5 seconds, check if a reset request is issued on machine of interest.
        #if it is, cancel it

        print("I monitor and cancel resets... You root it!")
        while True:
                detect_resets() 
                time.sleep(5)

def detect_resets():
        varname = 'issued a reset on ' + machine_name
        last_messages = [
                driver.find_elements_by_css_selector("div[class=bs-example] p")[-1].text,
                driver.find_elements_by_css_selector("div[class=bs-example] p")[-2].text,
                driver.find_elements_by_css_selector("div[class=bs-example] p")[-3].text
        ]
        
        for message in last_messages:

                if "requested a reset on " + machine_name in message and "/cancel" in message:
                        cancellation_id = extract_id_from_message(message)
                        print("Detected reset on " + machine_name + ", with id: " + cancellation_id)
                        cancel_reset(cancellation_id)

def extract_id_from_message(message):
        return message[message.index("/cancel") + len("/cancel"):].replace(" ", "")[0:6]

def cancel_reset(cancellation_id):

        print("Cancelling reset...")
        chat_input = driver.find_element_by_class_name('emojionearea-editor')
        chat_input.send_keys("/cancel " + cancellation_id)
        button = driver.find_elements_by_css_selector("div[class=panel-footer] button")[0].click()
        print("Reset Succesfully Canceled!")


main()
