from django.shortcuts import render, redirect
from django.http import HttpResponse

import datetime
from datetime import timezone, timedelta

from django.db.models import Count, Sum

from .models import Service, Expenses, Product

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
    last_30_days = (datetime.datetime.now() - timedelta(datetime.datetime.now().day)) + timedelta(1)

    # sum of the day
    todays_sum = Service.objects.filter(
        date__date = todays_date
    ).aggregate(todays_total_sum=Sum('price'))['todays_total_sum']

    # sum of previous date
    yesterdays_sum = Service.objects.filter(
        date__date = yesterdays_date
    ).aggregate(yesterdays_total_sum=Sum('price'))['yesterdays_total_sum'] # evaluates to none
    
    # crude way to convert none to int for comparison
    if yesterdays_sum == None:
        # print(yesterdays_sum)
        yesterdays_sum = 0
    if todays_sum == None:
        todays_sum = 0

    # previous day and current difference # should turn in to a percentage
    # but 1st solve division by 0 error
    # in cases where previous sales was 0 
    percentage_change = abs((yesterdays_sum - todays_sum))


    # all sercices for the day
    all_services = Service.objects.filter(
        date__date = todays_date)
    
    # monthly total sales
    monthly_total_sales = Service.objects.filter(
        date__gte = last_30_days
    ).aggregate(sale=Sum('price'))['sale']
    # print('month sales', monthly_total_sales)

    # total sales 
    total_sales = Service.objects.all().aggregate(total_sales=Sum('price'))['total_sales']

    # sum of all the expenses
    total_expenses = Expenses.objects.all().aggregate(total_expenses=Sum('price'))['total_expenses']

    # monthly total expenses
    monthly_total_expenses = Expenses.objects.filter(
        date_created__gte = last_30_days
    ).aggregate(monthly_expenses=Sum('price'))['monthly_expenses']

    # revenue less expenses
    if monthly_total_sales == None:
        monthly_total_sales = 0
    if monthly_total_expenses == None:
        monthly_total_expenses = 0
    monthly_revenue = monthly_total_sales - monthly_total_expenses

    # sum of all unpaid for sales and services
    unpaid_debts = Service.objects.filter(
        paid_status = False
    ).aggregate(unpaid_debts_sum=Sum('price'))['unpaid_debts_sum']


    # last 30 days daily sum for graphing
    # monthly summury
    # last_30_days = (datetime.datetime.now() - timedelta(datetime.datetime.now().day)) + timedelta(1)
    report = Service.objects.filter(
        date__gte=last_30_days).extra(
            {'day':'date(date)'}
        ).values('day').annotate(count=Sum('price'))

    date_labels = []
    date_sums = []

    for key in report:
        # print(key['day'], ': ', key['count'])
        date_labels.append(key['day'])
        date_sums.append(key['count'])


    context = {
        'todays_sum': todays_sum,
        'yesterdays_sum': yesterdays_sum,

        # percentage change
        'percentage_change' : percentage_change,
        'total_sales': monthly_total_sales,
        # all services for the day to be in a table
        'all_data': all_services,
        
        # daily sums for graphing
        'date_labels': date_labels,
        'date_sums': date_sums,

        # unpaid debt sums
        'unpaid_debts': unpaid_debts,

        # monthly revenue
        'monthly_revenue': monthly_revenue,
        'monthly_expenses': monthly_total_expenses,

        # expenses
        'total_expenses': total_expenses,
        
    }
    return render(request, 'cyber_dash_summury.html', context=context)


def inventory(request):
    page_title = "cyber inventory"
    all_products = Product.objects.all()

    context = {
        'all_products': all_products,
        'page_title': page_title,
    }
    return render(request, 'inventory.html', context=context)

def tables(request):
    todays_services = Service.objects.filter(
        date__date = todays_date)

    context = {
        'todays_services' : todays_services
    }
    return render(request, 'tables.html', context=context)