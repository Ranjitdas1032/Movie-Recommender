from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from main.forms import *
from main.models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomSignup(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"you have signin successfully....")
            return redirect('login_cus')
    else:
        form = CustomSignup()
    return render(request, 'myapp/signup.html', {'form': form})
    
def login_cus(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,"you have login successfully....")
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request,'myapp/login.html',{'form':form})

def logout_cus(request):
    logout(request)
    messages.success(request,"you have logout successfully....")
    return redirect('login_cus')

def home(request):
    movie_list = Movies.objects.all().order_by('-id')
    paginator = Paginator(movie_list, 6)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'myapp/home.html', {'movies': page_obj})

@login_required(login_url='/signup/')
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = MovieForm()
        
    return render(request,'myapp/Movie_Form.html',{'form':form})

@login_required(login_url='/signup/')
def movie_detail(request, pk):
    movie = get_object_or_404(Movies, pk=pk)
    comments = Comment.objects.filter(movie=movie).order_by('-timestamp')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.movie = movie
            comment.save()
            messages.success(request,"you comment has added successfully....")
            return redirect('movie_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, "myapp/detail.html", {
        'movie': movie,
        'form': form,
        'comments': comments
    })

def movie_chart_data(request,pk):
    movie = get_object_or_404(Movies,pk=pk)
    content = {
        'rottentomatoes' : movie.RottenTomatoes,
        'boxofficecollection': movie.BoxOfficeCollection
    }
    return JsonResponse(content)