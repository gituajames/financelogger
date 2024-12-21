from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


from .models import Transaction
from django.db.models import Count, Sum
from django.db.models.functions import TruncDate

# forms
from finlogger.forms import UploadMpesaMessageForm

# utils
from .utils import extract_mpesa_details
from datetime import datetime



def index(request):
    recent_transactions = Transaction.objects.order_by('-date_of_mpesa_msg_modify')[:5]

    groups = Transaction.objects.exclude(type_of_transaction='received').values(
        'category_of_the_transaction'
    ).annotate(totals_=Sum('amount')).order_by('totals_')

    category = []
    total = []

    for key in groups:
        
        category.append(key['category_of_the_transaction'])
        total.append(key['totals_'])
        # for key1, val in key.items():
            # print(key1, ': ', val)
            # print(val)
    # print(groups)

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

    # sum of all transaction costs
    total_transaction_costs = Transaction.objects.aggregate(total=Sum('transaction_cost'))['total']

    # daily totals
    daily_totals = Transaction.objects.annotate(
        day=TruncDate('date_of_transaction')
    ).values('day').annotate(
        total=Sum('amount')
    ).order_by('-day')[:5]

    context = {
        'recent_transactions' : recent_transactions,
        # data
        'labels' : labels,
        'data' : data,

        # categories
        'category' : category,
        'total' : total,

        # sum of all transaction costs
        'total_transaction_costs' : total_transaction_costs,

        # daily totals
        'daily_totals' : daily_totals
    }
    return render (request, 'index.html', context)


def uploadmpesamessage(request):
    if request.method == 'POST':
        form = UploadMpesaMessageForm(request.POST)
        
        mpesa_msg = request.POST['transaction_message']
        mpesa_details = extract_mpesa_details(mpesa_msg)

        # date_of_transaction
        amount = mpesa_details['Amount']
        type_of_transaction = mpesa_details['type_of_transaction']
        if mpesa_details['type_of_transaction'] == 'received':
            name_of_recipients = mpesa_details['Sender']
            transaction_cost = 0
        else:
            name_of_recipients = mpesa_details['Recipient']
            transaction_cost = mpesa_details['Transaction Cost']
        transaction_message = mpesa_msg

        datetimestr = mpesa_details['Date']+ ' ' +mpesa_details['Time']
        
        date_format = '%d/%m/%y %H:%M %p'
        date_obj = datetime.strptime(datetimestr, date_format)

        my_transaction = Transaction(
            date_of_transaction =  date_obj,
            amount = float(amount),
            type_of_transaction = type_of_transaction,
            name_of_recipients = name_of_recipients,
            transaction_cost = transaction_cost,
            transaction_message = transaction_message,

            geolocation_of_the_transaction = request.POST['geolocation_of_the_transaction'],
            location_description = request.POST['location_description'],
            category_of_the_transaction = request.POST['category_of_the_transaction'],
            description_of_the_transaction = request.POST['description_of_the_transaction'],
        )
        my_transaction.save()
        messages.success(request, ('msg saved'))
        return redirect('index')
    else:
        form = UploadMpesaMessageForm()
        context = {
            'form' : form
        }
    return render(request, 'uploadform.html', {'form' : form})
    # Create your views here.
