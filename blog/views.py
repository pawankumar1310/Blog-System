from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.http import Http404
from blog.models import Blog, UserComment
from account.models import Usermodel
from django.db.models import Q

# Create your views here.


class BlogPostsView(ListView):
    model = Blog
    queryset = Blog.objects.prefetch_related()
    template_name = 'blogpost_list.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pagination = context['page_obj']
        pages = []

        # Create a list of max 3 pages right and 3 pages left from the
        # current page and pas it to template as context argument
        # If there is only one page do not include in pagination
        for i in range(
                pagination.number - 3
                if pagination.number - 3 > 0 else 1,
                pagination.number + 3
                if pagination.number + 3 <= pagination.paginator.num_pages else pagination.paginator.num_pages + 1):
            pages.append(i)

        context['pages'] = pages if len(pages) > 1 else []

        return context


class BloggersList(ListView):
    model = Usermodel
    template_name = 'authors_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        moderator_or_author = Q(user_type__in='a') | Q(user_type__in='s')
        return queryset.filter(moderator_or_author)


class BlogSearchView(ListView):
    model = Blog
    queryset = Blog.objects.filter()
    template_name = 'blog/blogpost_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if not query:
            raise Http404
        search_query = Q(title__icontains=query) | Q(content__icontains=query)
        return queryset.filter(search_query)


class AuthorPostsView(DetailView):
    model = Usermodel
    template_name = 'components/user_posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.can_post:
            user_posts = Blog.objects.filter(author_id=self.object)
            context['posts'] = user_posts
        else:
            raise Http404()
        return context


class BlogPostDetailView(DetailView):
    model = Blog
    template_name = 'blogpost_detail.html'
    queryset = Blog.objects.filter().select_related(
        'author_id').prefetch_related('author_id', 'likes')

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()

        self.get_context_data(object=self.object)
        # Prevent user resubmit comment by refreshing the page
        return redirect(request.path)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.method == 'POST':
            # If it is a post request check if there is a comment field
            # for current user and add it to the db
            comment = self.request.POST.get('comment')

            if comment:
                new_comment = UserComment(
                    author_id=self.request.user,
                    blog_id=self.object,
                    comment=comment
                )
                print(new_comment)
                new_comment.save()
        comments = UserComment.objects.filter(blog_id=self.object)
        if comments:
            context['comments'] = comments

        return context
