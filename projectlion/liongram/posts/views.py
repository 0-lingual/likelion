from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from .models import Post

def index(request):
    post_list = Post.objects.all() # post 전체 데이터 조회
    context = {
        'post-list' : post_list,
    }
    return render(request  , 'index.html')

def post_list_view(request):
    # post_list = Post.objects.all() # post 전체 데이터 조회
    post_list = Post.objects.filter(writer=request.user) # post.writer가 현재 로그인인 것 조회
    # post_list = None 
    context = {
        'post-list' : post_list,
    }
    return render(request, 'posts/post_list.html', context)

def post_detail_view(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/post_detail.html', context)

@login_required
def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'posts/post_form.html')
    else:
        image = request.FILES.get('image')
        content = request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(
            image=image,
            content=content,
            writer=request.user 
        )
        return redirect(index)

def post_update_view(request, id):
    return render(request, 'posts/post_form.html')

def post_delete_view(request, id):
    return render(request, 'posts/post_corfirm_delete.html')

# FBV : 모든 코드를 직접 작성해야 함
# 주소값 입력 받는 방법(1) : 경로 지정 변수 사용
def url_view(request):
    print('url_view()')
    data = {'code' : '001', 'msg' : 'OK'}
    return HttpResponse('<h1>url_view<h1>')
    # return JsonResponse(data)

# 주소값 입력 받는 방법(2) : query string 사용
def url_parameter_view(request, username):
    print('url_parameter_view()')
    print(f"username : {username}")
    print(f"request.GET : {request.GET}")
    return HttpResponse(username)

# 주소값 입력 받는 방법(3) : form 사용(GET method / POST method)
def function_view(request):
    print(f"request.method : {request.method}")

    if request.method == 'GET':
        print(f"request.GET : {request.GET}")
    elif request.method == 'POST':
        print(f"request.POST : {request.POST}")
    return render(request, 'view.html')

# CBV : 함수를 상속받아 사용
# 주소값 입력 받는 방법(4) : 함수를 상속받아 사용
class class_view(ListView):
    model = Post
    template_name = 'cbv_view.html'