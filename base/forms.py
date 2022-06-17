from django import forms
from .models import *

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('__all__')

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ('__all__')
