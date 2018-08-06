from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.views import generic

from .models import Post

from .forms import PostForm



def main(request):
  return render(request, 'diary/main.html')

def mydiary(request):
  return render(request, 'diary/my_diary_view.html')

def setting(request):
  return render(request, 'diary/setting.html')

def write_diary(request):
  return render(request, 'diary/write_diary.html')

def pick_diary(request):
  return render(request, 'diary/pick_diary_view.html')

def group_diary(request,group="all"):
  groups = ['all','group1', 'group2', 'group3']
  item = {'all_group' : groups,'selected_group' : group}
  return render(request, 'diary/shared_diary_view.html',item)

def make_group(request):
  return render(request, 'diary/shared_diary_make.html')

def search_group(request):
  searched = request.GET.get('search')
  print(searched)
  item = {'searched':searched}
  return render(request, 'diary/shared_diary_search.html',item)

class ViewMydiary(generic.ListView):  
  template_name = 'diary/view_mydiary.html'
  context_object_name = 'diary'

  # 테이블에 저장되어 있는 포스트 두개 가져온다.
  def get_queryset(self):
    return Post.objects.order_by('-published_date')[:2]





# def write_diary(request):
#     if request.method == "POST":
#       form = PostForm(request.POST)
#       if form.is_valid():
#         post = form.save(commit=False)
#         post.user = request.user
#         post.published_date = timezone.now()
#         post.save()
#       return redirect('ViewMydiary')
#     else:
#       form = PostForm()
#     return render(request, 'diary/write_diary.html', {'form': form})


def edit_diary(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('ViewMydiary')
    else:
        form = PostForm(instance=post)
    return render(request, 'diary/write_diary.html', {'post': post})
