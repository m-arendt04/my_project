from renovation_costs.models import Product

paints_list = Product.objects.filter(product_category_id=1).values_list('id', 'name', 'price')
paints = [(p[0], f"{p[1]} - {p[2]} zł") for p in paints_list]
bases_list = Product.objects.filter(product_category_id=2).values_list('id', 'name', 'price')
bases = [(b[0], f"{b[1]} - {b[2]} zł") for b in bases_list]
wallpaper_list = Product.objects.filter(product_category_id=3).values_list('id', 'name', 'price')
wallpaper = [(w[0], f"{w[1]} - {w[2]} zł") for w in wallpaper_list]
wallpaper_glue_list = Product.objects.filter(product_category_id=4).values_list('id', 'name', 'price')
wallpaper_glue = [(wg[0], f"{wg[1]} - {wg[2]} zł") for wg in wallpaper_glue_list]
floor_tiles_list = Product.objects.filter(product_category_id=5).values_list('id', 'name', 'price')
floor_tiles = [(ft[0], f"{ft[1]} - {ft[2]} zł") for ft in floor_tiles_list]
wall_tiles_list = Product.objects.filter(product_category_id=6).values_list('id', 'name', 'price')
wall_tiles = [(w[0], f"{w[1]} - {w[2]} zł") for w in wall_tiles_list]
fugue_list = Product.objects.filter(product_category_id=7).values_list('id', 'name', 'price')
fugue = [(f[0], f"{f[1]} - {f[2]} zł") for f in fugue_list]
silicone_list = Product.objects.filter(product_category_id=8).values_list('id', 'name', 'price')
silicone = [(s[0], f"{s[1]} - {s[2]} zł") for s in silicone_list]
plaster_list = Product.objects.filter(product_category_id=9).values_list('id', 'name', 'price')
plaster = [(ps[0], f"{ps[1]} - {ps[2]} zł") for ps in plaster_list]
plaster_base_list = Product.objects.filter(product_category_id=10).values_list('id', 'name', 'price')
plaster_base = [(pb[0], f"{pb[1]} - {pb[2]} zł") for pb in plaster_base_list]
layers_of_plaster = (
    (1, 'Jednokrotne szpachlowanie'),
    (2, 'Dwukrotne szpachlowanie'),
    (3, 'Trzykrotne szpachlowanie'),
)

floor_panels_list = Product.objects.filter(product_category_id=11).values_list('id', 'name', 'price')
floor_panels = [(fp[0], f"{fp[1]} - {fp[2]} zł") for fp in floor_panels_list]
floor_panel_bed_list = Product.objects.filter(product_category_id=12).values_list('id', 'name', 'price')
floor_panel_bed = [(fb[0], f"{fb[1]} - {fb[2]} zł") for fb in floor_panel_bed_list]
foil_list = Product.objects.filter(product_category_id=13).values_list('id', 'name', 'price')
foil = [(fl[0], f"{fl[1]} - {fl[2]} zł") for fl in foil_list]
board_list = Product.objects.filter(product_category_id=14).values_list('id', 'name', 'price')
board = [(bd[0], f"{bd[1]} - {bd[2]} zł") for bd in board_list]
