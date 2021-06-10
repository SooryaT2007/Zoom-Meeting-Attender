from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# For this programe to work you have to download zoom client and log in
# PATH means chromedriver path


MEETING_ID = "84203868615"
PATH=(r"")

# Code starts from here





driver = webdriver.Chrome(PATH)
driver.get("http://www.zoom.us")
time.sleep(2)
join_now = driver.find_element_by_link_text('JOIN A MEETING')
join_now.send_keys(Keys.RETURN)
meeting_id = driver.find_element_by_id("join-confno")
meeting_id.send_keys(MEETING_ID)
time.sleep(10)
submit_btn = driver.find_element_by_id("btnSubmit")
submit_btn.send_keys(Keys.RETURN)
join = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div")
join.send_keys(Keys.RETURN)

