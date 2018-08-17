from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from django.views import generic

from .models import Post, Category, Comment, PickPost
from login.models import User
from datetime import date

from .forms import MakeGroupFrom, PostForm


import jwt # for token generation
from datetime import date #현재날짜 받아오기
import datetime
#from django.core.files.uploadhandler import FileUploadHandler

  
def main(request):
  try: # 로그인했을때만 접근가능하도록 처리
    user = request.session['user_name']
  except:
    return redirect('../unloginpage')
  user = "user2"
  user_id = 5
  user_posts = Post.objects.filter(username = user_id)
  # print('#############1392193###$$$$$$$$$$$$$$$$')
  # print(user_posts)
  user_today_posts = user_posts.filter(published__date = date.today())
  # print(user_today_posts)
  # print(user_posts)
  user_otherday_posts = user_posts.exclude(published__date = date.today())
  # print(user_otherday_posts)
  # user_posts_titlelist = []
  # for post in user_posts:
  #   user_posts_titlelist = post.title
  # 오늘꺼인일기와 아닌일기로 분류 

  item = {
    'today_posts' : user_today_posts,
    'otherday_posts' : user_otherday_posts
  }

  # login message를 위한 로직
  try:
    message = request.session['login_message']
    del request.session['login_message']
    item['message'] = message
  except:
    pass
  try:
    message = request.session['logout_message']
    del request.session['logout_message']
    item['message'] = message
  except:
    pass
  return render(request, 'diary/main.html', item)

# 내 일기장에 일기들을 불러와주는 함수
def mydiary(request):
  try: # 로그인했을때만 접근가능하도록 처리
    user = request.session['user_name']
  except:
    return redirect('../../unloginpage')
  user_id = 1 # 규란이가 성공하면 2가 아니라 현재 접속자를 불러온다. id가 될 지 아닌지는 아직 미정
  user_posts = Post.objects.filter(username = user_id)
  comments = {}
  for post in user_posts:
    comments[post.id] = []
    tmp_comments = Comment.objects.filter(post=post)
    comments[post.id].append(tmp_comments)
  return render(request, 'diary/my_diary_view.html', {'posts':user_posts, 'comments':comments})

def mydiary_delete(request):
  user_id = 1
  post_id = request.POST['post_id']
  user = User.objects.get(id = user_id)
  user_post = Post.objects.filter(username = user)
  selected_user_post = user_post.get(id = post_id)
  selected_user_post.delete()
  return redirect('../main/mydiary/')

def setting(request):
  try: # 로그인했을때만 접근가능하도록 처리
    user = request.session['user_name']
  except:
    return redirect('../../unloginpage')
  return render(request, 'diary/setting.html')

def edit_diary(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user_id = 2
    if request.method == "POST":
      original_post = Post.objects.get(id = request.POST['post_id'])
      original_post.title = request.POST['title']
      # original_post.category = Category.objects.get(C_name = request.POST['category'])
      original_post.emotion = request.POST['emotion']
      original_post.weather = request.POST['weather']
      if request.POST['photo'] == "": # 사진을 수정하지 않으면 걍 내비둔다
        pass
      else: # 새로운 사진을 첨부했으면, 기존의 사진을 지우고 새로 첨부한 사진을 db에 입력
        original_post.photo.delete(save=False)
        original_post.photo = request.FILES['photo'] 
      original_post.content = request.POST['content']
      original_post.save()
      return redirect('main')

    else:
        form = PostForm(instance=post)
    return render(request, 'diary/edit_diary.html', {'form': form, 'post': post})

def write_diary(request):
  try: # 로그인했을때만 접근가능하도록 처리
    user = request.session['user_name']
  except:
    return redirect('../../unloginpage')
  if request.method == "POST":
    form = PostForm(request.POST,request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.username = User.objects.get(id =2)
      post.category = Category.objects.get(id =1)
      post.save()
      return redirect('main')
  else:
    form = PostForm()
  return render(request, 'diary/write_diary.html')

def pick(request):
  if request.method == "POST":
    return redirect('../../errorpage')
  user_id = 1
  post_id = request.POST['post_id']
  user = User.objects.get(id = user_id)
  pick_post = Post.objects.get(id = post_id)
  try:
    PickPost_obejct = PickPost.objects.get(username = user)
    PickPost_obejct.pick_posts.add(pick_post)
  except: 
    PickPost_obejct = PickPost.objects.create(username = user)
    print("##### except")
    PickPost_obejct.pick_posts.add(pick_post)
    PickPost_obejct.save()
  return redirect('../main/groupdiary/all')

def pick_diary(request):
  try: # 로그인했을때만 접근가능하도록 처리
    user = request.session['user_name']
  except:
    return redirect('../../unloginpage')
  user = "test_user1"
  user_id = 1
  try:
    user_posts = PickPost.objects.get(username = user_id).pick_posts.all()
  except:
    return redirect('../')
  comments = {}
  for post in user_posts:
    comments[post.id] = []
    tmp_comments = Comment.objects.filter(post=post)
    comments[post.id].append(tmp_comments)
  item = {
    'pickposts' : user_posts,
     'comments' : comments
  }
  return render(request, 'diary/pick_diary_view.html',item)
  
def remove(request):
  user_id = 1
  post_id = request.POST['remove_id']
  # user = PickPost.objects.get(id = user_id)
  post = Post.objects.get(id = post_id)
  user_pickposts = PickPost.objects.get(username = user_id).pick_posts
  user_pickposts.remove(post)
  return redirect('../main/pickdiary/')

def comment_delete(request):
  user_id = 1
  post_id = request.POST['comment_id']
  user_comment = Comment.objects.filter(author = user_id)
  selected_user_comment = user_comment.get(id = post_id)
  selected_user_comment.delete()
  return redirect('../main/groupdiary/all')




def group_diary(request,group="all"):
  try: # 로그인했을때만 접근가능하도록 처리
    user = request.session['user_name']
  except:
    return redirect('../../unloginpage')
  # 현재 유저 이름에 대한 db의 id를 가져와야함. 예시를 바탕으로, test_user1의 id는 1임
  user = "test_user1"
  user_id = 2
  user_posts = Post.objects.filter(username = user_id) 
  # filter 를 통해서 어떤 유저 아이디에 해당하는 post들을 다 가져와서 user_posts 에 저장한다. 외래키 이기 때문에 username으로 해도 id로 탐색.
  user_categories = User.objects.filter(id = user_id)[0].categories.all()
   # 해당하는 id 에 맞는 유저를 찾아서 [0]을 붙인 이유가 뭐지 그리고 모든 categories를 변수에 저장한다.
  # 전체보기를 위해  user_categories_namelist의 맨 앞에 'all' 값을 하나 추가한다.
  user_categories_namelist = ["all"]
  for category in user_categories: # user_categories 안에 있는 카테고리들을 반복한다.
    user_categories_namelist.append(category.C_name) # 각 카테고리의 이름들을 namelist 변수에 담아준더ㅏ,
  user_categories_idlist = [] # 카테고리의 id 리스트와
  user_posts_idlist = [] # post의 id 리스트를 만들어주고
  for post in user_posts: # 특정 유저의 모든 post를 돌면서 
    user_posts_idlist.append(post.id) # 그 아이디 값을 변수에 담아준다.
    category = Category.objects.filter(C_name = post.category) # post의 카테고리가 원하는 카테고리의 이름과 같은 것들만 category 변수에 넣는다.
    if(len(category) == 0): # categorty 변수에 아무것도 없으면 
      pass # 그냥 넘어가고ㅓ
    else: # 뭐라도 있으면 
      category_id = category[0].id # 카테고리 안에 첫번째 post의 id 를 변수에 저장
      user_categories_idlist.append(category_id) # 그 id 를 idlist 변수에 넣는다.
  user_posts_idlist.reverse() # idlist를 뒤집어준다.

  comments = {} # 빈 딕셔너리를 선언
  for post in user_posts: # post들을 반복하며
    comments[post.id] = [] # 각 id 를 key로 가지는 빈 리스트 [] 를 value로 가짐
    tmp_comments = Comment.objects.filter(post = post) # post에 해당하는 comment를 다 가져와서 저장하고
    comments[post.id].append(tmp_comments) # 그 리스트에 넣어준다.
  #group이용해서 db에서 해당 group이름을 가진 교환일기장의 visible값을 아래 변수에 저장
  if group != 'all':
    category_for_link = Category.objects.filter(C_name = group)[0]
    visible = category_for_link.visible
    link = category_for_link.link
  else:
    visible = 1
    link = ""
    
  item = {
    'categories_namelist' : user_categories_namelist,
    'categories_idlist' : user_categories_idlist,
    'selected_group' : group,
    'posts':user_posts,
    'posts_idlist':user_posts_idlist,
    'comments': comments,
    'selected_group_visible': visible,
    'link': link
    }
  return render(request, 'diary/shared_diary_view.html',item)

def make_group(request):
  try: # 로그인했을때만 접근가능하도록 처리
    user = request.session['user_name']
  except:
    return redirect('../../unloginpage')
  return render(request, 'diary/shared_diary_make.html')

def making_group(request):
  try: # 로그인했을때만 접근가능하도록 처리
    user = request.session['user_name']
  except:
    return redirect('../../../unloginpage')
  if request.method == 'POST':
    visible = request.POST['visible']
    group_name = request.POST['C_name']
    form = MakeGroupFrom(request.POST)
    if form.is_valid():
      category = form.save(commit=False)
      if visible == 1:
        category.link = "http://localhost:8000/main/search/?search="+group_name
      else:
        token = jwt.encode({'group':group_name},'tokenpw',algorithm='HS256').decode('utf-8')
        link = "http://localhost:8000/main/invite/check/"+token
        category.link = link
      category.save()
  else:
    return redirect('../../../errorpage')
  return redirect('../groupdiary/all')

def search_group(request):
  try: # 로그인했을때만 접근가능하도록 처리
    user = request.session['user_name']
  except:
    return redirect('../../unloginpage')
  # user 가정
  user_id = 1
  user_categories = User.objects.get(id = user_id).categories.all() # user가 이미 속한 교환일기장

  search_word = request.GET.get('search')
  # C_name 에서 searched 를 가진 요소들을 찾아서 반환한다.
  searched_categories = Category.objects.filter(C_name__icontains=search_word) # 검색어를 포함한 제목의 모든 교환일기장
  
  not_entered_categories = list(set(searched_categories) - set(user_categories))

  item = {
    'search_word': search_word,
    'searched_categories': not_entered_categories
    }
  return render(request, 'diary/shared_diary_search.html',item)

def invite_check(request,token=""):
  try: # 로그인했을때만 접근가능하도록 처리
    user = request.session['user_name']
  except:
    return redirect('../../unloginpage')
  user = 'user2'
  if token == "":
    pass # return 잘못된 접근
  else:
    decoded = jwt.decode(token,'tokenpw',algorithms=['HS256'])
    group = decoded['group']
  
  item = {
    'group': group,
    'user': user
  }
  return render(request, 'diary/invite_check.html',item)


def join_group(request,group='',user=''):
  if request.method == "GET":
      return redirect('../../../errorpage')
  if request.POST['answer'] == '네':
    group = request.POST['group']
    user = request.POST['user']
    invite_group = Category.objects.get(C_name = group)
    invited_user = User.objects.get(nick_name = user)
    invited_user.categories.add(invite_group)
  else:
    redirect("../../groupdiary/all")
  return redirect("../../groupdiary/"+group)


