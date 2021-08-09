import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector('#treasure')
    x = float(x_element.get_attribute('valuex'))
    y = calc(x)
    input1 = browser.find_element_by_css_selector('#answer')
    input1.send_keys(y)

    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    radiobutton.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
except Exception as error:
	print(f'--Error {error}')
finally:
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла, т.к. системы UNIX/Linux ожидают пустую строку в конце файла, если в вашем скрипте ее не будет, то последняя строчка, содержащая код, может не выполниться.