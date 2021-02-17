import string
import time
import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome('./chromedriver', chrome_options=options)

print("""===============================
         Machine Reset Cancellation Bot
         ===============================
      """)

# Change these
username = 'your_username'
password = 'your_password'
machine_name = "machine_name"
login_url = "https://www.hackthebox.eu/login"

def main():
    print("Logging in...")
    driver.get(login_url)
    login()


def login():
    # login & redirect to shoutbox
    login_form = driver.find_element_by_name('email')
    login_form.send_keys(username)
    login_form = driver.find_element_by_name('password')
    login_form.send_keys(password)
    login_form.submit()

    driver.get("https://www.hackthebox.eu/home/shoutbox")

    print("\n########################################################")
    print("Started monitoring resets for machine: '" + machine_name + "'")
    print("If a reset occurs it will be automatically cancelled and you will be notified. \nGood Luck!")
    print("########################################################\n")

    # Ensure that the page is loaded - To be changed with ImplicitWait()
    time.sleep(5)  
    while True:
        detect_resets()
        time.sleep(1) # To be changed with ImplicitWait()


def detect_resets():
    message = driver.find_elements_by_css_selector(
        "div[class=bs-example] p")[-1].text

    if "requested a reset on " + machine_name in message and "/cancel" in message:
        cancellation_id = extract_id_from_message(message)
        print("Detected reset on " + machine_name +
              ", with id: " + cancellation_id)
        cancel_reset(cancellation_id)


def extract_id_from_message(message):
    return message[message.index("/cancel") + len("/cancel"):].replace(" ", "")[0:6]


def cancel_reset(cancellation_id):
    print("Cancelling reset...")
    chat_input = driver.find_element_by_class_name('emojionearea-editor')
    chat_input.send_keys("/cancel " + cancellation_id)
    button = driver.find_elements_by_css_selector(
        "div[class=panel-footer] button")[0].click()
    print("Reset Succesfully Canceled!")

if __name__ = "__main__":
    main()
