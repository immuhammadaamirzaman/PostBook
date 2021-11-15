from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserSignUpForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def SignUp(request):
    if request.method=="POST":
        form=UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Your Account has been Created!') 
            return redirect('signin')
    else:
        form=UserSignUpForm()
    return render(request,'UserApp/signUp.html',{'form':form})

@login_required
def Profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,'Your Profile has been Updated!')
            return redirect('profile')
    else:#if req is get then dont save the form info
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'UserApp/proFile.html',context)