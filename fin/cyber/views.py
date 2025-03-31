from django.shortcuts import render, redirect
from django.http import HttpResponse

import datetime
from datetime import timezone, timedelta

from django.db.models import Count, Sum

from .models import Service

from .forms import ServiceForm

def service_upload_form(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        service = request.POST['service']
        # print(service)
        if form.is_valid():
            form.save()
            # return HttpResponse(f'saved to db thanks {service}')
            return redirect('cyber_dash_summury')
    else:
        form = ServiceForm()
        context = {
            'form': form,
            }
    return render(request, 'service_upload_form.html', context=context)

# total_received_amount = Transaction.objects.filter(
        # type_of_transaction='received'
    # ).aggregate(total_sum_received=Sum('amount'))['total_sum_received']

def cyber_dash_summury(request):

    todays_date = datetime.datetime.today()
    yesterdays_date = todays_date - timedelta(days = 1)
    print(yesterdays_date)
    # utc_time = dt.replace(tzinfo=timezone.utc)
    # utc_timestamp = utc_time.timestamp()

    todays_sum = Service.objects.filter(
        date__date = todays_date
    ).aggregate(todays_total_sum=Sum('price'))['todays_total_sum']
    print('todays totals ',todays_sum)
    
    yesterdays_sum = Service.objects.filter(
        date__date = yesterdays_date
    ).aggregate(yesterdays_total_sum=Sum('price'))['yesterdays_total_sum'] # evaluates to none
    
    total_sales = Service.objects.all().aggregate(total_sales=Sum('price'))['total_sales']
    print('yesterdays totals ',yesterdays_sum)

    # crude way to convert none to int for comparison
    if yesterdays_sum == None:
        # print(yesterdays_sum)
        yesterdays_sum = 0
    if todays_sum == None:
        todays_sum = 0

    if todays_sum > yesterdays_sum:
        print("+")
    all_services = Service.objects.filter(
        date__date = todays_date)
    context = {
        'todays_sum': todays_sum,
        'total_sales': total_sales,
        'all_data': all_services,
        'yesterdays_sum': yesterdays_sum,
    }
    return render(request, 'cyber_dash_summury.html', context=context)


# Create your views here.
