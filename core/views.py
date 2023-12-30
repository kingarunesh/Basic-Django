from django.shortcuts import render


def home(request):
    """
        Home Page
    """
    return render(request=request, template_name="index.html")




# from datetime import datetime
# def home(request):
#     """
#         Home Page
#     """

#     #NOTE :         context
#     context = {
#         "title": "Home Page",
#         "first_name": "Arunesh",
#         "last_name": "kumar",
#         "age": 24.6,

#         "names": ["Aohan", "Bohan", "Cohan", "Dohan", "Eohan"],
#         "hello": [],
        
#         "person": {
#             "first_name": "Arunesh",
#             "last_name": "kumar",
#             "age": 24.6,
#             "gadgets": ["Mobile", "Mouse", "Laptop", "Monitor"]
#         },

#         "a": "arunesh",
#         "b": "ARUNESH",
#         "c": "ArUnESh",
#         "d": "",
#         "e": 12.2,
#         "f": 12.2234,
#         "g": 12.220000,
#         "h": 12.22345234345,
#         "i": 12,
#         "j": 12.0,

#         "date": datetime.now() ,





#         "text": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Laboriosam libero omnis provident perferendis ducimus! Autem voluptates iure, voluptatem praesentium atque assumenda sapiente distinctio voluptate accusantium maxime. Nam vero nihil ad."
#     }

#     return render(request=request, template_name="course/index.html", context=context)
