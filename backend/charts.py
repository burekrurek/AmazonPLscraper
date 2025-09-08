import pandas as pd
import matplotlib.pyplot as plt
from db_connect import Database

db = Database()

class charts:
    def __init__(self):
        return        
    
    def chart_from_csv(csv_file):
        db.sql_to_csv('products')
        
charts().chart_from_csv()
        