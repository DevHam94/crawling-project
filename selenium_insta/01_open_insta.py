from selenium import webdriver
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3) # 에러가 덜나게 3초를 기다려준다.


url = "https://www.instagram.com/"
driver.get(url=url)
xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'
# time.sleep(20)      # 바로 꺼지는걸 방지