from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'appname' : 'what do we need to survive?',
        'name': 'become death, destroyer of worlds',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)