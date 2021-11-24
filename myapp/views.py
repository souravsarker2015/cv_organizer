from django.shortcuts import render, redirect
from django.views import View

from .forms import CVForms
from .models import CV


class HomeView(View):
    def get(self, request):
        form = CVForms()
        candidates = CV.objects.all()
        return render(request, 'myapp/home.html', {'candidates': candidates, 'form': form})

    def post(self, request):
        form = CVForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')


class CandidateView(View):
    def get(self, request, pk):
        print(pk)
        candidate = CV.objects.get(pk=pk)
        return render(request, 'myapp/candidate.html', {'candidate': candidate})
