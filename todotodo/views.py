from django.shortcuts import render

# Create your views here.
def index(request, id):
    if request.method == 'GET':

        return render(request, 'todotodo/index.html')

def send_todo():
    return