from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.views import generic

from .models import Post, Category, Comment, PickPost
from login.models import User
from datetime import date

from .forms import MakeGroupFrom


import jwt # for token generation
from datetime import date #현재날짜 받아오기
def main(request):
  user = "user2"
  user_id = 5
  user_posts = Post.objects.filter(username = user_id)
  # print('#############1392193###$$$$$$$$$$$$$$$$')
  # print(user_posts)
  user_today_posts = user_posts.filter(published__date = date.today())
  # print(user_today_posts)
  # print(user_posts)
  user_otherday_posts = user_posts.exclude(published__date = date.today())
  print(user_otherday_posts)
  # user_posts_titlelist = []
  # for post in user_posts:
  #   user_posts_titlelist = post.title
  # 오늘꺼인일기와 아닌일기로 분류 
  item = {
    'today_posts' : user_today_posts,
    'otherday_posts' : user_otherday_posts
  }
  return render(request, 'diary/main.html', item)

def mydiary(request):
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
  return render(request, 'diary/setting.html')

def write_diary(request):
  return render(request, 'diary/write_diary.html')

def pick(request):
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
  # 현재 유저 이름에 대한 db의 id를 가져와야함. 예시를 바탕으로, test_user1의 id는 1임
  user = "user2"
  user_id = 5
  user_posts = Post.objects.filter(username = user_id)
  user_categories = User.objects.filter(id = user_id)[0].categories.all()
  # 전체보기를 위해  user_categories_namelist의 맨 앞에 'all' 값을 하나 추가한다.
  user_categories_namelist = ["all"]
  for category in user_categories:
    user_categories_namelist.append(category.C_name)
  user_categories_idlist = []
  user_posts_idlist = []
  for post in user_posts:
    user_posts_idlist.append(post.id)
    category = Category.objects.filter(C_name = post.category)
    if(len(category) == 0):
      pass
    else:
      category_id = category[0].id
      user_categories_idlist.append(category_id)
  user_posts_idlist.reverse()

  comments = {}
  for post in user_posts:
    comments[post.id] = []
  for post in user_posts:
    tmp_comments = Comment.objects.filter(post = post)
    comments[post.id].append(tmp_comments)

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
  return render(request, 'diary/shared_diary_make.html')

def making_group(request):
  visible = request.POST['visible']
  group_name = request.POST['C_name']
  if request.method == 'POST':
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
    print("it's not POST method")
  return redirect('../groupdiary/all')

def search_group(request):
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
  if request.POST['answer'] == '네':
    group = request.POST['group']
    user = request.POST['user']
    invite_group = Category.objects.get(C_name = group)
    invited_user = User.objects.get(nick_name = user)
    invited_user.categories.add(invite_group)
  else:
    redirect("../../groupdiary/all")
  return redirect("../../groupdiary/"+group)



def test_404page(request):
  return render(request, 'diary/404page.html')
    
def test_errorpage(request):
  return render(request, 'diary/errorpage.html')

def test_unloginpage(request):
  return render(request, 'diary/unloginpage.html')