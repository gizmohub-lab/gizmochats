from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from .models import chats
from django.contrib.auth.decorators import login_required
@login_required
def home(request, username):
    try:
        friend = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('/')

    if request.method == 'POST':
        text = request.POST.get('texts', '').strip()
        uploaded_file = request.FILES.get('file')

        image = None
        file = None
        if uploaded_file:
            if uploaded_file.content_type.startswith('image/'):
                image = uploaded_file
            else:
                file = uploaded_file

        if text or image or file:
            chats.objects.create(
                sender=request.user,
                receiver=friend,
                texts=text,
                image=image,
                file=file
            )
        return redirect('home', username=friend.username)

    messages = chats.objects.filter(
        Q(sender=request.user, receiver=friend) |
        Q(sender=friend, receiver=request.user)
    ).order_by('time')

    return render(request, 'chat_page.html', {
        'messages': messages,
        'friend': friend,
        'user': request.user
    })

def loggin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.username == 'irfuzz':
                return redirect('home', username='Ashiq')
            elif user.username == 'Ashiq':
                return redirect('home', username='irfuzz')
            else:
                return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def loggout(request):
    logout(request)
    return redirect('login')
