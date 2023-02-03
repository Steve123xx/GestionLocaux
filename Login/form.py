from django import forms
#formulaires du login
class loginUser(forms.Form):
    userName=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)

class loginAdmin(forms.Form):
    userName=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)

#formulaires de l'enregistrement

class EnrgUser(forms.Form):
    user_Name=forms.CharField(max_length=100,label="Nom de l'utilisateur")
    Photo_profile=forms.ImageField()
    password=forms.CharField(widget=forms.PasswordInput,label="Mot de passe")

class EnrgAdmin(forms.Form):
    admin_Name=forms.CharField(max_length=100,label="Nom de l'Administrateur")
    Photo_profile=forms.ImageField()
    password=forms.CharField(widget=forms.PasswordInput,label="Mot de passe")

class SupprimerUser(forms.Form):
    Nom_Utilisateur=forms.CharField(max_length=100)

class SupprimerAdmin(forms.Form):
    Nom_Administrateur=forms.CharField(max_length=100)