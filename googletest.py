from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

#變數調整區
#要買的演唱會後綴URL
xpathurl ="activity/game/25_casty"

# 防止跳出通知
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
prefs = {
    "profile.default_content_setting_values.notifications": 2
}
chrome_options.add_experimental_option("prefs", prefs)

#開啟cookie
with open('D:\cookie_jar.json') as f:
    cookies = json.load(f)
url = "https://tixcraft.com/"
driver = webdriver.Chrome(options=chrome_options)
# 最大化視窗
driver.maximize_window()
# 進入目標登入畫面
driver.get(url)

#打開登入
driver.implicitly_wait(3)

#直接跳至目標網頁的購買 detail->game
url = url + xpathurl
driver.get(url)
#關閉coolie設定視窗
driver.find_element(By.XPATH,'//button[@id="onetrust-reject-all-handler"]').click()

#訂票
driver.execute_script("Window.scrollTO(0,800)")
time.sleep(4)
driver.find_element(By.XPATH,'//button[@class="btn btn-primary text-bold m-0"]').click()
#依照項目自動電腦選票 gameID該項目流水號資訊
gameID = driver.find_element(By.ID,"gameId")
#資照區域排序 1之後會改變去for迴圈查有哪些剩餘
IDValue = gameID.get_attribute('value') +'_' + '1'
dt = driver.find_element(By.ID,IDValue).text
print(dt)
#區域位置迴圈查詢哪邊有剩餘座位
seatcount ='abcdefghijklmnopqrstuvwxyz'
if "剩餘" or "熱賣" in dt:
    for x in seatcount:
        elename = "select_form_" + x
        print(elename)
        if driver.find_element(By.CLASS_NAME,elename):
            driver.find_element(By.CLASS_NAME,elename).click()
            break
        else:
            continue
#買一張    
#driver.find_element(By.ID,"TicketForm_ticketPrice_02").send_keys(1)
driver.find_element(By.XPATH,'//*[contains(@id, "TicketForm_ticketPrice")]').send_keys(1)
#同意書
driver.find_element(By.XPATH,'//input[@id="TicketForm_agree"]').click()
#7秒內需輸入完驗證碼
time.sleep(7)
#確認張數下訂 
driver.execute_script("Window.scrollTO(0,1600)")
driver.find_element(By.XPATH,'//button[@class="btn btn-primary btn-green"]').click()
#選虛擬ATM
driver.find_element(By.XPATH,'//input[@id="CheckoutForm_paymentId_54"]').click()
#同意規則下一步
#driver.find_element(By.XPATH,'//button[@class="btn btn-primary btn-lg text-bold btn-green"]').click()