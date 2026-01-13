from django.shortcuts import render

def dashboard(request):
    return render(request, 'mainpage/dashboard.html', {
        'hide_navbar': True
    })
