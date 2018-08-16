from django.shortcuts import render, redirect, HttpResponse
import requests, json
from urllib.parse import urlencode
from .models import User
# Create your views here.
def login(request):
    try:
        message = request.session['logout_message']
        del request.session['logout_message']
        item = {
            'message': message
        }
        return render(request,'login/login_view.html',item)
    except:
        return render(request,'login/login_view.html')
    

def loging(request):
    # if request.method == 'GET'
    authorize_code = request.GET.get('code') # 인증 코드 받기
    # access token, refresh token을 위한 post 요청 body 및 header
    authorize_code.replace(" ","") # 공백제거
    body = {
        "grant_type": "authorization_code",
        "client_id": "1d894462dd40831cc8d2537ee51addfc",
        "redirect_uri": "http://localhost:8000/loging",
        "code": authorize_code,
    }
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    res = requests.post('https://kauth.kakao.com/oauth/token', data=urlencode(body), headers=headers)
    content = res.json()
    user_actoken = content['access_token']
    user_retoken = content['refresh_token']
    request.session['user_actoken'] = user_actoken # session에 access token 저장
    # access token, refresh token 받기 완료
    # 카카오톡 프로필 받기
    headers = {
        'Authorization': 'Bearer ' + user_actoken,
        'Content-type': 'application/x-www-form-urlencoded'
    }
    res = requests.get('https://kapi.kakao.com/v1/user/me', headers=headers)
    content = res.json()['properties']
    user_nickname = content['nickname']
    user_profile_image = content['profile_image']
    request.session['user_name'] = user_nickname
    request.session['user_image'] = user_profile_image
    try:
        user = User.objects.get(nick_name = user_nickname)
        request.session['login_message'] = user_nickname+"님 또 찾아주셔서 감사합니다."
    except:
        user = User.objects.create(nick_name = user_nickname)
        request.session['login_message'] = user_nickname+"님의 첫번째 로그인을 환영합니다 :-)"
    return redirect('../main')

def logout(request):
    print("logout")
    headers = {
        'Authorization': 'Bearer ' + request.session['user_actoken']
    }
    res = requests.post('https://kapi.kakao.com/v1/user/logout', headers=headers)
    status = res.status_code
    content = res.json()
    
    if status == 200:
        try:
            print("정상적인 로그아웃",content['id'])
            request.session['logout_message'] = request.session['user_name']+"님 정상적으로 로그아웃 되셨습니다."
            response = HttpResponse("Cookies Cleared")
            response.delete_cookie('sessionid')
            print('@@@',request.COOKIES)
            del request.session['user_actoken']
            del request.session['user_name']
            del request.session['user_image']
        except:
            print("로그아웃 실패")
            request.session['logout_message'] = request.session['user_name']+"님 로그아웃에 실패하였습니다. 다시 시도해주세요 :-("
            return redirect('./main')
    else: 
        print("로그아웃 실패")
        request.session['logout_message'] = request.session['user_name']+"님 로그아웃에 실패하였습니다. 다시 시도해주세요 :-("
        return redirect('./main')
    
    return redirect('../')