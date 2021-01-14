from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from social_core.exceptions import AuthAlreadyAssociated

from django.contrib.auth import logout
from django.shortcuts import redirect

def login(request):
    return render(request, 'youtube/login.html')
    # 유효성 검증에 성공할 경우
    if login_form.is_valid():
        # form으로부터 username, password값을 가져옴
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']

        # 가져온 username과 password에 해당하는 User가 있는지 판단한다
        # 존재할경우 user변수에는 User인스턴스가 할당되며,
        # 존재하지 않으면 None이 할당된다
        user = authenticate(
            username=username,
            password=password
        )
        # 인증에 성공했을 경우
        if user:
            # Django의 auth앱에서 제공하는 login함수를 실행해 앞으로의 요청/응답에 세션을 유지한다
            django_login(request, user)
            # Post목록 화면으로 이동
            return redirect('post:post_list')
        # 인증에 실패하면 login_form에 non_field_error를 추가한다
        login_form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다')
    else:
        login_form = LoginForm()
    context = {
        'login_form': login_form,
    }
    return render(request, 'youtube/index.html', {'name': index,})

def logout_request(request):
    logout(request)
    return render(request, 'youtube/index.html', {'name': index,})

def who(request):
    return render(request, 'youtube/who.html')

def index(request):
    return render(request, 'youtube/index.html')


def video(request):
    return render(request, 'youtube/video.html')


def top(request):
    return render(request, 'youtube/top.html')


def mychannel(request):
    return render(request, 'youtube/mychannel.html')


def search(request):
    return render(request, 'youtube/search.html')

    
