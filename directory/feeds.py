from django.contrib.syndication.feeds import Feed
from models import Company

class CompaniesFeed(Feed):
    title = "Coimbra Directory companies"
    link = "/"
    description = "The latest companies featured in Coimbra Directory."

    def items(self):
        return Company.objects.filter(approved = True).order_by('-id')[:20]

    def item_title(self, item):
        return item.name
    
    def item_link(self, item):
        return item.website

    def item_description(self, item):
        return item.description
    
class AllCompaniesFeed(Feed):
    title = "Coimbra Directory editor feed"
    link = "/admin"
    description = "The latest companies submitted to Company Directory."

    def items(self):
        return Company.objects.order_by('-id')[:20]

    def item_title(self, item):
        return item.name
    
    def item_link(self, item):
        return item.website

    def item_description(self, item):
        return item.description