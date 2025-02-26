from django.contrib import admin
from .models import *

admin.site.register(Flock)
admin.site.register(FeedType)
admin.site.register(Feed)
admin.site.register(EggProduction)
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(ExpenseCategory)
admin.site.register(IncomeCategory)
admin.site.register(InventoryLog)

