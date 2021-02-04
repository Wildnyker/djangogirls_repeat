from django.urls import path #18 import
from blog import views #18 import this modules


#19 add this pattern
"""this way we assign view post_list to the base url"""
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
"""name='post_list', is the name of the URL that will be used to identify the view. 
This can be the same as the name of the view but it can also be something completely different."""

#20 go to views