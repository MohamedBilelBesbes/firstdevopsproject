from selenium import webdriver as wb
import time
import requests
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
import unittest

class FrontTest(unittest.TestCase):
    def testindexform(self):
        options = Options()
        options.add_argument("--headless")
        #self.wbD = wb.Chrome("C:\\Users\\bilel\\Desktop\\ovice\\devops_project\\monoprix\\DevOps\\static\\chromedriver.exe",chrome_options=options)
        self.wbD = wb.Firefox(executable_path="./geckodriver",options=options)
        self.wbD.get("http://127.0.0.1:5000")
        wbD = self.wbD
        #shop_id
        wbD.find_element_by_xpath('//*[@id="input1"]').send_keys('1')
        #item_id
        wbD.find_element_by_xpath('//*[@id="input2"]').send_keys('283400170')
        #price
        wbD.find_element_by_xpath('//*[@id="input47"]').send_keys('3.5')
        #starting_price
        wbD.find_element_by_xpath('//*[@id="input5"]').send_keys('2019-04')
        #period
        wbD.find_element_by_xpath('//*[@id="input6"]').send_keys('4')
        time.sleep(1)
        wbD.find_element_by_xpath('/html/body/form/input').click()
        url = requests.get(wbD.current_url)
        assert url.status_code == 200
        wbD.close()


if __name__ == "__main__":
    unittest.main()
