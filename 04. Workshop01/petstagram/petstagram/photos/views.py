from django.shortcuts import render # type: ignore

# Create your views here.
def photo_add_page(request):
    return render(request, 'photo/photo-add-page.html')


def photo_edit_page(request):
    return render(request, 'photo/photo-edit-page.html')
                  
                  
def photo_details_page(request):
    return render(request, 'photo/photo-details-page.html')                  