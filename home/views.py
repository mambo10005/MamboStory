from django.http import HttpResponse

# Create your views here.
def credits(request):
    content = "Manho Joung"
    return HttpResponse(content, content_type="text/plain")