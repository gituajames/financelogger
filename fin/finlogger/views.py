from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from django.db.models import Count, Sum

from .models import Transaction

# forms
from finlogger.forms import UploadMpesaMessageForm



def index(request):
    recent_transactions = Transaction.objects.order_by('-date_of_transaction')[:5]

    # distill all the data for graphing
    # categorize by type of transaction
    labels = ['paid', 'sent', 'received']
    data = []

    paid_sum = Transaction.objects.filter(type_of_transaction='paid').aggregate(
        sum_paid = Sum('amount'))['sum_paid']
    data.append(paid_sum)

    sent_sum = Transaction.objects.filter(type_of_transaction='sent').aggregate(
        sum_sent = Sum('amount'))['sum_sent']
    data.append(sent_sum)

    received_sum = Transaction.objects.filter(type_of_transaction='received').aggregate(
        sum_received = Sum('amount'))['sum_received']
    data.append(received_sum)

    context = {
        'recent_transactions' : recent_transactions,
        # data
        'labels' : labels,
        'data' : data,
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
