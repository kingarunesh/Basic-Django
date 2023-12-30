from django.shortcuts import render


def course(request):
    """
        course page
    """
    context = {
        "title": "Course Page",
        "last_course": "MERN"
    }

    return render(request=request, template_name="course/course.html", context=context)
