from urllib.request import urlopen, Request
import re
import os
from db_connect import Database
from htmlSoup import htmlSoup


#a complete change of concept, we're doing only scraping from the actual item website


class WebScraper:
    def __init__(self, item_link):
        self.item_link = item_link
        #easy way to determine whether or not the user input is a link
            
        
    def scrape(self): 
            print('matched')
            link = self.item_link
            page = urlopen(link) 
            return page.read().decode('utf-8')
    def get_item_info(self):
        html = WebScraper(self.item_link).scrape()
        soup = htmlSoup(html)
        
        #unfortunately this only works for amazon since im too lazy to actually get something like a universal thing for every website, along with the limitations that are caused because of how every single website is building a freaking castle to protect themselves from crawling
        p_name = soup.findString('productTitle')
        
        image_div = html.find('<div id="imgTagWrapperId"')
        image_start = html.find('src="', image_div)
        image_start = image_start + len('src="')
        image_end = html.find('"', image_start)
        
        image = html[image_start:image_end]
        pr_whole = soup.findString('a-price-whole')
        pr_frac = soup.findString('a-price-fraction')
        
        product_name = p_name
        
        product_price = pr_whole + '.' + pr_frac
        product_price = product_price.replace('\xa0', '')
        product_price = float(product_price)
        
        return Database().insert_data('products',[{'product_name':product_name, 'product_price':product_price,'product_link': self.item_link, 'product_image': image}])
    

    
   