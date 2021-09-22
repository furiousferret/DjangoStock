from django.shortcuts import render, redirect
from .models import Stock
from .forms import stockForm
from django.contrib import messages



# api key
# pk_44018fadc8e0420489b04bd2cf0b7a88
def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_44018fadc8e0420489b04bd2cf0b7a88")
    
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error Posting" 
        return render(request, 'home.html', {'api': api})    
    
    else:
        return render(request, 'home.html', {'ticker':"Enter a Ticker Name"})    


def about(request):
    return render(request, 'about.html')    

def add_stock(request):
    import requests
    import json

    if request.method == 'POST':
        form = stockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added"))
            return redirect('add_stock')
        
    else:
        ticker = Stock.objects.all()
        output = []
        
        for ticker_item in ticker:

            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_44018fadc8e0420489b04bd2cf0b7a88")
    
            try:
                api = json.loads(api_request.content)
                output.append(api)

            except Exception as e:
                api = "Error Posting" 

        return render(request, 'add_stock.html',{'ticker': ticker, 'output':output})  


def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)      
    item.delete
    messages.success(request, ("Stock has been deleted"))
    return redirect('add_stock')  

def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, 'delete_stock.html', {'ticker':ticker})                  

