from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post

class LatestPostsFeed(Feed):
    title = 'My blog'
    link = '/blog/'
    description = 'New posts of my blog.'

    def items(self): # Retrieve the object to be included in the feed. in this case the last five published posts.
        return Post.published.all()[:5]

    def item_title(self, item): # This method retrieve the title of the "items method" defined before and
        return item.title       # return the title of it.

    def item_description(self, item): # same as the last one but retrieve the body.
        return truncatewords(item.body, 30)