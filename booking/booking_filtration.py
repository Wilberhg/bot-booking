from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BookingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, '*')
        # star_child_elements = [element for element in star_child_elements if element]
        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('data-filters-item')).strip() == (f'class:class={star_value}' or f'{star_value} estrela'):
                    star_element.click()
        
    def sort_price_lowest_first(self):
        element = self.driver.find_element_by_css_selector(
            'li[data-id="price"]'
        )
        element.click()