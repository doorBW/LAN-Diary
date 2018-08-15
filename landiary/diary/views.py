from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.views import generic

from .models import Post, Category, Comment, PickPost
from login.models import User
from datetime import date


def mydiary_select(request):
  user_id = 2
  return render(request, 'diary/my_diary_view.html')

def main(request):
  # user = "user2"
  user_id = 2
  user_posts = Post.objects.filter(username = user_id)
  user_today_posts = user_posts.filter(published__date = date.today())
  user_otherday_posts = user_posts.exclude(published__date = date.today())
  item = {
  'today_post': user_today_posts,
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
  user = "user1"
  user_id = 1
  user_posts = PickPost.objects.get(username = user_id).pick_posts.all()
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
  user = "test_user1"
  user_id = 3
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
  
  item = {
    'categories_namelist' : user_categories_namelist,
    'categories_idlist' : user_categories_idlist,
    'selected_group' : group,
    'posts':user_posts,
    'posts_idlist':user_posts_idlist,
    'comments': comments
    }
  return render(request, 'diary/shared_diary_view.html',item)

def make_group(request):
  return render(request, 'diary/shared_diary_make.html')

def search_group(request):
  searched = request.GET.get('search')
  print(searched)
  item = {'searched':searched}
  return render(request, 'diary/shared_diary_search.html',item)
