from django import forms
from hello.models import LogMessage

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ["message",] # NOTE: the trailling comma is required