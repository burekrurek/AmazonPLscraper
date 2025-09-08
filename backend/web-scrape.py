from urllib.request import urlopen
import re
import os
from db_connect import Database
from htmlSoup import htmlSoup


#a complete change of concept, we're doing only scraping from the actual item website


class WebScraper:
    def __init__(self, item_link):
        self.item_link = item_link
        #easy way to determine whether or not the user input is a link
        if re.match('https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/\/=]*)',self.item_link):
            self.is_link = True
        
    def scrape(self): 
        link = self.item_link
        page = urlopen(link) 
        return page.read().decode('utf-8')
        
    def get_item_info(self):
        soup = htmlSoup(WebScraper.scrape(self))
        
        #unfortunately this only works for amazon since im too lazy to actually get something like a universal thing for every website, along with the limitations that are caused because of how every single website is building a freaking castle to protect themselves from crawling
        p_name = soup.findByClassOrId('productTitle')
        
        
        pr_whole = soup.findByClassOrId('a-price-whole')
        pr_frac = soup.findByClassOrId('a-price-fraction')
        
        product_name = p_name
        
        product_price = pr_whole + '.' + pr_frac
        product_price = product_price.replace('\xa0', '')
        product_price = float(product_price)
        
        return Database().insert_data('products',[{'product_name':product_name, 'product_price':product_price,'product_link': self.item_link}])
    

    
   
    


if __name__ == '__main__':
    try:
        os.environ['PYPPETEER_DOWNLOAD_HOST'] = 'https://commondatastorage.googleapis.com/'
    except Exception as e:
        print(e)
    
    print(WebScraper(item_link = 'https://www.amazon.pl/Odwaga-bycia-nielubianym-Japo%C5%84ski-pokazuje/dp/8375796026/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.0986b30d-9179-4dd7-950d-777bac5aba2b&dib=eyJ2IjoiMSJ9.xj2DHBgvkwwIbIqLHPwPFzaNE7cEyX05NiQ6DFHoUji576d9xgblPZ5HaoiHCIZSUH646k3NMpUtPqME3SIIrWmLkDq-GsxcAUTp3kzwhZG-GZuv4bkIFmGKOWPd2tLZFY0lbp6kMk_noCadHqun-l6R0EPycdVoMlyOBRa8DWgNLfgCZBWN3sTVQ_GGL1gUChvCCMBPvYzayghPIi7DVznk98dWMGHOn9A5octmJhI._maTouDxQIbpGrZLm-5ce8mhay158UPW6AAjk6EWxjE&dib_tag=se&pd_rd_r=e37cda32-5ecf-40c8-9e7d-9be2f75fe833&pd_rd_w=vmSsJ&pd_rd_wg=6a9wa&qid=1757316059&refinements=p_36%3A-3900&rnid=20876091031&s=books&sr=1-1').get_item_info())
    print(Database().read_data('products'))