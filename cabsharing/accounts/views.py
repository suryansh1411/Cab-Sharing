from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from .forms import UserProfileForm, UserForm
from django.views.generic import DetailView, DeleteView, UpdateView 
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def SignupView(request):
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileForm(data=request.POST)

        if(user_form.is_valid() and profile_form.is_valid()):
            user=user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            username=user_form.cleaned_data['username']
            password=user_form.cleaned_data['password']

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic'] #may try if else to attach default

            profile.save()

            user=authenticate(username=username , password=password)
            login(request, user)
            return redirect('index')
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form=UserForm()
        profile_form=UserProfileForm()
    return render(request, 'accounts/signup.html', {'user_form':user_form,'profile_form':profile_form})


class UserDetailView(LoginRequiredMixin, DetailView):
    model=User
    template_name='accounts/user_detail.html'

# class UserDeleteView(LoginRequiredMixin, DeleteView):
#     model=User
#     success_url=reverse_lazy('index')



class UserUpdateView(LoginRequiredMixin, UpdateView):
    model=User
    fields=['username','email']
    success_url=reverse_lazy('index')
    # need to change it to detail
    # extra_context={'userprofile': UserProfileForm()}

    # def get_success_url(self):
    #     return reverse('accounts:user_detail', kwargs={'pk':self.user.pk})

class UserProfileUpateView(LoginRequiredMixin, UpdateView):
    model=UserProfile
    fields=['profile_pic']
