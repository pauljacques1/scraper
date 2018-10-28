import schedule
import time
import json

def job():
    with open('/Users/pauljacques/articles_news.json', 'r+') as f:
        data=json.load(f)
        for i in range(0,len(feed.entries)):
            if feed.entries[i].get('title') not in data:
                data[feed.entries[i].get('title')]=[feed.entries[i].get('summary'),feed.entries[i].get('link')]
        json=json.dumps(data)
        f = open("/Users/pauljacques/articles_news.json","w")
        f.write(json)
        f.close()

schedule.every(1).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)