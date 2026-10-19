from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


from .forms import BlogForm
# Create your views here.
# Display Hello Dear

def Dashboard(request):
    return render(request,"daily_news/Dashboard.html")

def blog_post(request):
    form = BlogForm()
    if request.method =="POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            # save the data to the data base
            form.save()
            return redirect("/")
       
    return render(request,
                  "daily_news/create-blog.html",
                    
    )


def homepage(request):
    blog_posts = Blog.objects.all()
    return render(request,"daily_news/homepage.html",
                  context={"blogs": blog_posts}
                  )

    # Redirect the user to /not_found
def article(request, pk):
    # Scan through the blog table
    # and get blog_posts whose id
    # is the same as the pk
    blog_posts = Blog.objects.filter(id=pk)

    if blog_posts.exists():
       return render(request,
                     "daily_news/article.html",
                     context={"blog": blog_posts.first()}
                     )
    else:
        return redirect("/not_found")

def not_found(request):
    return HttpResponse("not_found")

 
def edit_blog(request, pk):
    blog_posts = Blog.objects.filter(id=pk)

    if not blog_posts.exists():
        return redirect("/not_found")

    blog_post = blog_posts.first()

    if blog_post.author != request.user:
        return HttpResponse(
            "Permission Denied. You are not the owner of the blog post.", status=403
        )

    form = BlogForm(instance=blog_post)

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog_post)
        if form.is_valid():
            _post = form.save(commit=False)
            _post.author = request.user
            _post.published_at = blog_post.published_at
            _post.save()
            # return redirect(f"/article/{blog_post.pk})
            return redirect('read-blog', pk=blog_post.pk) 

    return render(request, "daily_news/edit_blog.html", {"blog_post": blog_post})

def register(request):
        form = UserCreationForm()
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return render("login")
            return render(request,"registration/register.html", {"form":form})

@login_required
def delete_blog(request, pk):
    if request.method == "POST":
        blog = Blog.objects.filter(id=pk).first()

        if blog and blog.author != request.user:
            return HttpResponse(
                "Permission Denied. You are not the owner of the blog post.",status=403
            )

        if blog:
            blog.delete() 

            return redirect("home")

    


@login_required
def profile(request):
    user = request.user

    # use the reverse accessor to obtain all the posts that belong to the user
    # and assign it to a variable called 'user_post'
    user_posts = user.blog_set.all()
    return render(request, "registration/profile.html", context={'blogs': user_posts})


                  
    



    

    