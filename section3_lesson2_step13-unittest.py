from selenium import webdriver
import time
import unittest

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        elements = ['.first_block .first','.first_block .second','.first_block .third'] 
        for it in elements:
            browser.find_element_by_css_selector(it).send_keys("rain")
        # self.assertEqual(len(elements),3, "Should be three spaces for data")

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
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text, "No congrads")        
    
    def test_registration2(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        elements = ['.first_block .first','.first_block .second','.first_block .third'] 
        for it in elements:
            browser.find_element_by_css_selector(it).send_keys("rain")

        # self.assertEqual(len(elements),3, "Should be three spaces for data")

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
        self.assertEqual("Congratulations! You have successfully registered!",welcome_text, "No congrads")
        
if __name__ == "__main__":
    unittest.main()
