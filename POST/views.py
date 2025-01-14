from django.shortcuts import render, redirect
from.forms import*
from.models import*
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    posts=Post.objects.all().order_by('-date')
    allusers=Users.objects.all()
    p_form=postForm()
    if request.method=="POST":
        p_form=postForm(request.POST, request.FILES)
        if p_form.is_valid():
            form=p_form.save(commit=False)
            form.author=request.user

            form.save()
            messages.info(request, 'successfully post posted!!!!')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Error in posting')
            return redirect('dashboard')
         
    # Pagination logic
    paginator = Paginator(posts, per_page=2)  # 2 posts per page
    page_number = request.GET.get('page')  # Get the current page number
    page_obj = paginator.get_page(page_number)  # Get the posts for that page
    
    context={
        'form':p_form,
        'post':page_obj,
        'alluser':allusers,
        'paginator':paginator,
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required(login_url='login')
def postdetail(request, pk):
    post = Post.objects.get(id=pk)
    c_form = commentForm()
    follow_form = followForm()
    comments = Comment.objects.filter(post=post)
    comment_count = comments.count()
    followers_count = Follow.objects.filter(followee=post.author).count()

    if request.method == "POST":
        # Handling comment form submission
        c_form = commentForm(request.POST)
        if c_form.is_valid():
            comment = c_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'Your comment has been posted successfully!')
            # Redirecting to the same post to see the comment
            return redirect('post-detail', pk=post.id)
        
        
        # Handling follow form submission
        follow_form = followForm(request.POST)
        follow=Follow.objects.filter(follower=request.user).exists()
        if follow_form.is_valid():
            follow = follow_form.save(commit=False)
            follow.followee = post.author
            follow.follower = request.user
            follower_exist=Follow.objects.filter(follower=follow.follower, followee=follow.followee) .exists()
            if follower_exist:
                messages.warning(request, 'already  followed')
                return redirect('post-detail', pk=post.id)
            else:
                follow.save()
                messages.success(request, 'You are now following this post!')
                return redirect('post-detail', pk=post.id)
        else:
            messages.warning(request, 'Failed to follow. Please try again.')

    context = {
        'c_form': c_form,
        'post': post,
        'count': comment_count,
        'content': comments,
        'followers_count': followers_count,
        'follow_form': follow_form,
    }
    return render(request, 'post/post_detail.html', context)


@login_required(login_url='login')
def update_post(request, pk):
    posts=Post.objects.get(id=pk)
    forms=postForm(instance=posts)
    
    if request.method=="POST":
        forms=postForm(request.POST, request.FILES, instance=forms)
        if forms.is_valid():
            form=forms.save(commit=False)
            form.author=request.user
            form.save()
            messages.success(request, 'successfully updated post')
            return redirect('post-detail')
        else:
            messages.warning(request, 'failure to update post')
            return redirect('post-detail')
    context={
        'post':posts,
    }
    return render(request, 'post/post_detail.html', context)


@login_required(login_url='login')
def post_del(request, pk):
    post=Post.objects.get(id=pk)
    post.delete()
    messages.warning(request, 'successfully delete post')
    return redirect('post-detail')


@login_required(login_url='login')
def post_detail(request, pk):
    followee=Post.objects.get(id=pk)
    if request.method=="POST":
        follow_form=followForm(request.POST)
        if follow_form.is_valid():
            form=follow_form.save(commit=False)
            form.followee=followee
            form.follower=request.user
            form.save()
            messages.info(request, 'successfully followed')
            return redirect('post-detail')    
        else:
            messages.warning(request, 'failure to folllow user')
            return redirect('post-detail')
    
 
@login_required(login_url='login')   
def post_detail(request, pk):
    posts=Post.objects.get(id=pk)
    context={
        'post':posts,
    }
    return render(request, 'post/post_detail.html', context)


@login_required(login_url='login')
def post_update(request, pk):
    posts=Post.objects.get(id=pk)
    forms=postForm(instance=posts)
    if request.method=="POST":
        forms =postForm(request.POST or None, request.FILES, instance=posts)
        if forms.is_valid():
            form =forms.save(commit=False)
            form.author=request.user
            form.save()
            messages.success(request, 'successfull post updated')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Error in updating post')
            return redirect('post-update')
    context={
        'post':posts,
        'form':forms,
    }
    return render(request, 'post/post_update.html', context)



@login_required(login_url='login')
def post_delete(request, pk):
    post=Post.objects.get(id=pk)
    post.delete()
    messages.warning(request, 'Successfull post deleted')
    return redirect('post-detail')