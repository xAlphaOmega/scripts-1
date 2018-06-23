# -*- coding=utf-8 -*-
from __future__ import print_function
 
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
 
class DL(object):
    "Selenium Firefox browser representation."
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        self.webdriver = webdriver.Firefox(firefox_options=options,
                executable_path=os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    "geckodriver"
                    )
            )
 
    def get(self, webpage):
        return self.webdriver.get(webpage)
 
    def search(self):
        return self.webdriver.find_element_by_id('videoPlayer')
 
    def __del__(self):
        self.webdriver.close()
 
if __name__ == "__main__":
    pelda = DL()
    pelda.get("https://nava.hu/id/3187894")
    print(pelda.search())
