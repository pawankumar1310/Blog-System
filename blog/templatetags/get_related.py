from django import template
from django.db.models import Count

from blog.models import Blog, UserComment

register = template.Library()


@register.simple_tag
def get_similar_posts(post: Blog) -> Blog:
    """Get a list of post sorted based of likes on the same category where the post is"""
    return Blog.objects.filter(category=post.category.first()).exclude(id=post.id) \
               .annotate(count=Count('likes')).order_by('-count').prefetch_related("category", "author")[:3]