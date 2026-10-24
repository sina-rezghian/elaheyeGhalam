from django.shortcuts import render

from .content import SERVICES, DECOR_SERVICES, CATALOGS


def index(request):
    return render(request, 'elaheyeghalam.html', {'services': SERVICES})
def decorsazi(request):
    return render(request, 'decorsazi.html', {'services': DECOR_SERVICES})
def ghorfesazi(request):
    return render(request, 'otherHtml/catalog_base.html', CATALOGS['ghorfesazi'])
def kabinet_sazi(request):
    return render(request, 'otherHtml/catalog_base.html', CATALOGS['kabinet_sazi'])
def chap_va_tablighat(request):
    return render(request, 'otherHtml/catalog_base.html', CATALOGS['chap_va_tablighat'])
def aboutus(request):
    return render(request, 'otherHtml/aboutus.html')
def contactus(request):
    return render(request, 'otherHtml/contactus.html')


def search(request):
    query = request.GET.get('q', '').strip()[:200]

    def normalize(text):
        return text.replace('ي', 'ی').replace('ك', 'ک').replace('\u200c', '').replace(' ', '').casefold()

    results = [service for service in SERVICES + DECOR_SERVICES
               if normalize(query) in normalize(service['title'] + service['description'])] if query else []
    return render(request, 'search.html', {'query': query, 'results': results})
