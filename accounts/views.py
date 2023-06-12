from django.shortcuts import render,redirect
from .models import Profile
from django.core.mail import send_mail
from.forms import SingupForm

# Create your views here.


def sing_up(request):
    
    if request.method=='POST':
        form=SingupForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            form.save()
            
            profile=Profile.objects.get(user__username=username)

            
            send_mail(
                "Activate Your Accounts",
                f"Welcome {username}\n use this code{profile.code}to activate your accounts \n green store ",
                "ehsanmorgan1994@gmail.com",
                [email],
                fail_silently=False,
            )
            
            return redirect(f'/accounts/{username}/activate')
            
        
    else:
        
        form=SingupForm()
        
    return render(request,'registration/signup.html',{'form':form})