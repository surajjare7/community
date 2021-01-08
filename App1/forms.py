from django import forms

from .models import Post, Query, Solution


class PostForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField(max_length=600)
    # category = forms.CharField()
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ('title','description','image')

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields=['question']
                

class SolutionForm(forms.ModelForm):
    class Meta:
        model=Solution
        fields=['answer']
