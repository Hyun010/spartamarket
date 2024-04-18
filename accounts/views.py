from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomUserCreationForm
from django.views.decorators.http import require_POST,require_http_methods
from django.contrib.auth.forms import (AuthenticationForm,)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from products.models import Product

@require_http_methods(['GET','POST'])
def signup(request):
    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('index')
    else:
        form=CustomUserCreationForm()
    context={"form":form}
    return render(request, 'accounts/signup.html',context)

@require_http_methods(['GET','POST'])
def login(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            next_path=request.GET.get("next") or "index"
            return redirect(next_path)
    else:
        form=AuthenticationForm()
    context={"form":form}
    return render(request, 'accounts/login.html',context)

@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('index')

def profile(request,username):
    member=get_object_or_404(get_user_model(),username=username)
    products=Product.objects.all().filter(author=member.id).order_by('-created_at')
    pd_jjims=Product.objects.all().filter(jjim_users=member.id).order_by('-created_at')
    context={
        "member":member,
        "products":products,
        "pd_jjims":pd_jjims,
    }
    return render(request, 'accounts/profile.html',context)

@require_POST
def follow(request, user_id):
    if request.user.is_authenticated:
        member=get_object_or_404(get_user_model(),pk=user_id)
        if request.user != member:
            if member.followers.filter(pk=request.user.pk).exists():
                member.followers.remove(request.user)
            else:
                member.followers.add(request.user)
        return redirect("accounts:profile",member.username)
    return redirect("accounts:login")