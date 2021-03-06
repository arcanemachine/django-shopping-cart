from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class NewUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = UserModel
        fields = UserCreationForm.Meta.fields + ('email',)

    def clean_email(self):
        if UserModel.objects.filter(email=self.cleaned_data['email']).exists():
            raise ValidationError("This email address is taken.")
        return self.cleaned_data['email']
