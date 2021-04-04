from django import forms


from .models import Messages


class SendMessage(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('pic', )
