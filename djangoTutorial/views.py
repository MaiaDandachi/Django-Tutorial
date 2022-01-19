"""
To Render HTML web pages
"""

from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request):
    """
    Takes in a django request
    Returns an HTML response 
    """
    article_obj = Article.objects.get(id=2)

    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }

    # H1_STRING = f"""<h1>{article_obj.title}</h1>"""
    # P_STRING = f"""<h1>{article_obj.content}</h1>"""
    # HTML_STRING = """ <h1>Home Page</h1>""" + H1_STRING + P_STRING

    # Django Templates
    HTML_STRING = render_to_string("home-view.html", context=context)

    return HttpResponse(HTML_STRING)
