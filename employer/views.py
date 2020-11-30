from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
        ListView, 
        DetailView, 
        CreateView,
        UpdateView,
        DeleteView
    )
from .models import Jobs
from .forms import JobForm

# Create your views here.
def home(request):
    context = {
        'jobs': Jobs.objects.all()
    }
    return render(request, 'employer/home.html', context)


class JobsListView(ListView):
    model = Jobs
    template_name = 'employer/home.html'
    context_object_name = 'jobs'
    ordeing = ['-date_posted']

class JobsDetailView(DetailView):
    model = Jobs

class JobsCreateView(LoginRequiredMixin, CreateView):
    model = Jobs
    #fields = ['companyname', 'jobplace', 'jobprofile', 'experience', 'jobdescription','contact','email','applyHere']
    form_class = JobForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class JobsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Jobs
    # fields = ['companyname', 'jobplace', 'jobprofile', 'experience', 'jobdescription','contact','email','applyHere']
    form_class = JobForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        jobs = self.get_object()
        if self.request.user == jobs.author:
            return True
        return False

class JobsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Jobs
    success_url = '/'

    def test_func(self):
        jobs = self.get_object()
        if self.request.user == jobs.author:
            return True
        return False


def about(request):
    return render(request, 'employer/about.html', {'title': 'About'})