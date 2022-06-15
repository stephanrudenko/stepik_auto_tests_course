import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

def answer():
   return str(math.log(int(time.time())))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('magic_links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestAnswers():
    def test_guest_should_sent_correct_answer(self, browser, magic_links):
        link = f"https://stepik.org/lesson/{magic_links}/step/1"
        browser.get(link)
        
        browser.implicitly_wait(10)

        text_area = browser.find_element(By.CSS_SELECTOR, ".textarea")  
        text_area.click()

        time = answer()
        
        text_area.send_keys(time)
        
        button = WebDriverWait(browser, 12).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
            )
        button.click()

        message = WebDriverWait(browser, 12).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "pre.smart-hints__hint"))).text
            
        assert message == "Correct!", print(f"{magic_links}" + " " + message)
        
if __name__ == "__main__":
    pytest.main()


        
