# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
 
# open Chrome
driver = webdriver.Chrome('D:/Programmazione/python/Compilatore Automatico form/chromedriver.exe')
 
# Open URL
driver.get('https://docs.google.com/forms/d/e/1FAIpQLScX90-iP1tYTY9vYSki85-3sBQCZo0c2QU5xKPWNJLu8qaTyg/viewform?usp=sf_link')
 
# wait for one second, until page gets fully loaded
time.sleep(1)
 
# Data
datas = [
    ['Lorenzo Cipriani', 'Rome', 'ROM-BON La casa de Papel',
        'C. Series One Touchpanel, Mic Pods, and Soundbar', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'All good, there were no issues.', 'ALL GOOD'],
    ['Lorenzo Cipriani', 'Rome', 'ROM-BON Stranger things',
        'C. Series One Touchpanel, Mic Pods, and Soundbar', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'All good, there were no issues.', 'ALL GOOD'],
    ['Lorenzo Cipriani', 'Rome', 'ROM-BON Suburra',
        'C. Series One Touchpanel, Mic Pods, and Soundbar', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'All good, there were no issues.', 'ALL GOOD'],
    ['Lorenzo Cipriani', 'Rome', 'ROM-BON Fedeltà',
        'C. Series One Touchpanel, Mic Pods, and Soundbar', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'All good, there were no issues.', 'ALL GOOD'],
]
 
# Iterate through each data
for data in datas:
    # Initialize count is zero
    count = 0
 
    # contain input boxes
    textboxes = driver.find_elements(By.CLASS_NAME, "whsOnd")

    # contain multiple answer
    radiobuttons = driver.find_element(By.CLASS_NAME, "rseUEf")
    select_radio = Select(radiobuttons)

 
    # contain textareas
    textareaboxes = driver.find_elements_by_class_name(
        "quantumWizTextinputPapertextareaInput")
 
    # Iterate through all input boxes
    for value in textboxes:
        # enter value
        value.send_keys(data[count])
        # increment count value
        count += 1

    select_radio.select_by_visible_text('Rome')


    # Iterate through all textareas
    for value in textareaboxes:
        # enter value
        value.send_keys(data[count])
        # increment count value
        count += 1
 
    # click on submit button
    submit = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()
 
    # fill another response
    another_response = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
 
# close the window
driver.close()