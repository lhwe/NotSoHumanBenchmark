import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://humanbenchmark.com/tests/typing')

try:
    letters_element = driver.find_element(By.CLASS_NAME, 'letters')
    words = [word if word else ' ' for word in letters_element.text.split()]
    compiled_text = ' '.join(words)
    print(f'Found element, typing...')
    pyautogui.typewrite(compiled_text)
except Exception as e:
    print("Error:", e)
pyautogui.sleep(5)
driver.quit()
