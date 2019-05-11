from django.shortcuts import render, get_object_or_404, redirect

from .models import Board, Comment

from django.utils import timezone

from .forms import CommentForm

# Create your views here.

def home(request):
    boards = Board.objects
    return render(request, 'home.html', {'boards': boards})

def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'board': board_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    board = Board()
    board.title = request.GET['title']
    board.body = request.GET['body']
    board.pub_date = timezone.datetime.now()
    board.save()
    return redirect('/myapp/' + str(board.id))

def delete(request, board_id):
    board = Board.objects.get(pk = board_id)
    board.delete()
    return redirect('/')

def edit(request, board_id):
    board_edit = Board.objects.get(pk= board_id)
    return render(request, 'edit.html', {'board': board_edit})

def update(request, board_id):
    board = Board.objects.get(pk= board_id)
    board.title = request.POST['title']
    board.body = request.POST['body']
    board.pub_date = timezone.datetime.now()
    board.save()
    return redirect('/')

def comment_new(request, board_id):
    post = get_object_or_404(Board, pk=board_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Board.objects.get(pk=board_id)
            comment.save()
            return redirect('detail', board_id)
    else:
        form= CommentForm()
    return render(request, 'board_form.html', {'form':form})

def comment_delete(request, comment_id):
#    password_input=request.GET['password']
#    passwordregistered = 
#    if(passwordinput==passwordregistered):
#    comment=Comment.objects.get(pk=comment_id)
#    comment.delete()
#    return redirect('board', board_id)
    return redirect('/')
