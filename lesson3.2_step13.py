from selenium import webdriver
import time
import unittest

class TestRegistration(unittest.TestCase):
    def test_link1(self): 
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
        input1.send_keys("Stepan")
        input2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
        input2.send_keys("Rudenko")
        input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        input3.send_keys("s.rudenko584@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "test failed in 1st link")
        #assert "Congratulations! You have successfully registered!" == welcome_text

    def test_link2(self): 
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("div.first_block > div.form-group.first_class > input")
        input1.send_keys("Stepan")
        input2 = browser.find_element_by_css_selector("div.first_block > div.form-group.second_class > input")
        input2.send_keys("Rudenko")
        input3 = browser.find_element_by_xpath("//input[@placeholder='Input your email']")
        input3.send_keys("s.rudenko584@gmail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "test failed on 2nd link")
        #assert "Congratulations! You have successfully registered!" == welcome_text

if __name__ == "__main__":
    unittest.main()


    


