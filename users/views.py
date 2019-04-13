from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Profile
from django.db.models import Q
from .forms import UserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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


class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    fields = [
        'fname', 'sname', 'cover', 'area_raised', 'bio',
        'primary_sch', 'high_sch', 'campus', 'course',
        'hobby', 'year_joined_library', 'profession'
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = [
        'fname', 'sname', 'area_raised', 'cover', 'bio',
        'primary_sch', 'high_sch', 'campus', 'course',
        'hobby', 'year_joined_library', 'profession'
    ]

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    success_url = '/'

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False


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

