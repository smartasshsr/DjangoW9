from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting, Comment
from .forms import PostingForm, CommentForm

# Create your views here.
def index(request):
    return render(request, 'page/index.html')

# [Read] 전체 글 목록 보기
def posting_list(request):
    postings = Posting.objects.all()
    context = {
        'postings': postings,
    }
    return render(request, 'page/posting_list.html', context)

# [Create] 글 작성하기
def posting_create(request):
    if request.method == 'POST':
        posting_form = PostingForm(request.POST)
        
        if posting_form.is_valid():
            posting_form.save()
            return redirect('page:posting_list')
    else:
        posting_form = PostingForm()
    
    context = {
        'posting_type': '글쓰기',
        'posting_form': posting_form,
    }
    return render(request, 'page/posting_form.html', context)

# [Read & Create] 작성글 보기 & 댓글 작성
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():
            comment_form = comment_form.save(commit=False)
            comment_form.posting = posting
            comment_form.save()
            return redirect('page:posting_detail', posting_id)
    else :
        comment_form = CommentForm()
    
    comments = posting.comment_list.all()

    context = {
        'posting': posting,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'page/posting_detail.html', context)

# [Update] 작성글 수정
def posting_update(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    if request.method == 'POST':
        posting_form = PostingForm(request.POST, instance=posting)

        if posting_form.is_valid():
            posting_form.save()
            return redirect('page:posting_detail', posting_id)
    else:
        posting_form = PostingForm(instance=posting)

    context = {
        'posting_type': '글수정',
        'posting': posting,
        'posting_form': posting_form,
    }
    return render(request, 'page/posting_form.html', context)

# [Delete] 작성글 삭제
def posting_delete(request, posting_id):
    if request.method == 'POST':
        posting = get_object_or_404(Posting, id=posting_id)
        posting.delete()
        return redirect('page:posting_list')
    return redirect('page:posting_detail', posting_id)

# [Delete] 댓글 삭제
def comment_delete(request, posting_id, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return redirect('page:posting_detail', posting_id)
