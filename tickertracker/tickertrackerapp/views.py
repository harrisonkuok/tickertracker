from django.http.response import JsonResponse

from .models import Stock
from .serializers import StockSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def stock_mentions_ranking(request):
    top_mentioned_stocks = Stock.get_top_mentioned(10)

    if request.method == 'GET':
        stocks_serializer = StockSerializer(top_mentioned_stocks, many=True)
        return JsonResponse(stocks_serializer.data, safe=False)


# def stock_mentions_ranking(request):
#     top_mentioned_stocks = Stock.get_top_mentioned(10)
#     context = {
#         "stocks": top_mentioned_stocks
#     }
#     return render(request, 'stock_mentions_ranking.html', context)
