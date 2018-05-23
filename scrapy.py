import time
from selenium import webdriver
from settings import CHROME_DRIVER_LOCATION, BASE_URL

SELECT_QUERY_SELECTOR = '.ControlGroup .Select'
SELECT_WINDOW_QUERY_SELECTOR = '.Popup_visible'
SELECT_OPTION_QUERY_SELECTOR = '.Menu .MenuItem:not(.MenuItem_has-clear)'

class Scrapy:
    def __init__(self):
        self._driver = webdriver.Chrome(CHROME_DRIVER_LOCATION)
        self.result = {}

    def run(self):
        self._driver.get(BASE_URL)
        self._scrap()
        self._driver.close()

    def _scrap(self):
        i = 0
        while True:
            self._click_on_brands_select()   
            brand_el = self._get_brand_element(i)  
            if brand_el is None:
                break            
            brand_name = brand_el.get_attribute('textContent')   
            brand_el.click()      

            self._click_on_models_select()
            self.result[brand_name] = self._get_models()          

            i += 1

    def _click_on_brands_select(self):
        self._driver.find_element_by_css_selector(SELECT_QUERY_SELECTOR).click()     
    
    def _get_brand_element(self, i):
        brand_elements = self._driver.find_element_by_css_selector(
            SELECT_WINDOW_QUERY_SELECTOR
        ).find_elements_by_css_selector(
            SELECT_OPTION_QUERY_SELECTOR
        )
        if len(brand_elements) > i:
            return brand_elements[i]
        else:
            return None

    def _click_on_models_select(self):
        self._driver.find_elements_by_css_selector(SELECT_QUERY_SELECTOR)[1].click()           

    def _get_models(self, max_tries=5, **kwargs):
        model_elements = self._driver.find_element_by_css_selector(
            SELECT_WINDOW_QUERY_SELECTOR
        ).find_elements_by_css_selector(
            SELECT_OPTION_QUERY_SELECTOR
        )
        try_ = kwargs.get('try_') or 1
        if len(model_elements) > 0:
            return [el.get_attribute('textContent') for el in model_elements]
        elif try_ < max_tries:
            time.sleep(0.5)
            return self._get_models(max_tries, try_=try_ + 1)
        else:
            raise Exception('Could not get models.')
