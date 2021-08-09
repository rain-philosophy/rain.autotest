from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    field1 = browser.find_element_by_xpath("//input[contains(@placeholder, 'first name')]")
    field1.send_keys("Hi 0")
    field2=browser.find_element_by_xpath("//input[contains(@placeholder, 'last name')]")
    field2.send_keys("Hi 1")
    field3 = browser.find_element_by_xpath("//input[contains(@placeholder, 'email')]")
    field3.send_keys("Hi 2")

    ...

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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()