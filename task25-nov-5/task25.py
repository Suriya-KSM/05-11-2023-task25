from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from time import sleep

class KSM:
    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        

    def login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            self.driver.execute_script("window.scrollBy(0,500);")
            sleep(3)
            wait = WebDriverWait(self.driver, 20)
            expand_all = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button/span')))
            expand_all.click()
            sleep(5)
            birth_date_button1 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#text-input__7')))
            birth_date_button1.send_keys("01")
            sleep(3)

        
        except NoSuchElementException as selenium_error:
            print(selenium_error)
        
        except TimeoutException as a:
            print("Timeout Exception", a)

        finally:
            self.driver.quit()
            


URL="https://www.imdb.com/search/name/"
Obj = KSM(URL)
Obj.login()
