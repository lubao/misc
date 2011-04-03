# Create your views here.
from todoList.todo.models import *
from django.core.urlresolvers import reverse

def mark_done(request, pk):
    item = Item.objects.get(pk=pk)
    item.done = True
    item.save()
    return HttpResponseRedirect(reverse("admin:todo_item_changelist"))

