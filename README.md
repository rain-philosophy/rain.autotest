## rain.autotest
Stepik's autotest course hw by Rain
___
##### about chrome driver:
> ChromeDriver is a powerful tool, and it can cause harms in the wrong hands. While using ChromeDriver, please follow these suggestions to help keeping it safe:

> > By default, ChromeDriver only allows local connections. If you need to connect to it from a remote host, use --allowed-ips switch on the command line to specify a list of IP addresses that are allowed to connect to ChromeDriver.

> > If possible, run ChromeDriver with a test account that has no access to sensitive local or network data. ChromeDriver should never be run with a privileged account.

> >  If possible, run ChromeDriver in a protected environment such as Docker or virtual machine.

> > Use firewall to prevent unauthorized remote connection to ChromeDriver.

> > If you are using ChromeDriver through third-party tools such as Selenium Server, be sure to protect the network ports of those tools as well.

> > Use the latest versions of ChromeDriver and Chrome.
___
##### code features:
###### auto exit from chrome | try-except-finally
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit")
    button.click()
except Exception as error:
	print(f'--Error {error}')
finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла, т.к. системы UNIX/Linux ожидают пустую строку в конце файла, 
# если в вашем скрипте ее не будет, то последняя строчка, содержащая код, может не выполниться.
```
###### auto exit from chrome | with-as
```python
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    button = browser.find_element(By.ID, "submit")
    button.click()

# не забываем оставить пустую строку в конце файла, т.к. системы UNIX/Linux ожидают пустую строку в конце файла, 
# если в вашем скрипте ее не будет, то последняя строчка, содержащая код, может не выполниться.
```
###### assert
```python
# проверяем, что количество товаров равно 2
assert len(goods) == 2, 'smth wrong'

message = browser.find_element_by_id("verify_message")
assert "successful" in message.text

assert "login" in browser.current_url, # сообщение об ошибке

catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную,чтобы не брать два раза
assert catalog_text == "Каталог", \
    f"Wrong language, got {catalog_text} instead of 'Каталог'"  
```
###### get_atribute
```python
# http://suninjuly.github.io/math.html
# <input class="check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>

people_radio = browser.find_element_by_id("peopleRule")
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)

assert people_checked is not None, "People radio is not selected by default"
# Т.к. у данного атрибута значение не указано явно, то метод get_attribute вернёт "true". Возможно, вы заметили, 
# что "true" написано с маленькой буквы, — все методы WebDriver взаимодействуют с браузером с помощью JavaScript, 
# в котором булевые значения пишутся с маленькой буквы, а не с большой, как в Python.

# Мы можем написать проверку другим способом, сравнив строки:
assert people_checked == "true", "People radio is not selected by default"

robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None
# Так же мы можем проверять наличие атрибута disabled, который определяет, может ли пользователь взаимодействовать 
# с элементом. 
```
###### select - работа со списками
```python
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1") # ищем элемент с текстом "Python"
# Можно использовать еще два метода: select.select_by_visible_text("text") и select.select_by_index(index). 
```
###### execute_script - выполнение JavaScript через selenium
```python
from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("document.title='Script executing';alert('Robots at work');")
```
###### send file from directory
```python
import os 

current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')        # добавляем к этому пути имя файла 
element.send_keys(file_path)
```
###### alert
```python
# принять алерт
alert = browser.switch_to.alert
alert.accept()

# взять текст алерта
alert = browser.switch_to.alert
alert_text = alert.text

# конфирм - сообщение с выбором отмены
confirm = browser.switch_to.alert
confirm.accept()
confirm.dismiss()

# промт - сообщение с полем ответа
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()
```
###### windows
```python
browser.switch_to.window(window_name)
new_window = browser.window_handles[1]
```
###### waits | implicit wait
```python
# неявное ожидание (Implicit wait) - говорим WebDriver искать каждый элемент в течение 5 секунд
# Таким образом, мы сможем получить нужный элемент в идеальном случае сразу, в худшем случае за 5 секунд.
browser = webdriver.Chrome()
browser.implicitly_wait(5)
```
> Если произойдет ошибка, то WebDriver выбросит одно из следующих исключений (exceptions):
> * Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.
> * Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился, то получим StaleElementReferenceException. Например, мы нашли элемент Кнопка и через какое-то время решили выполнить с ним уже известный нам метод click. Если кнопка за это время была скрыта скриптом, то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение.
> * Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры), и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.
###### waits | explicit wait
```python
# явное ожидание (Explicit Waits)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait2.html")
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
        )
button.click()
message = browser.find_element_by_id("verify_message")
assert "successful" in message.text

'''
В модуле expected_conditions есть много других правил, которые позволяют реализовать необходимые ожидания 
((By.ID, 'селектор'),'значение'))
title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
'''

# Если мы захотим проверять, что кнопка становится неактивной после отправки данных, то можно задать негативное 
# правило с помощью метода until_not: говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
        )
```
###### pageLoadStrategy
```python
# none (не определено)
# eager (страница становится интерактивной)
# normal (полная загрузка страницы)

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

link = "example.com"
caps = DesiredCapabilities.CHROME
browser = webdriver.Chrome(desired_capabilities=caps)
caps['pageLoadStrategy'] = 'none' # Do not wait for full page load
```
___
##### --help
[форматирование readme](https://github.com/GnuriaN/format-README#%D0%9E%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)       
[... что такое переменная PATH?](http://barancev.github.io/what-is-path-env-var/)        
[отучаемся от токсичных code-review](https://habr.com/ru/post/453968/)      
[youtube: if __name __ == '__main__': что это значит](https://www.youtube.com/watch?v=cW_-zGG4ef4)      
###### css:
[тренажер по css-селекторам](https://flukeout.github.io/)      
[css-селекторы](https://developer.mozilla.org/ru/docs/Web/CSS/CSS_Selectors)       
[css sselector reference](https://www.w3schools.com/cssref/css_selectors.asp)       
[статья на хабре: Селекторы CSS и их применение в автоматизации тестирования Программного Обеспечения](https://habr.com/ru/company/otus/blog/350368/)       
[... как строить хорошие локаторы?](http://barancev.github.io/good-locators/)        
###### selenium:
[атрибуты html](https://www.w3schools.com/tags/ref_attributes.asp)         
[пояснение за expected_conditions для explicit wait](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions)       
[... ограничение времени загрузки страницы](http://barancev.github.io/slow-loading-pages/)      
[... что означает "окончание загрузки страницы"?](http://barancev.github.io/page-loading-complete/)       
[How to Get Selenium to Wait for Page Load After a Click](https://www.cloudbees.com/blog/get-selenium-to-wait-for-page-load)       
###### git:
[тренажер по git](https://learngitbranching.js.org/)        
[книга по git](https://git-scm.com/book/ru/v2/)     
[еще одна книга по git](http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/ru/index.html)        
[git для даунов на примере котиков](https://habr.com/ru/company/intel/blog/344962/)        
[еще один тренажер по git](https://githowto.com/ru)     
