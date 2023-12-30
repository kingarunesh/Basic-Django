from django.shortcuts import render


def course(request):
    """
        course page
    """
    context = {
        "title": "Course Page"
    }

    return render(request=request, template_name="course/course.html", context=context)
