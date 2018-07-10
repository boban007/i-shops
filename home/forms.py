from django import forms

class ContactForm(forms.Form):

    name = forms.CharField(max_length=100)
    name.widget.attrs['class'] = 'form-control'
    name.widget.attrs['placeholder'] = 'Name'

    email = forms.EmailField()
    email.widget.attrs['class'] = 'form-control'
    email.widget.attrs['placeholder'] = 'Email'

    subject = forms.CharField(max_length=100)
    subject.widget.attrs['class'] = 'form-control'
    subject.widget.attrs['placeholder'] = 'Subject'

    message = forms.CharField(widget=forms.Textarea)
    message.widget.attrs['id'] = 'message'
    message.widget.attrs['class'] = 'form-control'
    message.widget.attrs['placeholder'] = 'Your Message Here'
    message.widget.attrs['rows'] = '8'
