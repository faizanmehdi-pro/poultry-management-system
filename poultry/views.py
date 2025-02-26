
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.response import Response
  

class Dashboard(APIView):
    def get(self,request):
        data={
        "total_birds":Flock.objects.aggregate(total=Sum('birds_count'))['total'] or 0,
        "egg_production":EggProduction.objects.aggregate(total=Sum('quantity'))['total'] or 0,
        "income" : Income.objects.aggregate(total=Sum('amount'))['total'] or 0,
        "expense" : Expense.objects.aggregate(total=Sum('amount'))['total'] or 0

        }
        serializer=DashboardSerializer(data)
        return Response(serializer.data)