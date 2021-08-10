from django.shortcuts import render
from django.core.mail import send_mail
from .models import *
# Create your views here.

def home(request):
    hokimnews = news.objects.all()
    logos = logo.objects.all()


    if request.method == 'POST':
        ism = request.POST['user']
        last = request.POST['last']
        tel = request.POST['pochta']
        local = request.POST['local']
        xabar = request.POST['xabar']
        title=ism
        msg='Sizga '+ism+'dan xabar bor'+'\nFamilyasi: '+last+'\nTelfon nomeri: '+tel+ '\n' + local + 'dan:\n'+xabar + '\nXABAR Mazmuni:\n'+xabar

        print(ism, xabar, local)
        send_mail(
            ism,
            msg,
            local,
            ['alevcoder1@gmail.com'],
            fail_silently=False,
        )
        
        print('Xabaringiz ketti')
    return render(request, 'index.html', {'news':hokimnews, 'logo': logos})
