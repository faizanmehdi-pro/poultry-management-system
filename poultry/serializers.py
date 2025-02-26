from rest_framework import serializers
from .models import (
    Flock, FeedType, Feed, Currency,  EggProduction, IncomeCategory,
    ExpenseCategory, Income, Expense, InventoryLog
)

class FlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flock
        fields = '__all__'

class FeedTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedType
        fields = '__all__'

class FeedSerializer(serializers.ModelSerializer):
    feed_type = serializers.StringRelatedField()  # To display feed type name

    class Meta:
        model = Feed
        fields = '__all__'

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class EggProductionSerializer(serializers.ModelSerializer):
    flock = serializers.StringRelatedField()

    class Meta:
        model = EggProduction
        fields = '__all__'

class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = '__all__'

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'

class IncomeSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer(read_only=True)
    category = IncomeCategorySerializer(read_only=True)

    class Meta:
        model = Income
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer(read_only=True)
    category = ExpenseCategorySerializer(read_only=True)

    class Meta:
        model = Expense
        fields = '__all__'

class InventoryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryLog
        fields = '__all__'


class DashboardSerializer(serializers.Serializer):
    total_birds=serializers.IntegerField()
    egg_production=serializers.IntegerField()
    income=serializers.IntegerField()
    expense=serializers.IntegerField()