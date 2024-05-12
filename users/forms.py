from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from users.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4",
                                                             "placeholder": "Введите имя пользователя"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control py-4",
                                                                 "placeholder": "Введите пароль"}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widgets = {
            'email': forms.EmailInput(attrs={"class": "form-control py-4"}),
            'first_name': forms.TextInput(attrs={"class": "form-control py-4"}),
            'last_name': forms.TextInput(attrs={"class": "form-control py-4"}),
            'username': forms.TextInput(attrs={"class": "form-control py-4"}),
            'password1': forms.PasswordInput(attrs={"class": "form-control py-4"}),
            'password2': forms.PasswordInput(attrs={"class": "form-control py-4"}),

        }
        help_texts = {
            'username': 'Введите уникальное имя пользователя',
            'email': 'Введите действующий адрес электронной почты',
            'password1': 'Пароль должен содержать не менее 8 символов и включать цифры и специальные символы',
            'password2': 'Повторите пароль для подтверждения',
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой email уже существует")
        return email


class ProfileUserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'image', 'username', 'email']
