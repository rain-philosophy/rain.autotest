from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	elements = browser.find_elements_by_css_selector('.form-control')
	for it in elements:
		it.send_keys('rain')

	element = browser.find_element_by_css_selector("#file")
	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
	element.send_keys(file_path)

	button = browser.find_element_by_tag_name("button")
	button.click()
except Exception as error:
	print(f'--Error {error}')
finally:
	time.sleep(10)
    # закрываем браузер после всех манипуляций
	browser.quit()

# не забываем оставить пустую строку в конце файла, т.к. системы UNIX/Linux ожидают пустую строку в конце файла, если в вашем скрипте ее не будет, то последняя строчка, содержащая код, может не выполниться.