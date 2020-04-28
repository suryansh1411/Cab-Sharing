from django import forms


class PostForm(forms.ModelForm):
    message=forms.CharField(max_length=500, widget=forms.TextInput)
    class Meta():
        field=('message')
