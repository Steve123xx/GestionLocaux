import os
from django.shortcuts import render, get_object_or_404
from .form import loginUser,loginAdmin,EnrgAdmin,EnrgUser,SupprimerAdmin,SupprimerUser
from .models import LoginUser,LoginAdmin
# from .process import html_to_pdf
from django.views.generic import View
from django.http import HttpResponse
from django.template.loader import render_to_string
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

global o1,o2,o3,o4,o5,o6,o7,o8
o1=1
o2=2
o3=3
o4=4
o5=5
o6=6
o7=7
o8=8

def profile(nom):
    profi=LoginAdmin.objects.all()
    for prof in profi:
        
        if prof.AdminName==nom:
            f=f'{prof.profile}'
            return f

# def dict_user(model):
#     dictionnaire={}
#     for i in model:
#         dictionnaire[f"{i.UserName}"]=i.Password
#     return dictionnaire

# def dict_Admin(model):
#     dictionnaire={}
#     for i in model:
#         dictionnaire[f"{i.AdminName}"]=i.Password
#     return dictionnaire

def LoginUsers(request):
    if request.method=='POST':
        form1=loginUser(request.POST)
        if form1.is_valid():
            if LoginUser.objects.filter(UserName=form1.cleaned_data['userName']).exists():
                if LoginUser.objects.filter(Password=form1.cleaned_data['password']).exists():
                    usern=LoginUser.objects.get(UserName=form1.cleaned_data['userName'])
                    userp=LoginUser.objects.get(Password=form1.cleaned_data['password'])
                    return render(request, 'HomeUser\Home.html',{'userName':usern,'password':userp,'form':form1})

    return render(request, 'Form/LoginUser.html',{'login':loginUser})

def LoginAdmins(request):
    if request.method=='POST':
        form1=loginAdmin(request.POST)
        if form1.is_valid():
            if LoginAdmin.objects.filter(AdminName=form1.cleaned_data['userName']).exists():
                if LoginAdmin.objects.filter(Password=form1.cleaned_data['password']).exists():
                    usern=LoginAdmin.objects.get(AdminName=form1.cleaned_data['userName'])
                    return render(request, 'HomeAdmin/Home.html',{'profile':profile(f"{usern}"),'nom':usern,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'o6':o6,'o7':o7,'o8':o8})

    return render(request, 'Form/LoginAdmin.html',{'login':loginAdmin})

#Opérations Administrateur

def Operations(request,nom,ListeUser):
    admin=LoginAdmin.objects.all()
    user=LoginUser.objects.all()
    if ListeUser==1:
        return render(request, "HomeAdmin/Operation/liste/ListeUser.html",{'profile':profile(nom),'nom':nom,'operation':ListeUser,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'o6':o6,'o7':o7,'o8':o8,'user':user})
    elif ListeUser==2:
        return render(request, "HomeAdmin/Operation/liste/ListeAdmin.html",{'profile':profile(nom),'nom':nom,'operation':ListeUser,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'o6':o6,'o7':o7,'o8':o8,'admin':admin})
    elif ListeUser==3:
        user_name=",".join([e.UserName for e in LoginUser.objects.all()])
        user_pass=",".join([e.Password for e in LoginUser.objects.all()])
        return render(request, "HomeAdmin/Operation/modifier/ModifierUser.html",{'login':EnrgUser,'profile':profile(nom),'nom':nom,'operation':ListeUser,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'o6':o6,'o7':o7,'o8':o8,'user_name':user_name,"user_pass":user_pass})
    elif ListeUser==4:
        Admin_name=",".join([e.AdminName for e in LoginAdmin.objects.all()])
        Admin_pass=",".join([e.Password for e in LoginAdmin.objects.all()])
        return render(request, "HomeAdmin/Operation/modifier/ModifierAdmin.html",{'login':EnrgAdmin,'profile':profile(nom),'nom':nom,'operation':ListeUser,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'o6':o6,'o7':o7,'o8':o8,'admin_name':Admin_name,"admin_pass":Admin_pass})
    elif ListeUser==5:
        if request.method=='POST':
            form1=EnrgUser(request.POST,request.FILES)
            if form1.is_valid():
                try:
                    Enregistrer=LoginUser(UserName=form1.cleaned_data['user_Name'],Password=form1.cleaned_data['password'],profile=request.FILES['Photo_profile'])
                    Enregistrer.save()
                    valid=f"L'enregistrement de l'utilisateur {form1.cleaned_data['user_Name']} été effectuer qvec succes"
                    return render(request, "HomeAdmin/Operation/Enregistrer/EnregistrerUser.html",{'valide':valid,'login':EnrgUser,'profile':profile(nom),'nom':nom,'operation':ListeUser,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'o6':o6,'o7':o7,'o8':o8})
                except:
                    valid=f"l'utilisateur {form1.cleaned_data['user_Name']} ou ce mot de passe existe deja"
                    return render(request, "HomeAdmin/Operation/Enregistrer/EnregistrerUser.html",{'valide':valid,'login':EnrgUser,'profile':profile(nom),'nom':nom,'operation':ListeUser,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'o6':o6,'o7':o7,'o8':o8})

        user=",".join([e.UserName for e in LoginUser.objects.all()])
        return render(request, "HomeAdmin/Operation/Enregistrer/EnregistrerUser.html",{'login':EnrgUser,'profile':profile(nom),'nom':nom,'operation':ListeUser,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'o6':o6,'o7':o7,'o8':o8,'user':user})
    elif ListeUser==6:
        if request.method=='POST':
            form1=EnrgAdmin(request.POST,request.FILES)
            if (form1.is_valid()):
                try:
                    Enregistrer=LoginAdmin(AdminName=form1.cleaned_data['admin_Name'],Password=form1.cleaned_data['password'],profile=request.FILES['Photo_profile'])
                    Enregistrer.save()
                    valid=f"L'enregistrement de l'administrateur {form1.cleaned_data['admin_Name']} a été effectuer qvec succes"
                    return render(request, "HomeAdmin/Operation/Enregistrer/EnregistrezAdmin.html",{'valide':valid,'login':EnrgUser,'profile':profile(nom),'nom':nom,'operation':ListeUser,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'o6':o6,'o7':o7,'o8':o8})
                except:
                    valid=f"l'administrateur {form1.cleaned_data['admin_Name']} ou ce mot de passe existe deja"
                    return render(request, "HomeAdmin/Operation/Enregistrer/EnregistrezAdmin.html",{'valide':valid,'login':EnrgUser,'profile':profile(nom),'nom':nom,'operation':ListeUser,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'o6':o6,'o7':o7,'o8':o8})
        Admin=",".join([e.AdminName for e in LoginAdmin.objects.all()])
        return render(request, "HomeAdmin/Operation/Enregistrer/EnregistrezAdmin.html",{'login':EnrgAdmin,'profile':profile(nom),'nom':nom,'operation':ListeUser,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'o6':o6,'o7':o7,'o8':o8,'Admin':Admin})
    elif ListeUser==7:
        if request.method=='POST':
            form1=SupprimerUser(request.POST)
            if form1.is_valid():
                name=LoginUser.objects.get(UserName=f"{form1.cleaned_data['Nom_Utilisateur']}")
                os.remove(os.path.join(BASE_DIR,(f'Login/static/{name.profile}')))
                name.delete()
                valid=f"La suppression de l'utilisateur {form1.cleaned_data['Nom_Utilisateur']} a été effectuer avec succes"
                return render(request, "HomeAdmin/Operation/supprimer/SupprimerUser.html",{'profile':profile(nom),'nom':nom,'operation':ListeUser,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'o6':o6,'o7':o7,'o8':o8,'user':user,'login':SupprimerUser,'valide':valid})
        user=",".join([e.UserName for e in LoginUser.objects.all()])
        return render(request, "HomeAdmin/Operation/supprimer/SupprimerUser.html",{'profile':profile(nom),'nom':nom,'operation':ListeUser,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'o6':o6,'o7':o7,'o8':o8,'user':user,'login':SupprimerUser})
    else:
        if request.method=='POST':
            form1=SupprimerAdmin(request.POST)
            if form1.is_valid():
                name=LoginAdmin.objects.get(AdminName=f"{form1.cleaned_data['Nom_Administrateur']}")
                os.remove(os.path.join(BASE_DIR,(f'Login/static/{name.profile}')))
                name.delete()
                valid=f"La suppression de l'administrateur {form1.cleaned_data['Nom_Administrateur']} a été effectuer avec succes"
                return render(request, "HomeAdmin/Operation/supprimer/SupprimerAdmin.html",{'profile':profile(nom),'nom':nom,'operation':ListeUser,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'o6':o6,'o7':o7,'o8':o8,'user':user,'login':SupprimerUser,'valide':valid})
        Admin=",".join([e.AdminName for e in LoginAdmin.objects.all()])
        return render(request, "HomeAdmin/Operation/supprimer/SupprimerAdmin.html",{'profile':profile(nom),'nom':nom,'operation':ListeUser,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'o6':o6,'o7':o7,'o8':o8,'Admin':Admin,'login':SupprimerAdmin})
    
    return render(request, "HomeAdmin/Operation/Operations.html",{'profile':profile(nom),'nom':nom,'operation':ListeUser,'o1':o1,'o2':o2,'o3':o3,'o4':o4,'o5':o5,'o6':o6,'o7':o7,'o8':o8})
