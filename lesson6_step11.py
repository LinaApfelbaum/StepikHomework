from selenium import webdriver
import time

from selenium.webdriver.common.by import By

link = input("Paste required link: ")
browser = webdriver.Chrome()
browser.get(link)

try:
    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first')]")
    first_name.send_keys("Robyn")
    last_name = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last')]")
    last_name.send_keys("Carlsson")
    email = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]")
    email.send_keys("robyn@gmail.se")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
