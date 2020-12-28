from itunes_app_scraper.scraper import AppStoreScraper
from pprint import pprint

#not using this script
scraper = AppStoreScraper()
results = scraper.get_app_details(app_id='1287282214',country='in') 
# we can get the average rating
#from this code

pprint(results)