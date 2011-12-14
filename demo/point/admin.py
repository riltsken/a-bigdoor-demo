from django.contrib import admin

from demo.point import models as pmodels

admin.site.register(pmodels.Transaction)
admin.site.register(pmodels.Award)
admin.site.register(pmodels.Level)
admin.site.register(pmodels.Currency)
