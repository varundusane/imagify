from django import forms

<<<<<<< HEAD

from .models import Messages


class SendMessage(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ('pic', )
=======
from .models import Messages

class SendMessage(forms.ModelForm):
    message = forms.CharField(
        label='Message',
        max_length=255,
        widget=forms.Textarea,
        help_text="You have 255 characters remainings",


    )

    class Meta:
        model = Messages
        fields = ('pic', 'message', )
>>>>>>> 02ac08a5e02b8c2bb1451d42ec17bf3afa8b0827
