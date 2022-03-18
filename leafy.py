from selenium import webdriver
import time
import unittest
import Utilities as U
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import urllib.parse
import xlsxwriter
from selenium.common.exceptions import NoSuchElementException


class Vegetables(unittest.TestCase):

    @staticmethod
    def test_getdata():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()

        driver.get("https://gourmetgarden.in/")
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@class="modal__store-pick-links"]/a[2]').click()       #chennai loction
        driver.find_element_by_xpath('//*[@class="menu"]/li[3]').click()                                 #vegs
        product_Name = driver.find_elements_by_xpath('//*[@class="hot-pick__title"]')
        product_price = driver.find_elements_by_xpath('//*[@class="hot-pick__price"]')
        #product_Regular_price = driver.find_elements_by_xpath('//*[@class=""product__price--reg js-price""]')              #('//*[@class=""hot-pick__price""]/span[2]')
        #product_Spcl_price = driver.find_elements_by_xpath('//*[@class=""hot-pick__price""]/span[3]')
        product = driver.find_elements_by_xpath('//*[@class="product__form--add-to-cart"]')                               #('//*[@class=""hot-pick-product splide__slide js-collection-hover""]')



        (len(product))
        log_file = "D:\\New folder\\Gourmet-26dec.log"

        for i in range(len(product)):
            #U.log("INFO", [product_Name[i].text , product_price[i].text] , log_file)
            U.log("INFO",( product[i].text ), log_file)


if __name__ == '__main__':
    unittest.main()

#chennai = //*[@class=""modal__store-pick-links""]/a[2]"