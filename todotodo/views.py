from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'GET':

        return render(request, 'todotodo/index.html')

def home(request):
    return

def send_todo():
    return