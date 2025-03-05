from django.db import models
from django.utils import timezone


class Flock(models.Model):
    name = models.CharField(max_length=100,unique=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    type = models.CharField(max_length=50,default="broiler")  
    description = models.TextField(null=True, blank=True)
    birds_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    
class FeedType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Feed(models.Model):
    feed_type = models.ForeignKey(FeedType, on_delete=models.CASCADE)
    quantity_bags = models.PositiveIntegerField()
    date_recorded = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.feed_type.name} - {self.quantity_bags} bags"



class Currency(models.Model):
    name = models.CharField(max_length=50, unique=True)
    symbol = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.name} ({self.symbol})"


class EggProduction(models.Model):
    flock = models.ForeignKey(Flock, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} eggs of {self.flock.name} on {self.date}"
    
class IncomeCategory(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Income(models.Model):
    date=models.DateField()
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    currency=models.ForeignKey(Currency,on_delete=models.SET_NULL,null=True)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    description=models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Expense(models.Model):
    date = models.DateField()
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True)
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.category} - {self.amount} on {self.date}"

class InventoryLog(models.Model):
    INVENTORY_CHOICES={
        ('birds','Birds'),
        ('feed','Feed'),
        ('eggs','Eggs'),
    }

    TYPE_CHOICES={
        ('addition','Addition'),
        ('reduction','Reduction'),
    
    }
    date=models.DateField()
    type=models.CharField(max_length=100,choices=TYPE_CHOICES)
    inventory=models.CharField(max_length=100,choices=INVENTORY_CHOICES)
    flock_reduction_reason=models.CharField(max_length=50,null=True,blank=True)
    birds_count = models.IntegerField(null=True, blank=True)
    feed_quantity = models.IntegerField(null=True, blank=True)
    feed_unit = models.CharField(max_length=50, null=True, blank=True)
    feed_reduction_reason = models.CharField(max_length=100, null=True, blank=True)
    eggs_quantity = models.IntegerField(null=True, blank=True)
    egg_reduction_reason = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.type} - {self.inventory} on {self.date}"
    




    





   
