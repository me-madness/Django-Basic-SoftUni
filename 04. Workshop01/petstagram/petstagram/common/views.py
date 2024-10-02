from django.shortcuts import render # type: ignore


# Create your views here.
def home_page(request):
    return render(request, 'common/home-page.html')
