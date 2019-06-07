from renovation_costs.models import Product

paints = Product.objects.filter(product_category_id=1).values_list('id', 'name')
bases = Product.objects.filter(product_category_id=2).values_list('id', 'name')
wallpaper = Product.objects.filter(product_category_id=3).values_list('id', 'name')
wallpaper_glue = Product.objects.filter(product_category_id=4).values_list('id', 'name')
floor_tiles = Product.objects.filter(product_category_id=5).values_list('id', 'name')
wall_tiles = Product.objects.filter(product_category_id=6).values_list('id', 'name')
fugue = Product.objects.filter(product_category_id=7).values_list('id', 'name')
silicone = Product.objects.filter(product_category_id=8).values_list('id', 'name')
plaster = Product.objects.filter(product_category_id=9).values_list('id', 'name')
plaster_base = Product.objects.filter(product_category_id=10).values_list('id', 'name')
layers_of_plaster = (
    (1, 'Jednokrotne szpachlowanie'),
    (2, 'Dwukrotne szpachlowanie'),
    (3, 'Trzykrotne szpachlowanie'),
)

floor_panels = Product.objects.filter(product_category_id=11).values_list('id', 'name')
floor_panel_bed = Product.objects.filter(product_category_id=12).values_list('id', 'name')
foil = Product.objects.filter(product_category_id=13).values_list('id', 'name')
board = Product.objects.filter(product_category_id=14).values_list('id', 'name')
