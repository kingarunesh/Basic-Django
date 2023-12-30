from django.shortcuts import render


def fees(request):
    """
        fees page view
    """

    context = {
        "title": "Fees Page"
    }

    return render(request=request, template_name="fees/fees.html", context=context)
