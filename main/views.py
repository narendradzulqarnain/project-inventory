from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'appname' : 'this is an inventory',
        'name': 'Narendra Dzulqarnain',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)