from django.contrib import admin

from .models import Article, ArticleCategory, BibliographicDatabase, PublicationType

admin.site.register(ArticleCategory)
admin.site.register(PublicationType)
admin.site.register(BibliographicDatabase)
admin.site.register(Article)
