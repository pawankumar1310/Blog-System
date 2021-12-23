from django.contrib.auth.forms import UserCreationForm
from account.models import Usermodel
from django.forms import ChoiceField



class SignUpForm(UserCreationForm):
    user_type = ChoiceField(choices=Usermodel.get_signup_types())

    class Meta:
        fields = ('username', 'email', 'password1', 'password2',
                  'user_type','bio')
        model = Usermodel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].label = 'username'
        self.fields['email'].label = 'Email Address'