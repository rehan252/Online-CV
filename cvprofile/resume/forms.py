from django import forms


class ContactForm(forms.Form):
    """"
    Contact form for collecting user enquiries
    """
    full_name = forms.CharField(widget=forms.TextInput, required=True)
    email_address = forms.EmailField(required=True)
    subject = forms.CharField(widget=forms.TextInput, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
