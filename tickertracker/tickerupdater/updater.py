from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler
from tickerupdater import tickerApi

def start():
    tickerApi.update_mentions()
    scheduler = BackgroundScheduler()
    scheduler.add_job(tickerApi.update_mentions, 'interval', minutes=1)
    scheduler.start()