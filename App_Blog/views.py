from django.shortcuts import render

# Create your views here.
def blog_list(request):
    return render(request,'App_Blog/blog_list.html',context={})

@login_required
def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = CommentForm()
    already_liked = Likes.objects.filter(blog=blog, user= request.user)
    if already_liked:
        liked = True
    else:
        liked = False


 class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image')
    template_name = 'App_Blog/edit_blog.html'

def get_success_url(self, **kwargs):
        return reverse_lazy('App_Blog:blog_details', kwargs={'slug':self.object.slug})
