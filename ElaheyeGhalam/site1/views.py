from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'elaheyeghalam.html')
def decorsazi(request):
    return render(request, 'decorsazi.html')
def ghorfesazi(request):
    return render(request, 'otherHtml/catalog3.html')
def kabinet_sazi(request):
    return render(request, 'otherHtml/catalog.html')
def chap_va_tablighat(request):
    return render(request, 'otherHtml/catalog2.html')
def aboutus(request):
    return render(request, 'otherHtml/aboutus.html')
def contactus(request):
    return render(request, 'otherHtml/contactus.html')