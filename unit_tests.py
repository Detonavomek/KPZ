#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import unittest, os
from BeautifulSoup import BeautifulSoup
os.chdir('.')
from selenium import selenium, webdriver
from selenium.webdriver.common.keys import Keys
os.chdir(os.path.dirname(os.path.realpath(__file__)))
import orm_functions as Controler

class OrmFunctionTests(unittest.TestCase):
    def testCourtTRUE(self):
    	courtName = 'Court 2u'
    	Controler.AddCourt(courtName)
    	cc = filter(lambda X: X.name == courtName, Controler.GetCourts())
    	self.failUnless(bool(len(cc)))

    def testCourtFALSE(self):
    	courtName = 222
    	Controler.AddCourt(courtName)
    	cc = filter(lambda X: X.name == courtName, Controler.GetCourts())
        self.failIf(bool(len(cc)))

    def testForm(self):
    	driver = webdriver.Firefox()
    	driver.get("localhost:8082/court")
    	self.failUnless(driver.find_element_by_id('buttonAdd').get_attribute('value') == 'Add')
    	driver.close()

unittest.main()