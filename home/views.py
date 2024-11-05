from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def credits(request):
    content = "Manho Joung"
    return HttpResponse(content, content_type="text/plain")

def news(request):
    data = {
        'news': [
            "MamboStory has a news page!",
            "MamboStory has its first web page",
        ],
    }
    return render(request, "news2.html", data)