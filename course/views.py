from django.shortcuts import render


def home(request):
    """
        Home Page
    """
    return render(request=request, template_name="index.html")
