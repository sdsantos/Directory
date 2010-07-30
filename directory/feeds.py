from django.contrib.syndication.feeds import Feed
from models import Company

class CompaniesFeed(Feed):
    title = "Coimbra Directory"
    link = "/"
    description = "The latest companies featured in Coimbra Directory."

    title_template = 'feed_title.html'
    description_template = "feed_description.html"

    def items(self):
        return Company.objects.filter(approved = True).order_by('-id')[:20]

class AllCompaniesFeed(Feed):
    title = "Coimbra Directory editor feed"
    link = "/admin"
    description = "The latest companies submitted to Company Directory."

    title_template = 'feed_title.html'
    description_template = "feed_description.html"

    def items(self):
        return Company.objects.order_by('-id')[:20]
