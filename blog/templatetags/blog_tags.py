from django import template
from django.db.models import Count
import markdown
from django.utils.safestring import mark_safe

register = template.Library() # this is a instance of template library and it's used to register your own template tags.

from ..models import Post

@register.simple_tag  # way ton regsiter a simple tag.
def total_posts():  # we define a tag called "total_posts". Django will use the function name as a tag name.
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')  # with an inclusion tag you can render a template with context varaibles returned
                                                        # by you template tag. We spiecified the template that has to be rendered with the return
                                                        # value.
def show_latest_posts(count=5):  # number of comments we want to display count = 5.
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}  # the function return a dictionary of values instead of a simple value.


@register.assignment_tag  # are like simple tags that stores the result in a given variable.

def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='markdown') #This is a template filter.
def markdown_format(text):
    return mark_safe(markdown.markdown(text)) # mark a string as safe for (HTML) output purposes. it's necessary to mark this html safe. If not, Django wouldn't use it for security reasons.

