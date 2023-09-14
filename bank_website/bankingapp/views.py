
# Create your views here.
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404,redirect
from .forms import PersonCreationForm
from .models import District,Branch,Person

# Create your views here.
def index(request):
    return render(request,"index.html")


def new(request):
    return render(request,'new_page.html')

def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bankingapp:submit')
    return render(request, 'submission_form.html', {'form': form})

def load_areas(request):
    district_id = request.GET.get('district_id')
    cities = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'area_dropdown_list.html', {'cities': cities})

def submit(request):
    return render(request,"submit.html")