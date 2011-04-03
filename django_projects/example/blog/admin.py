from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils.html import escape
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from blog.models import Post
from blog.models import Comment 

class PostAdmin(admin.ModelAdmin):
    search_field = ["title"]

class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post,PostAdmin)
