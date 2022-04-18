from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.db.models import Q

from .models import Organism

# Create your views here.
def organism(request, organism_id):
    organism = get_object_or_404(Organism, id=organism_id)
    context = {
        'active_organisms': 'active',
        'organism': organism
    }
    return render(request, 'life/organism.html', context=context)

class SearchView(ListView):
    model = Organism
    template_name = 'life/search.html'

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        if query:
            object_list = Organism.objects.filter(Q(name__icontains=query) | Q(scientific_name__icontains=query))
        else:
            object_list = Organism.objects.all().order_by('-id')[:8]
        return object_list

    def get_context_data(self,**kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['num_of_orgs'] = len(context['object_list'])
        context['active_organisms'] = 'active'
        q = self.request.GET.get("q")
        if q:
            context['query'] = q
        return context