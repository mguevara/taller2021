# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 21:55:33 2021

@author: cristobal
"""


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
import random
import sqlite3 as sql



options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
    
def scrapper():
    driver_path = 'C:\\Users\\cristobal\\Downloads\\chromedriver'
    
    driver = webdriver.Chrome(driver_path, chrome_options=options)
    
    
    driver.set_window_position(2000, 0)
    driver.maximize_window()
    time.sleep(1)
    
    driver.get('https://www.toctoc.com/')
    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                          'button.align-right secondary slidedown-button'.replace(' ', '.'))))\
        .click()
    
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                          'input.form-control')))\
        .send_keys('Valparaíso')
       
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                          'a.btn-busca btn btn-success btn-block'.replace(' ', '.'))))\
        .click()
    
    time.sleep(25)
    df = pd.DataFrame(columns = ['Precio', 'Direccion', 'Region'])
    for i in range (2):
        
            matches = driver.find_elements_by_class_name('un-ress.tp2')
        
            for match in matches:
                UF=match.find_element_by_class_name('precio').text
                UF=UF.split('Desde\nUF')[1]
                direccion=match.find_element_by_class_name('dir').text
                region=match.find_element_by_class_name('region').text
                    
                print(UF)
                print(direccion)
                print(region)
                
                df = df.append({'Precio' : UF, 'Direccion' : direccion, 'Region' : region},ignore_index = True)
            
            time.sleep(random.uniform(5.0,8.0))  
            driver.find_element_by_xpath('//*[@id="resul"]/nav/ul/li[4]/a').click()
            
    print(df)
        
    driver.quit()
    conn=sql.connect('valores.db')
    df.to_sql('valores',conn)
scrapper()  

def cadahora():
    scrapper()
    time.sleep(3600)
    while True:
        scrapper()
        time.sleep(3600)





