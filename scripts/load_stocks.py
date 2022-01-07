import csv

from tickertrackerapp.models import Stock

def run():
    fhand = open('tickertrackerapp/ticker_list.csv')
    reader = csv.reader(fhand)

    Stock.objects.all().delete()

    for row in reader:
        Stock.objects.create(ticker=row[0], name=row[1])