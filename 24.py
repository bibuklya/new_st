from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser.implicitly_wait(13)
    text = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    button = browser.find_element(By.ID, "book")
    button.click()
    
    #message = browser.find_element(By.ID, "verify_message")

    #assert "successful" in message.text
    x = browser.find_element(By.ID, "input_value").text
    #x = x_element.get_attribute("valuex")
    y = calc(x)
    field_y = browser.find_element(By.CSS_SELECTOR, "#answer")
    field_y.send_keys(y)


    button = browser.find_element(By.ID, "solve")
    button.click()

    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()