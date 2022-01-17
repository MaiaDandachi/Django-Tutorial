"""
To Render HTML web pages
"""

from django.http import HttpResponse

HTML_STRING = """ <h1>Home Page</h1>"""


def home_view(request):
    """
    Takes in a django request
    Returns an HTML response 
    """
    return HttpResponse(HTML_STRING)
