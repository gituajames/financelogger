from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from django.db.models import Count, Sum

from .models import Transaction

# forms
from finlogger.forms import UploadMpesaMessageForm



def index(request):
    recent_transactions = Transaction.objects.order_by('-date_of_transaction')[:5]

    groups = Transaction.objects.values(
        'category_of_the_transaction'
    ).annotate(totals_=Sum('amount')).order_by('totals_')

    category = []
    total = []

    for key in groups:
        print(key['category_of_the_transaction'])
        category.append(key['category_of_the_transaction'])
        total.append(key['totals_'])
        # for key1, val in key.items():
            # print(key1, ': ', val)
            # print(val)
    print(groups)

    # distill all the data for graphing
    # categorize by type of transaction
    money_in_and_out_categories = Transaction.objects.values(
        'type_of_transaction'
    ).annotate(total_money=Sum('amount')).order_by('total_money')

    labels = []
    data = []

    for key in money_in_and_out_categories:
        labels.append(key['type_of_transaction'])
        data.append(key['total_money'])

    # paid_sum = Transaction.objects.filter(type_of_transaction='paid').aggregate(
    #     sum_paid = Sum('amount'))['sum_paid']
    # data.append(paid_sum)

    # sent_sum = Transaction.objects.filter(type_of_transaction='sent').aggregate(
    #     sum_sent = Sum('amount'))['sum_sent']
    # data.append(sent_sum)

    # received_sum = Transaction.objects.filter(type_of_transaction='received').aggregate(
    #     sum_received = Sum('amount'))['sum_received']
    # data.append(received_sum)

    context = {
        'recent_transactions' : recent_transactions,
        # data
        'labels' : labels,
        'data' : data,

        # categories
        'category' : category,
        'total' : total
    }
    return render (request, 'index.html', context)


def uploadmpesamessage(request):
    if request.method == 'POST':
        form = UploadMpesaMessageForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print('valid')
            form.save()
            messages.success(request, ('msg saved'))
        else:
            messages.error(request, 'Error saving msg')
        return redirect('index')
    else:
        form = UploadMpesaMessageForm()
        context = {
            'form' : form
        }
    return render(request, 'uploadform.html', {'form' : form})
    # Create your views here.
