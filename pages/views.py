from django.shortcuts import render
from django.views.generic import TemplateView


def hom_page_view(request):
    context = {
        'inventory' : ['widget1' , 'widget2' , 'widget3'],
        'greeting' : 'arigato gozaimasu'

    }


    return render(request , 'home.html' , context)

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self , **qwargs):
        context = super().get_context_data(**qwargs)
        context['address'] = '123 imaginary street'
        context['number'] = '0775312007'
        return context


