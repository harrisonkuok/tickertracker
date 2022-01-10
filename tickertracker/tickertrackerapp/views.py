from tickerupdater import tickerApi
from django.shortcuts import render
from .models import Stock

# Create your views here.

def stock_mentions_ranking(request):
    top_mentioned_stocks = Stock.get_top_mentioned(10)
    context = {
        "stocks": top_mentioned_stocks
    }
    return render(request, 'stock_mentions_ranking.html', context)
