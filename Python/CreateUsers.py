from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import xlrd

x = 0
y = 0 
title = ''
para = ''
div = ''
website = ""http://www.exapmle.com""

class User:

    def __init__(self, first, last, mid, usern, passw, month, day, year, zipc, city, cntry, email):
        self.first = first
        self.last = last
        self.mid = mid
        self.usern = usern
        self.passw =  passw            
        self.month = month
        self.day = day
        self.year = year
        self.zipc = zipc
        self.city = city
        self.cntry = cntry
        self.email = email     
                
    def dob(self):
        return '{} {} {}'.format(self.day, self.month, self.year)
        
      

def getHTMLdata(title, para, div)

    driver = webdriver.Firefox()
    driver.get(website)

    elem = driver.find_element_by_tag_name('p')

    driver.close()
    
    

def getLastNames(x, y):

    namesList = []

    x = 0
    y = 0

    lnamesbook = namesbook.sheet_by_name('lastNames')
    lname = namesbook.cell(x, y).value

        

    








    

 