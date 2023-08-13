from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(label='نام و نام خانوادگی',
                           max_length=100,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'نام خود را وارد کنید'
                               },
                           ))
    email = forms.EmailField(label='ایمیل',
                             widget=forms.TextInput(
                                 attrs={
                                     'class': 'form-control',
                                     'placeholder': 'ایمیل خود را وارد کنید'
                                 },
                             ))
    message = forms.CharField(label='متن پیام',
                              widget=forms.Textarea(
                                  attrs={
                                      'id': 'message',
                                      'class': 'form-control',
                                      'placeholder': 'پیام خود را وارد کنید'
                                  },
                              ))
