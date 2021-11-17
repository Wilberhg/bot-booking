from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class BookingReport:
    def __init__(self, deal_boxes:WebElement):
        self.deal_boxes = deal_boxes

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            hotel_name = deal_box.find_element(By.CSS_SELECTOR,
                'div[data-testid="title"]'
            ).get_attribute('innerHTML').strip()
            
            hotel_price = deal_box.find_element(
                By.CSS_SELECTOR, 
                'div[data-testid="price-and-discounted-price"]'
            ).find_elements(By.TAG_NAME, 'span')[-1].text.strip()
            
            try:
                hotel_score = deal_box.find_element(By.CSS_SELECTOR,
                    'div[data-testid="review-score"]'
                ).find_element(By.TAG_NAME, 'div').get_attribute('innerHTML').strip()
            except:
                hotel_score = 'N/A'

            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )
        
        return collection