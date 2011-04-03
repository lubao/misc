from todo.models import Item
from todo.models import DateTime
from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils.html import escape
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'priority', 'difficulty', 'done']
    search_field = ['name']

class ItemInline(admin.TabularInline):
    extra = 3 
    model = Item

class DateAdmin(admin.ModelAdmin):
    list_display = ['datetime']
    inlines = [ItemInline]

    def response_add(self, request, obj, post_url_continue='../%s/'):
        ''' Determines the HttpResponse for the add_view stage '''
        opts = obj._meta
        pk_value = obj._get_pk_val()

        msg = "Item(s) were added successfully"
        # Here, we distinguish b/t different save types by checking for
        # the presence of keys in request.POST
        if request.POST.has_key("_continue"):
            self.message_user(request, msg + ' ' + 
                _("You may edit it again below."))
            if request.POST.has_key("_popup"):
                post_url_continue += "?_popup=1"
            return HttpResponseRedirect(post_url_continue % pk_value)

        if request.POST.has_key("_popup"):
            return HttpResponse(
               '<script type="text/javascript">opener.dismissAddAnotherPopup(window, "%s", "%s");'
               '</script>' % (escape(pk_value), escape(obj))
                )
        elif request.POST.has_key("_addanother"):
            self.message_user(request, msg + ' ' + (
             _("You may add another %s below.") %force_unicode(opts.verbose_name)))
            return HttpResponseRedirect(request.path)
        else:
            self.message_user(request, msg)
            return HttpResponseRedirect(reverse("admin:todo_item_changelist"))


admin.site.register(Item, ItemAdmin)
admin.site.register(DateTime, DateAdmin)
