
from django.shortcuts import render
from django.template import context
from .models import Article


def article_search_view(request):
    print(request.GET)
    query_dic = request.GET  # This is a dictionary

    try:
        # query comes from the input name inside the form
        query = int(query_dic.get("query"))
    except:
        query = None

    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)

    context = {
        "object":  article_obj,
    }
    return render(request, "articles/search.html", context=context)


def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object":  article_obj,
    }
    return render(request, "articles/detail.html", context=context)
