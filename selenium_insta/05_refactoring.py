from selenium import webdriver
import chromedriver_autoinstaller
import time
import os

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(13) # 에러가 덜나게 3초를 기다려준다.


url = "https://www.instagram.com/"
driver.get(url=url)

def login(id, password):
    input_id = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    input_id.send_keys(id)
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    # driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)

def search(hashtag, scroll_times):
    url = f"https://www.instagram.com/explore/tags/{hashtag}/"
    driver.get(url=url)
    time.sleep(6)

    for _ in range(scroll_times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(7)

def like_comment(nth, comment, repeat=3):
    row = (nth - 1) // 3 + 1
    col = 0
    # nth 포스트 클릭
    xpath = f'/html/body/div[i]/div/div/div[1]/div/div/div/div[1]/div[1]/section/main/article/div[2]/div/div[{row}]/div[{col}'
    driver.find_element(By.XPATH, xpath).click()

    for _ in range(repeat):
        # like
        like_xpath = '/html/body/div[1]/div/div/div/div[2]/div/article/div/div[3]/div/div/section[1]/span[1]/button'
        driver.find_element(By.XPATH, like_xpath).click()

        # comment
        comment_xpath = ''
        driver.find_element(By.XPATH, comment_xpath).click()
        driver.find_element(By.XPATH, comment_xpath).send_keys(comment)
        # 게시 버튼 누르기
        comment_button_xpath = ''
        driver.find_element(By.XPATH, comment_xpath).click()

        # 다음 게시물
        next_button_xpath = ''
        driver.find_element(By.XPATH, next_button_xpath)

id = os.getenv("INSTA_ID")
password = os.getenv("INSTA_PW")

login(id, password)

time.sleep(5)

# search
hashtag = "강아지"
search(hashtag, 1)

# like comment
like_comment(13, "강아지가 귀엽네요", 2)

time.sleep(20)
