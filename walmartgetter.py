from selenium import webdriver

import time
import datetime as dt
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

postal_code = ""    #enter your postal code
interval_set = 30   #run script in every # minutes
multi_times = 336     #how many times you want to run it
isheadless = True  #True = Headless   False = Browser Visible
isvpn = False  #True = vpn is on, False = vpn is off

from selenium.common.exceptions import NoSuchElementException


def gowalmart():
    if isheadless == True:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Last I checked this was necessary
        driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options=options)
    else:
        driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
    original_size = driver.get_window_size()
    urllink = "https://www.walmart.ca/en/scheduled-shopping/pickup"
    print("Going to Walmart")
    driver.get(urllink)
    time.sleep(20)
    try:
        enterpc = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[3]/div[5]/div/div[1]/div/form/input[1]")
    except NoSuchElementException:
        time.sleep(10)
        print("Cannot find first element, try again")
        driver.quit()
        return

    enterpc.clear()
    enterpc.send_keys(postal_code)
    time.sleep(20)
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[3]/div[5]/div/div[1]/div/form/input[2]").click()
    #naviga()
    time.sleep(30)
    if isvpn == False:
        
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[3]/div[5]/div/div[3]/div[1]/div/div[1]/div[1]/div[2]/div[2]/button").click()

        time.sleep(30)

        driver.find_element_by_id("next-slots").send_keys(Keys.NULL)

        required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        required_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        driver.set_window_size(required_width, required_height)
        driver.execute_script("document.body.style.zoom = '80%'")

    print("Typed Address")
    screenname = "m" + str(dt.datetime.now().month) + "d" + str(dt.datetime.now().day) + "h" + str(
    dt.datetime.now().hour) + "m" + str(dt.datetime.now().minute)
    driver.save_screenshot("screenshot at " + screenname + " p1.png")

    try:
        slot2 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[3]/div[5]/div/div[7]/div[1]/div/div/button[2]/div")
    except NoSuchElementException:
        print("Cannot find first element, try again")
        driver.quit()
        return
    driver.execute_script("arguments[0].click();", slot2)
    #slot2.click()
    time.sleep(30)
    driver.save_screenshot("screenshot at " + screenname + " p2.png")
    try:
        slot3 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[3]/div[5]/div/div[7]/div[1]/div/div/button[2]/div")
    except NoSuchElementException:
        print("Cannot find first element, try again")
        driver.quit()
        return
    driver.execute_script("arguments[0].click();", slot3)
    #slot3.click()
    time.sleep(30)
    driver.save_screenshot("screenshot at " + screenname + " p3.png")
    
    
    
    driver.set_window_size(original_size['width'], original_size['height'])

    driver.quit()
    print("done cycle:  " + screenname)



counter  = 0

while counter < multi_times:
    gowalmart()
    time.sleep(60*interval_set)
    counter += 1
