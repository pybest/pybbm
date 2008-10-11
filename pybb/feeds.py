from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from django.core.urlresolvers import reverse

from pybb.models import Post, Topic

class PybbFeed(Feed):
    feed_type = Atom1Feed

    def link(self):
        return reverse('pybb.views.index')

    def item_guid(self, obj):
        return str(obj.id)

class LastPosts(PybbFeed):
    title = 'Latest posts on forum'
    description = 'Latest posts on forum'
    title_template = 'pybb/feeds/posts_title.html'
    description_template = 'pybb/feeds/posts_description.html'

    def items(self):
        return Post.objects.order_by('-created')[:15]


class LastTopics(PybbFeed):
    title = 'Latest topics on forum'
    description = 'Latest topics on forum'
    title_template = 'pybb/feeds/topics_title.html'
    description_template = 'pybb/feeds/topics_description.html'

    def items(self):
        return Topic.objects.order_by('-created')[:15]