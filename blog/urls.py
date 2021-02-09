from django.urls import path #18 import
from blog import views #18 import this modules


#19 add this pattern
"""this way we assign view post_list to the base url"""
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name = 'post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit')

]
"""name='post_list', is the name of the URL that will be used to identify the view. 
This can be the same as the name of the view but it can also be something completely different."""

#20 go to views




#27 after this back this views to create post_detail
"""<int:pk>/It means that Django expects an integer value 
and will transfer it to a view as a variable called pk    
"""

#34 after adding post_new go to the views to add a view to that page


#40 after creating url for post_edit cteate this view in views