from django.shortcuts import render

def track_list(request):
    return render(request, 'tracker/track_list.html', {})
