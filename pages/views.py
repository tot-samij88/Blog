from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Post


def index(request):
    post = Post.objects.all().filter(is_published=True)
    paginator = Paginator(post, 3)
    page = request.GET.get('page')
    pages_post = paginator.get_page(page)
    context = {
        "posts": pages_post,
    }
    return render(request, 'pages/index.html', context)


def single(request, post_id):
    single_post = get_object_or_404(Post, pk=post_id)
    return render(request, 'pages/single.html', {"single_post": single_post, })



""" Autentification. Add user, later == if else -> bad or OK -> request. The end  """

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username alrady taken .")
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email alrady taken .")
                return redirect(register)
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password,is_staff=1,is_superuser=1)
                user.save()
                messages.success(request, "You are registred. Sign in")
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")
        return render(request, "pages/register.html")
    else:
        return render(request, "pages/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are in")
            return redirect('index')
        else:
            messages.error(request, "Login or password incorrect")
            return redirect('login')
    else:
        return render(request, "pages/login.html")


def logout(request):
    if request.method == "POST":
        auth.logout(request)
    messages.success(request, "See you later.")
    return redirect('index')

