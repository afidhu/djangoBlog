from django import forms
from.models import Post, Comment,Follow

class postForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=('author','user_profile',)
        fields="__all__"
        widgets={
            'title':forms.TextInput(),
            "video":forms.FileInput(),
            "content":forms.Textarea(attrs={'rows':4}),
            "image":forms.FileInput(),
            }
        
    def __init__(self, *args, **kwargs):
        super(postForm, self).__init__(*args, **kwargs)    
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'
        
        
        
class commentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('content',)
        widgets={
            "content":forms.Textarea(attrs={'rows':4,'class':'form-control'}),
            }
        
        
class followForm(forms.ModelForm):
    class Meta:
        model=Follow
        exclude=('follower', 'followee')
        
        