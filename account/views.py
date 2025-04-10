from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from chats.models import chats
@login_required
def account_page(request):
    user = request.user
    messages_sent = chats.objects.filter(sender=user).count()
    messages_received = chats.objects.filter(receiver=user).count()

    return render(request, 'account_page.html', {
        'user': user,
        'messages_sent': messages_sent,
        'messages_received': messages_received,
    })

# Create your views here.


