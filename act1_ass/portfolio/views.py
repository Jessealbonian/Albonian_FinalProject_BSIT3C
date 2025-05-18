from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "pages/index.html")

def dshbrd(request):
        data = [
            {"title": "Users", "count": 150},
            {"title": "Orders", "count": 320},
            {"title": "Revenue", "count": "12450"},
        ]  
        return render(request, "pages/dshbrd.html", context={"data": data})

def portfolio(request):
    return render(request, "pages/portfolio.html")
