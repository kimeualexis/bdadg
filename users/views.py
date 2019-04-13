from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Profile
from django.db.models import Q
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def index(request):
    profiles = Profile.objects.all()
    query = request.GET.get("q")
    if query:
        profiles = profiles.filter(
            Q(fname__icontains=query) |
            Q(sname__icontains=query)
        ).distinct()
        return render(request, 'users/index.html', {
            'profiles': profiles,
        })
    return render(request, 'users/index.html', {'profiles': profiles})


class ProfileCreateView(CreateView):
    model = Profile
    fields = [
        'fname', 'sname', 'cover', 'area_raised', 'bio',
        'primary_sch', 'high_sch', 'campus', 'course',
        'hobby', 'year_joined_library', 'profession'
    ]


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = [
        'fname', 'sname', 'area_raised', 'cover', 'bio',
        'primary_sch', 'high_sch', 'campus', 'course',
        'hobby', 'year_joined_library', 'profession'
    ]


class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = '/'


def signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = form.save(commit=False)
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('users:users-index')
    return render(request, 'registration/signup.html', {'form': form})

