from renovation_costs.models import Product

paints = Product.objects.filter(product_category_id=1).values_list('id', 'name')
bases = Product.objects.filter(product_category_id=2).values_list('id', 'name')
wallpaper = Product.objects.filter(product_category_id=3).values_list('id', 'name')
wallpaper_glue = Product.objects.filter(product_category_id=4).values_list('id', 'name')
wall_tiles = Product.objects.filter(product_category__name='płytki ścienne').values_list('id', 'name')
floor_tiles = Product.objects.filter(product_category__name='płytki podłogowe').values_list('id', 'name')
fugue = Product.objects.filter(product_category__name='fuga').values_list('id', 'name')
silicone = Product.objects.filter(product_category__name='silikon').values_list('id', 'name')

