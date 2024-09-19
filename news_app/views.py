from django.shortcuts import render
from django.views.generic import TemplateView
from .models import News, Category

# Create your views here.

def news_list(request):
    news_list=News.objects.filter(status=News.Status.Puplished)
    context={
        'news_list': news_list
    }
    return render(request, "news/news_list.html", context=context)
class HomePageView(TemplateView):
    template_name = "news/index.html"

class CategoryPageView(TemplateView):
    template_name = "news/category.html"

class SinglePageView(TemplateView):
    template_name = "news/single.html"

class ContactPageView(TemplateView):
    template_name = "news/contact.html"
