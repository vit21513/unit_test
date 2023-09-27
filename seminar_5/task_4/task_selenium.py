from selenium import webdriver
import unittest
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import By
class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Edge(service=Service(executable_path="msedgedriver.exe"))
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://www.google.com')
        elem = self.browser.find_element(By.NAME,'q')
        elem.send_keys('Selenium')
        elem.send_keys(Keys.RETURN)
        # self.assertIn('Google', self.browser.title)
        self.assertIn('https://www.selenium.dev',self.browser.find_element(By.XPATH,'/html/body').text)
    def tearDown(self) -> None:
        self.browser.close()