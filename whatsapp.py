from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options



def load_settings():
    settings = {
        'browser': 'firefox',
        'browser_path': '/home/josua/.mozilla/firefox/3v4idfl6.webscraping',
        'name': 'Meine Gruppe',
        'page': 'https://web.whatsapp.com/'
    }
    return settings


def load_driver(settings):
    firefox_profile = webdriver.FirefoxProfile(settings['browser_path'])
    options = Options()
    options.headless = False
    driver = webdriver.Firefox(firefox_profile, options=options)

    return driver

def open_chat(driver, name):
    #search_field = driver.find_element_by_xpath('//div[text() = "Suchen oder neuen Chat beginnen"]/parent::div/descendant::div[@contenteditable="true"]')
    #search_field.send_keys(name)
    chat = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    chat.click()

def send_message(driver, username, message, count):
    open_chat(driver, username)

    msg_box = driver.find_element_by_xpath('//div[@spellcheck = "true"]')
    for _ in range(count):
        msg_box.send_keys(message)

        button = driver.find_element_by_xpath('//span[@data-icon="send"]/parent::button')
        button.click()



def read_last_in_message(driver):
    """
    Reading the last message that you got in from the chatter
    """
    for messages in driver.find_elements_by_xpath(
            "//div[contains(@class,'message-in')]"):
        try:
            message = ""
            emojis = []

            message_container = messages.find_element_by_xpath(
                ".//div[@class='copyable-text']")

            message = message_container.find_element_by_xpath(
                ".//span[contains(@class,'selectable-text invisible-space copyable-text')]"
            ).text

            for emoji in message_container.find_elements_by_xpath(
                    ".//img[contains(@class,'selectable-text invisible-space copyable-text')]"
            ):
                emojis.append(emoji.get_attribute("data-plain-text"))

        except NoSuchElementException:  # In case there are only emojis in the message
            try:
                message = ""
                emojis = []
                message_container = messages.find_element_by_xpath(
                    ".//div[@class='copyable-text']")

                for emoji in message_container.find_elements_by_xpath(
                        ".//img[contains(@class,'selectable-text invisible-space copyable-text')]"
                ):
                    emojis.append(emoji.get_attribute("data-plain-text"))
            except NoSuchElementException:
                pass

    return message, emojis


def wait_for_loading(driver):
    loaded = False
    while not loaded:
        try:
            driver.find_element_by_xpath('//div[text() = "Suchen oder neuen Chat beginnen"]/parent::div/descendant::div[@contenteditable="true"]')
            loaded = True
        except:
            loaded = False


def read_messages_since(driver, username, count):
    driver.execute_script("window.scrollBy(0,{})".format(count))

def main():
    """
    Loading all the configuration and opening the website
    (Browser profile where whatsapp web is already scanned)
    """
    settings = load_settings()
    driver = load_driver(settings)
    driver.get(settings['page'])
    wait_for_loading(driver)
    print("website loaded")

    #do something here:
    open_chat(driver, "Meine Gruppe")
    read_messages_since(driver, "Meine Gruppe", -900)
    #print(read_last_in_message(driver))

main()