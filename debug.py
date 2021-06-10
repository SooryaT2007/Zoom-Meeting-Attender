from selenium import webdriver

PATH=(r"C:\Users\DELL\OneDrive\Python\Chrome Driver\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(PATH)
driver.get("http://www.zoom.us")