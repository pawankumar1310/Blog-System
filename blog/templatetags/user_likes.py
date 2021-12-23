from typing import Union

from django import template

from blog.models import Blog, UserComment

register = template.Library()


@register.simple_tag
def has_user_liked(content: Union[Blog, UserComment], user) -> bool:
    return content.has_user_liked(user)