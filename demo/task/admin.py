from django.contrib import admin

from demo.task.models import UserTask, Task

admin.site.register(Task)
admin.site.register(UserTask)
