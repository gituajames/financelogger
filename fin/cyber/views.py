from django.shortcuts import render, redirect
from django.http import HttpResponse

import datetime
from datetime import timezone, timedelta

from django.db.models import Count, Sum

from .models import Service, Expenses

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

    unpaid_debts = Service.objects.filter(
        paid_status = False
    ).aggregate(unpaid_debts_sum=Sum('price'))['unpaid_debts_sum']
    print('depts ',unpaid_debts)
    
    yesterdays_sum = Service.objects.filter(
        date__date = yesterdays_date
    ).aggregate(yesterdays_total_sum=Sum('price'))['yesterdays_total_sum'] # evaluates to none
    
    total_sales = Service.objects.all().aggregate(total_sales=Sum('price'))['total_sales']
    print('yesterdays totals ',yesterdays_sum)

    # sum of all the expenses
    total_expenses = Expenses.objects.all().aggregate(total_expenses=Sum('price'))['total_expenses']

    # crude way to convert none to int for comparison
    if yesterdays_sum == None:
        # print(yesterdays_sum)
        yesterdays_sum = 0
    if todays_sum == None:
        todays_sum = 0

    percentage_change = abs((yesterdays_sum - todays_sum))
    # all sercices for the day
    all_services = Service.objects.filter(
        date__date = todays_date)

    # last 30 days daily sum for graphing
    last_30_days = datetime.datetime.today() - timedelta(30)
    report = Service.objects.filter(
        date__gte=last_30_days).extra(
            {'day':'date(date)'}
        ).values('day').annotate(count=Sum('price'))

    date_labels = []
    date_sums = []

    for key in report:
        print(key['day'], ': ', key['count'])
        date_labels.append(key['day'])
        date_sums.append(key['count'])

    # print(report)
    context = {
        'todays_sum': todays_sum,
        'yesterdays_sum': yesterdays_sum,

        # percentage change
        'percentage_change' : percentage_change,
        'total_sales': total_sales,
        # all services for the day to be in a table
        'all_data': all_services,
        # daily sums for graphing
        'date_labels': date_labels,
        'date_sums': date_sums,

        # unpaid debt sums
        'unpaid_debts': unpaid_debts,

        # expenses
        'total_expenses': total_expenses,
        
    }
    return render(request, 'cyber_dash_summury.html', context=context)


# Create your views here.
