from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
	browser = webdriver.Chrome()
	browser.get(link)

	button = browser.find_element_by_tag_name("button")
	button.click()

	browser.switch_to.window(browser.window_handles[-1])

	x_element = browser.find_element_by_css_selector('#input_value')
	x = x_element.text
	y = calc(x)
	input1 = browser.find_element_by_tag_name('#answer')
	input1.send_keys(y)

	button = browser.find_element_by_tag_name("button")
	button.click()
except Exception as error:
	print(f'--Error {error}')
finally:
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла, т.к. системы UNIX/Linux ожидают пустую строку в конце файла, если в вашем скрипте ее не будет, то последняя строчка, содержащая код, может не выполниться.