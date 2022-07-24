from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'todotodo/index.html')

def send_todo():
    return