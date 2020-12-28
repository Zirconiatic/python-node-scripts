from google_play_scraper import app
from pprint import pprint
import sys

#rating details of the application playtore
result = app(
    'com.activision.callofduty.shooter',
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)

pprint(type(result))
#pprint(result)

f= open("call-of-duty-rating-details.txt","w+")
# result is list + dictionary

for key,value in result.items():
    if (key == 'score' or key == 'ratings' or key == 'reviews' or key == 'released' or key == 'url' or key == 'version'):
        try:
            f.write(key+"->"+str(value)+"\n")
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
    if (key == 'histogram'):
        f.write("Rating Details:- \n")
        temp_count = 1
        pprint(type(value))
        for temp in value:
            try:
                pprint(type(temp))
                f.write(str(temp_count)+"->"+str(temp)+"\n")
                temp_count = temp_count + 1
            except:
                print("Oops!", sys.exc_info(), "occurred.")
f.write("\n")

f.close()