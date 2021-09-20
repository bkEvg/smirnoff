from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.9
    changefreq = 'weekly'
    i18n = True

    def items(self):
        return ['main', 'livingroom', 'kitchen', 'ideas_list', 'bedroom']

    def location(self, item):
        return reverse(item)