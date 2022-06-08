from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math

def calc():
    return str(math.log(abs(12*math.sin(int(x)))))
    
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    button = browser.find_element(By.ID, "book")

    browser.execute_script("arguments[0].scrollIntoView();", button)
    
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )
    button.click()

    number = browser.find_element_by_id("input_value")
    x = number.text

    magic_number = calc()

    #промежуточний етап для перевірки роботи формули
    print(magic_number)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(magic_number)

    browser.execute_script("arguments[0].scrollIntoView();", answer)
    
    submit = browser.find_element_by_id("solve")
    submit.click()
    
finally:
    time.sleep(10)
    browser.quit()
    
