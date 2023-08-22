from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(label='ایمیل',
                             widget=forms.EmailInput()
                             )
    password = forms.CharField(label='پسورد',
                               widget=forms.PasswordInput()
                               )
    password_confirmation = forms.CharField(label='تکرار پسورد',
                                            widget=forms.PasswordInput(),
                                            )

    def clean_password_confirmation(self):
        # custom validation that rais field error
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if password == password_confirmation:
            return password_confirmation
        raise ValidationError('پسورد و تکرار پسورد مطابقت ندارند')

    # def clean(self):
    #     # custom validation that rais non-field error
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     password_confirmation = cleaned_data.get('password_confirmation')
    #
    #     if password and password_confirmation and password != password_confirmation:
    #         raise ValidationError('Passwords do not match.')
    #     return cleaned_data
