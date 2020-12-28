from google_play_scraper import Sort, reviews_all
import sys

package_name = 'com.activision.callofduty.shooter'
result = reviews_all(
    package_name,
    sleep_milliseconds=0, # defaults to 0
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    #filter_score_with=5 # defaults to None(means all score)
)

count = 0

#print(result)
f= open(package_name+".txt","w+")
# result is list + dictionary
for i in result:
    for key,value in i.items():
        try:
            f.write(key+"->"+str(value)+"\n")
        except:
            print("Oops!", sys.exc_info()[0], "occurred.")
    count = count + 1
    f.write("Review Number->"+str(count)+"\n")
    f.write("\n")

f.close()
