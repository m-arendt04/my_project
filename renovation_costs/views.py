from django.shortcuts import render
from django.views import View


class RenovationCostView(View):
    def get(self, request):
        return render(request, 'renovation_costs/renovation_cost_main.html')

