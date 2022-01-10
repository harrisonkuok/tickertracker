from psaw import PushshiftAPI
import datetime as dt
import reticker

from tickertrackerapp.models import Stock

EXTRACTOR = reticker.TickerExtractor()

def _get_today_timestamp():
    now_pst = dt.datetime.today() - dt.timedelta(hours=8)
    today_utc = dt.datetime(now_pst.year, now_pst.month, now_pst.day) + dt.timedelta(hours=8)
    return int(today_utc.timestamp())

def _get_subreddit_submissions():
    api = PushshiftAPI()
    start = _get_today_timestamp()
    submissions = list(api.search_submissions(after=start,
                            subreddit='wallstreetbets',
                            filter=['title']))
    return submissions

def _filter_ticker_like(text):
    return EXTRACTOR.extract(text)

def _get_ticker_mentioned():
    submissions = _get_subreddit_submissions()
    ticker_mentioned = []
    for submission in submissions:
        ticker_mentioned += _filter_ticker_like(submission.title)
    return ticker_mentioned

def update_mentions():
    ticker_mentioned = _get_ticker_mentioned()
    Stock.objects.all().update(mention=0)
    for ticker in ticker_mentioned:
        try:
            stock = Stock.objects.get(ticker=ticker.upper())
            stock.mention += 1
            stock.save()
        except:
            continue
