from selenium import webdriver
import time
import math

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element_by_css_selector('#input_value')
	x = x_element.text
	y = calc(x)
	input1 = browser.find_element_by_tag_name('#answer')
	input1.send_keys(y)

	checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
	browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
	checkbox.click()
	radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
	browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutton)
	radiobutton.click()

	button = browser.find_element_by_tag_name("button")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()
except Exception as error:
	print(f'--Error {error}')
finally:
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла, т.к. системы UNIX/Linux ожидают пустую строку в конце файла, если в вашем скрипте ее не будет, то последняя строчка, содержащая код, может не выполниться.