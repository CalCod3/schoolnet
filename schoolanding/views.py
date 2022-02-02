from django.shortcuts import render

def landing_view(request, *args, **kwargs):
    
    template = 'landing.html'
    
    return render(request, template)