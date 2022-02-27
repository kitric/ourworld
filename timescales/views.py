from django.shortcuts import render

# Create your views here.
def timescales(request):
    return render(request, 'timescales/index.html', {'active_timescales':'active' })