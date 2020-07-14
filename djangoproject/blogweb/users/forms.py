from django import forms

class Login(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class Signup(forms.Form):
    fname = forms.CharField(max_length=200,label="FirstName")
    lname = forms.CharField(max_length=200,label="LastName")
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    image = forms.ImageField()

class Forgot(forms.Form):
    email = forms.EmailField()

class Otp(forms.Form):
    otp = forms.CharField()
    
#print(dir(forms))
#<input type="text" name="fname">
#formspy --> form
#views.py --> function
#html page --> templates
#accept forms in 3 ways on html page
#form.as_p
#form.as_table
#form.as_ul