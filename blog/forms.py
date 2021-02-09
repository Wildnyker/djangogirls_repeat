from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

"""
This form is directly based on model from 
models.py - forms.ModelForm defines that
out form will be nased on some model
In Meta class in fields we define what model will be used
and whar fields will be used in our form

Only the logged into admin person will be able to use form
as we do not define anythin other
"""


#32 now go to the base.html and create a button for edit