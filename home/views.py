from django.shortcuts import render, HttpResponse

# Create your views here.


def home_view(request):
    if request.user.is_authenticated:
        context = {
            'name': 'ataner',
        }
    else:
        context = {
            'name': 'misafir',
        }
    return render(request, 'home.html', context)
