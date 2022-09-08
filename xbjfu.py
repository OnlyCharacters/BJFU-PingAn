from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
import time

# 输入你的账号密码
username_u = ""
password_u = ""

opt = webdriver.ChromeOptions()
opt.add_argument("headless")
opt.add_argument("no-sandbox")
opt.add_argument("disable-gpu")
driver = webdriver.Chrome(options=opt)

driver.get("https://cas.bjfu.edu.cn/")

# 输入账号密码和登录
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="un"]')))
except TimeoutException:
    driver.quit()
else:
    username = driver.find_element(by="xpath", value='//*[@id="un"]')
    password = driver.find_element(by="xpath", value='//*[@id="pd"]')
    ActionChains(driver).send_keys_to_element(username, username_u).perform()
    ActionChains(driver).send_keys_to_element(password, password_u).perform()
    driver.find_element(by="xpath", value='//*[@id="index_login_btn"]/input').click()

# 进入报平安表格
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ul_workhall_svsdd"]/li[1]/div[1]/img')))
except TimeoutException:
    driver.quit()
else:
    driver.find_element(by="xpath", value='//*[@id="ul_workhall_svsdd"]/li[1]/div[1]/img').click()
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])

# 提交
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body_0"]/div[1]/div[2]/div[4]/span')))
except TimeoutException:
    driver.quit()
except UnexpectedAlertPresentException:
    driver.quit()
else:
    driver.find_element(by="xpath", value='//*[@id="commit"]').click()
    time.sleep(2)
    driver.quit()