from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://login.live.com/')
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="i0116"]').send_keys('E-MAIL')
navegador.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="i0118"]').send_keys('SENHA')
navegador.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
input('')