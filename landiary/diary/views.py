from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.views import generic

from .models import Post, Category, Comment
from login.models import User
from .forms import PostForm
import datetime
#from django.core.files.uploadhandler import FileUploadHandler

def main(request):
  return render(request, 'diary/main.html')

# 내 일기장에 일기들을 불러와주는 함수
def mydiary(request):
  user_id = 2 # 규란이가 성공하면 2가 아니라 현재 접속자를 불러온다. id가 될 지 아닌지는 아직 미정
  user_posts = Post.objects.filter(username = user_id)
  comments = {}
  for post in user_posts:
    comments[post.id] = []
    tmp_comments = Comment.objects.filter(post=post)
    comments[post.id].append(tmp_comments)
  
  return render(request, 'diary/my_diary_view.html', {'posts':user_posts, 'comments':comments})

def post_delete(request):
  post_id = request.GET('post_id')
  post.delete()
  return redirect('mydiary')



def setting(request):
  return render(request, 'diary/setting.html')

# def write_diary(request):
#   return render(request, 'diary/write_diary.html')
'''
def edit_diary(request):
  user_id = 2
  print("############", request.POST['post_id'])
  post_id = request.POST['post_id']
  print("##########", post_id)
  post = Post.objects.get(id = post_id)
  
  if request.method == "POST":
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      post = form.save(commit = False)
      post.uername = User.objects.get(id=2)
      post.category = Category.object.get(id = 1)
      post.save()
      return redirect('../main/mydiary')
  else:
    form = PostForm(instance = post)
  return render(request, 'diary/edit_diary.html')
'''
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
        # form = PostForm(request.POST, instance=post)
        # if form.is_valid():
        #     post = form.save(commit=False)
        #     post.uername = User.objects.get(id=user_id)
        #     post.category = Category.objects.get(id = post.id)
        #     post.photo = 
        #     post.save()
        #     return redirect('main')

    else:
        form = PostForm(instance=post)
    return render(request, 'diary/edit_diary.html', {'form': form, 'post': post})


'''
def edit_diary(request):
  post_id = request.POST['edit_id']
  post = get_object_or_404(Post, id=post_id)
  if request.method == "POST":
    form = PostForm(request.POST, instance = post)
    if form.is_valid():
      post = form.save(commit=False)
      post.uername = User.objects.get(id=2)
      post.category = Category.object.get(id = 1)
      post.save()
      return redirect('mydiary')
    else:
      form = PostForm(instance = post)
    return render(request, 'diary/edit_diary.html')
'''


'''
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
'''



def write_diary(request):
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


def pick_diary(request):
  return render(request, 'diary/pick_diary_view.html')



def group_diary(request,group="all"):
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
