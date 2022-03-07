from django.shortcuts import render

# Create your views here.
def organisms(request):
    context = {
        'active_organisms': 'active'
    }
    return render(request, 'life/index.html', context=context)