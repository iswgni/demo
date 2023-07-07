import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Search(unittest.TestCase):
    def setUp(self):
        self.drv = webdriver.Chrome()
        self.drv.get('http://www.google.com')
        assert 'Google' in self.drv.title

    def test_search(self):
        elm = self.drv.find_element(By.NAME, 'q')
        elm.send_keys('selenide')
        elm.send_keys(Keys.RETURN)
        wait = WebDriverWait(self.drv, 100)
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/h3'))).click()
        url = self.drv.current_url
        if 'selenide.org' in url:
            print('Selenide.org - первый результат в поисковой строке')
        self.drv.back()
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="cnt"]/div[5]/div/div/div[1]/div[1]/div/a[1]/div'))).click()
        wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'dmeZbb')))
        elm1 = self.drv.find_element(By.CLASS_NAME, 'dmeZbb').text
        if 'selenide.org' in elm1:
            print('Первая картинка относится к selenide.org')
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[2]/c-wiz/div[1]/div/div[1]/div[1]/div/div/a[1]'))).click()
        wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'apx8Vc tjvcx GvPZzd cHaqb')))
        elm2 = self.drv.find_element(By.CLASS_NAME, 'apx8Vc tjvcx GvPZzd cHaqb').text
        if 'selenide.org' in elm2:
            print('Selenide.org - все еще первый результат в поисковой строке')
        else:
            print(elm2)

    def tearDown(self):
        self.drv.close()


if __name__ == '__main__':
    unittest.main()
