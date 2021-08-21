import datetime

import yagmail
import pandas as pd
from yagmail import YagAddressError
import time

from news import NewsFeed

while True:
    if datetime.datetime.now().hour == 9 and datetime.datetime.now().minute == 31:
        df = pd.read_excel('people.xlsx')

        for index, row in df.iterrows():
            try:
                news_feed = NewsFeed(interest=row['interest'], language='en')
                email = yagmail.SMTP(user='<Login Email Address>', password='<Enter Password>')
                email.send(to=row['email'],
                           subject=f"Your today's news article about {row['interest']}",
                           contents=f"Hi {row['name']}, \n See what's on about {row['interest']} today.\n\n "
                                    f"{news_feed.get()} \n\n Thanks & Regards,\n Support Team")
            except YagAddressError as e:
                break

    time.sleep(60)
