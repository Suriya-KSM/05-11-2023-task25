from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from time import sleep
import pytest
from Data import data
from Locators import locators

class Test_IMDB:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()

    def test_IMDB(self, booting_function):
        self.driver.maximize_window()
        self.driver.get(data.Data().url)
        self.driver.execute_script("window.scrollBy(0,500);")
        wait = WebDriverWait(self.driver, 20)
        expand_all = wait.until(EC.element_to_be_clickable((By.XPATH, locators.Locators().expand)))
        expand_all.click()
        sleep(5)
        Name_ = wait.until(EC.element_to_be_clickable((By.XPATH,locators.Locators().name_box)))
        Name_.send_keys(data.Data().NAME)
        dob_ = wait.until(EC.element_to_be_clickable((By.XPATH,locators.Locators().DOB_box)))
        dob_.send_keys(data.Data().DOB)
        results = wait.until(EC.element_to_be_clickable((By.XPATH,locators.Locators().see_results)))
        results.click()
        present_url = data.Data().after_search
        assert self.driver.current_url == present_url
        print("Success")
