import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = int(browser.find_element_by_css_selector('#num1').text)
    y = int(browser.find_element_by_css_selector('#num2').text)
    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(f'{x+y}')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
except Exception as error:
	print(f'--Error {error}')
finally:
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла, т.к. системы UNIX/Linux ожидают пустую строку в конце файла, если в вашем скрипте ее не будет, то последняя строчка, содержащая код, может не выполниться.