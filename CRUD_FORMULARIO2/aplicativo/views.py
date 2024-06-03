from django.shortcuts import render, redirect
from aplicativo.forms import AlunosForm
from aplicativo.models import Alunos

# Create your views here.
def home(request):
    data = {}
    data ['db'] = Alunos.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = AlunosForm()
    return render(request, 'forms.html', data)

def create(request):
    form = AlunosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(home)
