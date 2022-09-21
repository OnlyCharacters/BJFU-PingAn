from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException, NoSuchElementException, ElementClickInterceptedException
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

driver.get("https://x.bjfu.edu.cn/tp_up/view?m=bjfu#act=question/question")

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
# try:
#     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ul_workhall_svsdd"]/li[1]/div[1]/img')))
# except TimeoutException:
#     driver.quit()
# else:
#     driver.find_element(by="xpath", value='//*[@id="ul_workhall_svsdd"]/li[1]/div[1]/img').click()
#     windows = driver.window_handles
#     driver.switch_to.window(windows[-1])

# 提交
try:
    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="question_btn_query"]')))
except TimeoutException:
    print("TimeoutException")
    driver.quit()
except UnexpectedAlertPresentException:
    print("UnexpectedAlertPresentException")
    driver.quit()
except NoSuchElementException:
    if EC.text_to_be_present_in_element((By.XPATH, '//*[@id="layui-layer1"]/div[2]'), "今日已报平安！"):
        print("今日已报平安")
    else:
        print("NoSuchElementException")
    driver.quit()
except ElementClickInterceptedException:
    print("今日已报平安")
    driver.quit()
else:
    time.sleep(1)
    driver.find_element(by="xpath", value='//*[@id="question_btn_query"]').click()
    driver.quit()