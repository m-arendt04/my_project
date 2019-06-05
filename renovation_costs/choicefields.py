from renovation_costs.models import Paint, Base

paints = Paint.objects.values_list('id', 'name')
bases = Base.objects.values_list('id', 'name')
