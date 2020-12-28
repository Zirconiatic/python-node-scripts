from google_play_scraper import Sort, reviews_all
import sys

import xlwt 
from xlwt import Workbook

# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('PlayReviews')

#package_name = 'com.activision.callofduty.shooter'
#reviews in excel playstore
package_name = 'in.hsbc.hsbcindia'
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
# result is list + dictionary
# intializing the name of the headers
sheet1.write(0,0,'reviewId')
sheet1.write(0,1,'userName')
sheet1.write(0,2,'userImage')
sheet1.write(0,3,'content')
sheet1.write(0,4,'score')
sheet1.write(0,5,'thumbsUpCount')
sheet1.write(0,6,'reviewCreatedVersion')
sheet1.write(0,7,'at')
sheet1.write(0,8,'replyContent')
sheet1.write(0,9,'repliedAt')

outer_count = 1
for i in result:
    inner_count = 0
    for key,value in i.items():
        #print(str(outer_count),str(inner_count))
        sheet1.write(outer_count, inner_count, str(value))
        inner_count = inner_count + 1
    outer_count = outer_count + 1

wb.save('play_HSBC_India_reviews1.xls')