import os
import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
def index():
    return render('todotodo/index.html')


def kakao_login(request):
    client_id = os.environ.get('KAKAO_REST_API_KEY')
    redirect_uri = 'http://localhost:8000/accounts/signin/kakao/callback/'
    kakao_auth_api = 'https://kauth.kakao.com/oauth/authorize?'
    return redirect(f'{kakao_auth_api}client_id={client_id}&redirect_uri={redirect_uri}&response_type=code')

def kakao_callback(request):
    auth_code = request.GET.get('code')
    kakao_token_api = 'https://kauth.kakao.com/oauth/token'
    data = {
        'grant_type': 'authorization_code',
        'client_id': os.environ.get('KAKAO_REST_API_KEY'),
        'redirection_uri': 'http://localhost:8000/accounts/signin/kakao/callback',
        'code': auth_code
    }

    token_response = requests.post(kakao_token_api, data=data)
    access_token = token_response.json().get('access_token')
    user_info_response = requests.get('https://kapi.kakao.com/v2/user/me', headers={"Authorization": f'Bearer ${access_token}'})

    return redirect('/accounts/signin')

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/signin.html')
    else:
        return render(request, 'accounts/signin.html')

def congrats(request):
    return render(request, 'accounts/congrats.html')

def login():
    return
