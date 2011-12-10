from django.contrib import admin

from demo.point.models import Transaction,Award,Level

admin.site.register(Transaction)
admin.site.register(Award)
admin.site.register(Level)
