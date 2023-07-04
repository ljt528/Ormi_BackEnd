from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment, HashTag
from .forms import PostForm, CommentForm, HashTagForm
from django.urls import reverse_lazy, reverse

# Create your views here.
# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('Index page GET')
#     # 나머지 요청
#     # 에러, 예외처리
#     return HttpResponse('No!!!')

### Post
class Index(View):
    def get(self, request):
        # return HttpResponse('Index page GET class')

        # 데이터베이스에 접근해서 값을 가져와야 합니다.
        # 게시판에 글들을 보여줘야하기 때문에 데이터베이스에서 "값 조회"
        # MyModel.objects.all()
        post_objs = Post.objects.all()
        # context = 데이터베이스에서 가져온 값
        context = {
            "posts" : post_objs  #None
        }
        # print(post_objs) QuerySet<[post 1, 2, 3, 4, 5]>
        return render(request, 'blog/post_list.html', context) # 렌더의 정석적인 3가지 인자 값
    



'''
class Index(LoginRequiredMixin, View):
    def get(self, request):
        # Post - User 연결 (Foreignkey)
        # User를 이용해서 Post를 가지고 온다.
        posts = Post.objects.filter(writer=request.user)
        context = {
        "posts": posts
        }
        return render(request, 'blog/post_list.html', context)
'''

# write
# post - form
# 글 작성 화면
# def write(request):
#     if request.method == 'POST':
#         # form 확인
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save()
#             return redirect('blog:list')

#     form = PostForm()
#     return render(request, 'blog/write.html', { 'form': form })


# Django 자체의 클래스 뷰 기능도 강력, 편리
# model, template_name, context_object_name,
# paginate_by, form_class, form_valid(), get_queryset()
# django.views.generic -> ListView
# class List(ListView):
#     model = Post #모델
#     template_name = 'blog/post_list.html' # 템플릿
#     context_object_name = 'posts' # 변수 값의 이름


# class Write(CreateView):
#     model = Post # 모델
#     form_class = PostForm # 폼  템플릿 지정안해줌(헷갈리기 않기!)
#     success_url = reverse_lazy('blog:list') # 성공 시 보내줄 url


class Write(LoginRequiredMixin, View): # 로그인됐을 때 View로 접근가능
    # Mixin: LoginRequiredMixin 로그인된사람만 접근가능함
    def get(self, request):
        form = PostForm()
        context = {
            'form': form
        }
        return render(request, 'blog/post_form.html', context)
    
    def post(self, request): # request -> HttpRequest 객체
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False) # commit=False 변수 할당만 우선 하고 이후에 수정가능
            post.writer = request.user
            post.save()
            return redirect('blog:list') # response -> HttpResponse 객체
        form.add_error(None, '폼이 유효하지 않습니다.')
        context = {
            'form': form
        }
        return render(request, 'blog/post_form.html')


# class Detail(DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'
#     context_object_name = 'post'


# class Update(UpdateView):
#     model = Post
#     template_name = 'blog/post_edit.html'
#     fields = ['title', 'content']
#     # success_url = reverse_lazy('blog:list')
    
#     # intial 기능 사용 -> form에 값을 미리 넣어주기 위해서
#     def get_initial(self):
#         initial = super().get_initial() # UpdateView(generic view)에서 제공하는 initial(딕셔너리)
#         post = self.get_object() # pk 기반으로 객체를 가져옴
#         initial['title'] = post.title
#         initial['content'] = post.content
#         return initial
    
#     def get_success_url(self): # get_absolute_url
#         post = self.get_object() # pk 기반으로 현재 객체 가져오기
#         return reverse('blog:detail', kwargs={ 'pk': post.pk })
        # kwargs(키워드를 뜻함) pk값을 키워드로 받겠다

    
class Update(View):
    def get(self, request, pk): # post_id
        post = Post.objects.get(pk=pk)
        form = PostForm(initial={'title': post.title, 'content': post.content})
        context = {
            'form': form,
            'post': post
        }
        return render(request, 'blog/post_edit.html', context)
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', pk=pk)
        
        form.add_error('폼이 유효하지 않습니다.')
        context = {
            'form': form
        }
        return render(request, 'blog/post_edit.html', context)


# class Delete(DeleteView):
#     model = Post
#     success_url = reverse_lazy('blog:list')


class Delete(View):
    def post(self, request, pk): # post_id
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('blog:list')
    
    # 클래스 자체에 아예 접근하지 못하게 -> LoginRequiredMixin
    # Login이 되었을 때만 삭제 버튼이 보이게


class DetailView(View):
    def get(self, request, pk): # post_id: 데이터베이스 post_id 테이블 이름 사용하고 싶어서
        # list -> object 상세 페이지 -> 상세 페이지 하나의 내용
        # pk 값을 왔다갔다, 하나의 인자
        

        # 데이터베이스 방문 (post요청으로 생각하지말기!!)
        # 해당 글
        # 장고 ORM (pk: 무조건 pk로 작성해야합니다)
        post = Post.objects.get(pk=pk)
        # 댓글
        comments = Comment.objects.filter(post=post) # 필터를 쓰면 괄호안에 있는 값을 조건으로 가져온다 post던 아니던
        # 해시태그
        hashtags = HashTag.objects.filter(post=post)
        
        # 댓글 Form
        comment_form = CommentForm()

        # 태그 Form
        hashtag_form = HashTagForm()

        context = {
            'post': post,
            'comments': comments,
            'hashtags': hashtags,
            'comment_form': comment_form,
            'hashtag_form': hashtag_form
        }
        
        return render(request, 'blog/post_detail.html', context)
    # 렌더링 하는 이유 : 디테일 페이지에서 렌더링 되어야 작성할 수 있음


### Comment
class CommentWrite(View):
    # def get(self, request):
    #     pass
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            # 사용자에게 댓글 내용을 받아옴
            content = form.cleaned_data['content']
            # 해당 아이디에 해당하는 글 불러옴
            post = Post.objects.get(pk=pk)
            # 유저 정보 가져오기
            writer = request.user
            # 댓글 객체 생성, create 메서드를 사용할 때는 save 필요 없음
            comment = Comment.objects.create(post=post, content=content, writer=writer)
            # comment = Comment(post=post) -> comment.save()
            return redirect('blog:detail', pk=pk)
        # 렌더링 이후에 가기 때문에 실시간으로 올라오는 것처럼 보이기 위해서 redirect 씀
        form.add_error('폼이 유효하지 않습니다.')
        context = {
            'form': form
        }
        return render(request, 'blog/form_error.html', context)


class CommentDelete(View):
    def post(self, request, pk): # comment_id
        # 지울 객체를 찾아야 한다. -> 댓글 객체를 가져와야 한다.
        comment = Comment.objects.get(pk=pk)
        # 상세페이지로 돌아가기
        post_id = comment.post.id
        # 삭제
        comment.delete()
        
        return redirect('blog:detail', pk=post_id)
    

### Tag
class HashTagWrite(View):
    def post(self, request, pk): # post_id
        form = HashTagForm(request.POST)
        if form.is_valid():
            # 사용자에게 태그 내용을 받아옴
            name = form.cleaned_data['name']
            # 해당 아이디에 해당하는 글 불러옴
            post = Post.objects.get(pk=pk)
            # 작성자 정보 가져오기
            writer = request.user
            # 댓글 객체 생성, create 메서드를 사용할 때는 save 필요 없음
            hashtag = HashTag.objects.create(post=post, name=name, writer=writer)
            # comment = Comment(post=post) -> comment.save()
            return redirect('blog:detail', pk=pk)
        
        form.add_error('폼이 유효하지 않습니다.')
        context = {
            'form': form
        }
        return render(request, 'blog/form_error.html', context)


class HashTagDelete(View):
    def post(self, request, pk): # hashtag_id
        # 지울 객체를 찾아야 한다. -> 태그 객체
        hashtag = HashTag.objects.get(pk=pk)
        # 상세페이지로 돌아가기
        post_id = hashtag.post.id
        # 삭제
        hashtag.delete()
        
        return redirect('blog:detail', pk=post_id)