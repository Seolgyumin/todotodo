import os
from django.shortcuts import render, redirect

# Create your views here.
def index():
    return render('todotodo/index.html')


def kakao_login(request):
    client_id = os.environ.get('KAKAO_REST_API_KEY')
    redirect_uri = 'http://localhost:8000/accounts/signin/kakao/callback/'
    kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?'
    return redirect(f'{kakao_auth_api}client_id={client_id}&redirect_uri={redirect_uri}&response_type=code')


def signin(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/signin.html')
    else:
        return render(request, 'accounts/signin.html')

def login():
    return
