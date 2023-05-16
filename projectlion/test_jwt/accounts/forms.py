from django.contrib.auth.forms import UserCreationForm
from django.forms import models
from .models import Profile

# 회원가입 form 구현
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = '아이디'
        self.fields['email'].label = '이메일 주소'
        self.fields['first_name'].label = '이름'
        self.fields['last_name'].label = '성'

class ProfileForm(models.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address']
