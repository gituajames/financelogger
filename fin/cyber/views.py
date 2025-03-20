from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Service

from .forms import ServiceForm

def index(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        service = request.POST['service']
        print(service)
        if form.is_valid():
            form.save()
            # return HttpResponse(f'saved to db thanks {service}')
            return redirect('home')
    else:
        form = ServiceForm()
        context = {
            'form': form,
            }
    return render(request, 'cyber.html', context=context)



def home(request):
    all_services = Service.objects.order_by('-date')[:8]
    context = {
        'all_data': all_services
    }
    return render(request, 'home.html', context=context)


# Create your views here.
