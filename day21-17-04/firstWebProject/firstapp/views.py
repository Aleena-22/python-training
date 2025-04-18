from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def converter_view(request):
    if request.method == 'POST':
        amount = float(request.POST.get('amount', 0))
        currency = request.POST.get('currency')
        converted_amount = None

        # conversion rates
        conversion_rate_inr_to_usd = 0.012
        conversion_rate_usd_to_inr = 82.50

        if currency == 'INR':
            converted_amount = amount * conversion_rate_inr_to_usd
        elif currency == 'USD':
            converted_amount = amount * conversion_rate_usd_to_inr

        return render(request, 'firstapp/converter.html', {
            'converted_amount': round(converted_amount, 2),
            'currency': currency,
            'original_amount': amount,
        })

    return render(request, 'firstapp/converter.html')

def root_view(request):
    return redirect('/converter/') 

def timer_view(request):
    return render(request, 'firstapp/timer.html')

def timer_req(request):
    return redirect('/timer/') 
