from django.urls import path

from .views import hom_page_view , AboutPageView

urlpatterns = [

path("about/" , AboutPageView.as_view() , name= "about"),
path("" , hom_page_view, name= "home")


]