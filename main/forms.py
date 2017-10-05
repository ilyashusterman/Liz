from django import forms


class Trip(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    destination = forms.CharField(label='Destination', max_length=100)
    stops = forms.CharField(label='Stops', max_length=100)
    img_url = forms.CharField(label='Image Url', max_length=100)