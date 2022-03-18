from selenium import webdriver
import time
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import urllib.parse
import xlsxwriter

class Vegetables(unittest.TestCase):

    @staticmethod
    def test_getdata():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()

        driver.get("https://gourmetgarden.in/")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@class="modal__store-pick-links"]/a[1]').click()       #chennai loction
        driver.find_element_by_xpath('//*[@class="menu"]/li[1]').click()                                 #vegs
        #product_name = driver.find_elements_by_xpath('//*[@class=""hot-pick__title-link-alt""]/h2')
        #product_price = driver.find_elements_by_xpath('//*[@class=""my-auto""]')     #//*[@class=""hot-pick__price""]
        product = driver.find_elements_by_xpath('//*[@class="hot-pick-product splide__slide js-collection-hover"]')

        (len(product))

        df_veg = pd.DataFrame(columns=['Product'])


        for i in range(len(product)):
            df_veg = df_veg.append({'Product Name':product[i].text}, ignore_index=True)

        df_veg.to_excel('23fruits.xlsx', index=False)





if __name__ == '__main__':
    unittest.main()

#chennai = //*[@class=""modal__store-pick-links""]/a[2]"