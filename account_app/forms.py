from django import forms


class SignUpForm(forms.Form):
    first_name = forms.CharField(
        label='نام',
        widget=forms.TextInput()
    )
    last_name = forms.CharField(
        label='نام خانوادگی',
        widget=forms.TextInput()
    )
    age = forms.CharField(
        label='سن',
        widget=forms.TextInput()
    )
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput()
    )
    password = forms.CharField(
        label="پسورد",
        widget=forms.TextInput()
    )
    confirm_password = forms.CharField(
        label="تکرار پسورد",
        widget=forms.TextInput()
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        else:
            raise forms.ValidationError("رمز عبور های وارد شده یکسان نیستند")

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if 18 <= int(age) <= 50:
            return age
        else:
            raise forms.ValidationError("سن وارد شده صحیح نمیباشد")


class LoginForm(forms.Form):
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(),
        error_messages={
            'required': 'نام کاربری خود را وارد کنید'
        }
    )
    password = forms.CharField(
        label='پسورد',
        widget=forms.TextInput(),
        error_messages={
            'required': 'پسورد خود را وارد کنید'
        }
    )
