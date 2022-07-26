from django.shortcuts import render

def index(request):
    return render(request, 'history/history.html')

def chat_index(request):
    return render(request, 'history/chat.html')