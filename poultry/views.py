from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework import viewsets
from django.utils.timezone import now

class FlockView(viewsets.ModelViewSet): 
    queryset=Flock.objects.all()
    serializer_class=FlockSerializer

class Dashboard(APIView):
    def get(self, request):
        flock_name = request.query_params.get("flock_name")  # Get flock name from request
        year = request.query_params.get("year", now().year)  # Default to current year
        date_filter = {"date__year": year}

        # Apply filtering if a flock name is provided
        flock_filter = {"name": flock_name} if flock_name else {}

        total_birds = Flock.objects.filter(**flock_filter).aggregate(total=Sum('birds_count'))['total'] or 0
        egg_production = EggProduction.objects.filter(flock__name=flock_name, **date_filter).aggregate(total=Sum('quantity'))['total'] or 0
        income = Income.objects.filter(**date_filter).aggregate(total=Sum('amount'))['total'] or 0
        expense = Expense.objects.filter(**date_filter).aggregate(total=Sum('amount'))['total'] or 0

        data = {
            "total_birds": total_birds,
            "egg_production": egg_production,
            "income": income,
            "expense": expense
        }

        serializer = DashboardSerializer(data)
        return Response(serializer.data)


