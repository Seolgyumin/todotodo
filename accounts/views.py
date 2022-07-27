import os
import jwt
import requests
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from accounts.models import KakaoUser

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
    user_info = requests.get('https://kapi.kakao.com/v2/user/me', headers={"Authorization": f'Bearer ${access_token}'}).json()

    print(user_info['id'])

    if KakaoUser.objects.filter(id=user_info['id']).exists():  # 기존에 소셜로그인을 했었는지 확인
        user = KakaoUser.objects.get(id=user_info['id'])
        encoded_jwt = jwt.encode({'id': user.id}, os.environ.get('DJANGO_KEY'), algorithm='HS256')  # jwt토큰 발행
    else:
        user = KakaoUser(
            id=user_info['id'],
            name=user_info['properties']['nickname'],
            email=user_info['properties'].get('email', None)
        )
        user.save()
        encoded_jwt = jwt.encode({'id': user.id}, os.environ.get('DJANGO_KEY'), algorithm='HS256')  # jwt토큰 발행
    return render(request, 'accounts/signin.html', {'user': user, 'jwt_token': encoded_jwt})

def congrats(request):
    return render(request, 'accounts/congrats.html')

def login():
    return
