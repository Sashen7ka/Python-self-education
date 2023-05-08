from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# создаем экземпляр веб-драйвера Chrome
driver = webdriver.Chrome()

# открываем главную страницу Розетки
driver.get('https://rozetka.com.ua/')

# находим кнопку "Вход" и кликаем на нее
driver.find_element(By.XPATH, '/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[3]/rz-user/button').click()
time.sleep(2)
# находим ссылку "Зарегистрироваться" и кликаем на нее
driver.find_element(By.XPATH, '/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-auth/div/form/fieldset/div[5]/button[2]').click()

# заполняем поля регистрации
first_name_field = driver.find_element(By.CSS_SELECTOR, '#registerUserName')
first_name_field.send_keys('Сашу')
time.sleep(2)

last_name_field = driver.find_element(By.CSS_SELECTOR, '#registerUserSurname')
last_name_field.send_keys('Ля')
time.sleep(2)
phone_field = driver.find_element(By.CSS_SELECTOR, '#registerUserPhone')
phone_field.send_keys('0936543267')

email_field = driver.find_element(By.CSS_SELECTOR, '#registerUserEmail')
email_field.send_keys('eynyw@mailforspam.com')

password_field = driver.find_element(By.CSS_SELECTOR, '#registerUserPassword')
password_field.send_keys('R12345678')
time.sleep(2)
# находим и кликаем на кнопку "Зарегистрироваться"
register_button = driver.find_element(By.XPATH, '/html/body/app-root/rz-single-modal-window/div[3]/div[2]/rz-user-identification/rz-register/div/form/fieldset/div[8]/button[1]').click()
time.sleep(4)
# закрываем браузер после завершения регистрации
driver.quit()
