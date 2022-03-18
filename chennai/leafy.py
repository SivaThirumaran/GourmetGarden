from selenium import webdriver
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

class Vegetables(unittest.TestCase):

    @staticmethod
    def test_getdata():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()

        driver.get("https://gourmetgarden.in/")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@class="modal__store-pick-links"]/a[2]').click()       #chennai loction
        driver.find_element_by_xpath('//*[@class="menu"]/li[5]').click()
        product = driver.find_elements_by_xpath('//*[@class="product__form--add-to-cart"]')

        (len(product))

        df_veg = pd.DataFrame()


        for i in range(len(product)):
            df_veg = df_veg.append({'Product Name':product[i].text}, ignore_index=True)

        df_veg.to_excel('21febleafy.xlsx', index=False)





if __name__ == '__main__':
    unittest.main()

