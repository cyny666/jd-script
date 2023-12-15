import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F')
#让用户扫码登录
time.sleep(15)
driver.get("https://www.jd.com/")
while(True):
    print(datetime.now())
    datetime_str = str(datetime.now())[:-7]
    driver.get("https://cart.jd.com/cart_index")
    if (datetime_str == "2023-12-19 10:00:00"):
        print("开始抢购")
        # 找到商品
        time.sleep(3)
        target = driver.find_element(By.ID,"100077030325")
        checkshop = target.find_element(By.NAME, "checkItem")
        checkshop.click()
        time.sleep(1)
        # 在购物车中找到结算按钮并点击
        checkout_button = driver.find_element(By.CLASS_NAME, "common-submit-btn")
        checkout_button.click()
        time.sleep(1)
        # 找到提交订单按钮并点击
        submit_button = driver.find_element(By.ID, "order-submit")
        submit_button.click()
        time.sleep(10)
        driver.quit()




