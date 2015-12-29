from django import forms

FINANCE_TYPE =(("LIC","LIC"),("FD","FD"),("SAVING", "SAVING"))


class financeManagerForm(forms.Form):
    name = forms.CharField(required=True)
    policyNumber=forms.CharField(required=True)
    financetype = forms.ChoiceField(choices=FINANCE_TYPE, widget=forms.Select(), required=True)
    issueDate = forms.DateField(widget= forms.TextInput(
                                                    attrs={'class':'datepicker'}
                                     ))
    maturityDate= forms.DateField(widget= forms.TextInput(
                                                    attrs={'class':'datepicker'}
                                     )
                                  )
    amount = forms.IntegerField(required=True)
    remarks = forms.CharField(required=False,widget=forms.Textarea(attrs={'rows':5, 'cols':22}), max_length = 100)


class RegisterForm(forms.Form):
    firstname = forms.CharField(required=False, widget=forms.TextInput(attrs={'size': 32, 'placeholder': 'First Name.', 'class':'form-control'}))
    lastname = forms.CharField(required=False, widget=forms.TextInput(attrs={'size': 32, 'placeholder': 'Last Name.', 'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'size': 32, 'placeholder': 'Enter Username.', 'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'size': 32, 'placeholder': 'Enter email address', 'class':'form-control'}))
    password = forms.CharField( widget=forms.TextInput(attrs={'type':'password','size': 32, 'placeholder': 'Enter Password', 'class':'form-control'}))
    confirm_password = forms.CharField( widget=forms.TextInput(attrs={'type':'password', 'size': 32, 'placeholder': 'Confirm Password', 'class':'form-control'}))
   
    '''
    def clean_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError(" Confirm Password Did not match.")
            
    '''
class ProfileForm(forms.Form):
    firstname = forms.CharField(required=False, widget=forms.TextInput(attrs={'size': 32, 'placeholder': 'First Name.', 'class':'form-control'}))
    lastname = forms.CharField(required=False, widget=forms.TextInput(attrs={'size': 32, 'placeholder': 'Last Name.', 'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'size': 32, 'placeholder': 'Enter Username.', 'class':'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'size': 32, 'placeholder': 'Enter email address', 'class':'form-control'}))
    password = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'password','size': 32, 'placeholder': 'Enter Password', 'class':'form-control'}))
    confirm_password = forms.CharField(required=False, widget=forms.TextInput(attrs={'type':'password', 'size': 32, 'placeholder': 'Confirm Password', 'class':'form-control'}))
    