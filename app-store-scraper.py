from app_store_scraper import AppStore
from pprint import pprint
import sys

#this script is used to get the reviews and saving the same in text file appstore
app_details = AppStore(country="us", app_name="call-of-duty-mobile", app_id=479516143)

pprint(app_details)
app_details.review(how_many=1000)

#pprint(type(app_details.reviews))
pprint(app_details.reviews_count)

count = 0

f= open("call-of-duty-app-store.txt","w+")
for i in app_details.reviews:
    for key,value in i.items():
        try:
            f.write(key+"->"+str(value)+"\n")
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
    count = count + 1
    f.write("Review Number->"+str(count)+"\n")
    f.write("\n")

f.close()