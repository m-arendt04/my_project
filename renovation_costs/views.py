import math

from django.shortcuts import render
from django.views import View

from renovation_costs.forms import PaintingCostForm, SlotSizeCalc, WallpaperCostForm, CeramicGlazeCostForm, AreaSizeCalc
# from renovation_costs.models import Paint, Base, Wallpaper, WallpaperGlue
from renovation_costs.models import Product


class RenovationCategoriesView(View):
    def get(self, request):
        return render(request, 'renovation_costs/renovation_cost_main.html')


class PaintingCostView(View):
    def get(self, request):
        form = PaintingCostForm()
        form_calc = SlotSizeCalc()
        ctx = {
            'form': form,
            'form_slot_size': form_calc
        }
        return render(request, 'renovation_costs/painting_cost_view.html', ctx)

    #
    def post(self, request):
        form = PaintingCostForm(request.POST)
        if form.is_valid():
            running_metre = form.cleaned_data['running_metre']
            flat_height = form.cleaned_data['flat_height']
            slot_area = form.cleaned_data['slot_area']
            ceiling_area = form.cleaned_data['ceiling_area']
            paint = form.cleaned_data['paints']
            base = form.cleaned_data['bases']

            paint_area = running_metre * flat_height + ceiling_area - slot_area
            chosen_paint = Product.objects.get(pk=paint)
            chosen_base = Product.objects.get(pk=base)

            result_of_paint = math.ceil(paint_area / chosen_paint.usage_per_unit) \
                              * chosen_paint.price
            result_of_base = math.ceil(paint_area / chosen_base.usage_per_unit) \
                             * chosen_base.price

            ctx = {
                'costs_of_paint': round(result_of_paint, 2),
                'costs_of_base': round(result_of_base, 2),
                'chosen_paint': chosen_paint,
                'chosen_base': chosen_base,
            }
            return render(request, 'renovation_costs/painting_cost_view_done.html', ctx)


class WallpaperCostView(View):
    def get(self, request):
        form = WallpaperCostForm()
        form_calc = SlotSizeCalc()
        ctx = {
            'form': form,
            'form_slot_calc': form_calc
        }
        return render(request, 'renovation_costs/wallpaper_cost_view.html', ctx)

    def post(self, request):
        form = WallpaperCostForm(request.POST)
        if form.is_valid():
            running_metre = form.cleaned_data['running_metre']
            flat_height = form.cleaned_data['flat_height']
            slot_area = form.cleaned_data['slot_area']
            wallpaper = form.cleaned_data['wallpaper']
            glue = form.cleaned_data['glue']

            wallpaper_area = running_metre * flat_height - slot_area
            chosen_wallpaper = Product.objects.get(pk=wallpaper)
            chosen_glue = Product.objects.get(pk=glue)

            result_of_wallpaper = math.ceil(wallpaper_area / chosen_wallpaper.usage_per_unit) * chosen_wallpaper.price
            result_of_glue = math.ceil(wallpaper_area/chosen_glue.usage_per_unit) * chosen_glue.price

            ctx = {
                'costs_of_wallpaper': round(result_of_wallpaper, 2),
                'costs_of_glue': round(result_of_glue, 2),
                'chosen_wallpaper': chosen_wallpaper,
                'chosen_glue': chosen_glue,
            }
            return render(request, 'renovation_costs/wallpaper_cost_view_done.html', ctx)


class CeramicGlazeCostView(View):
    def get(self, request):
        form = CeramicGlazeCostForm()
        form_calc_1= SlotSizeCalc()
        form_calc_2= AreaSizeCalc()

        ctx = {
            'form': form,
            'form_slot_calc': form_calc_1,
            'form_floor_tiles_area': form_calc_2
        }

        return render(request, 'renovation_costs/ceramic_glaze_cost_view.html', ctx)

    def post(self, request):
        form = CeramicGlazeCostForm(request.POST)
        if form.is_valid():
            wall_running_metre = form.cleaned_data['wall_running_metre']
            wall_height = form.cleaned_data['wall_height']
            floor_area = form.cleaned_data['floor_area']
            slot_area = form.cleaned_data['slot_area']
            wall_tiles = form.cleaned_data['wall_tiles']
            floor_tiles = form.cleaned_data['floor_tiles']
            fugue = form.cleaned_data['fugue']
            silicone = form.cleaned_data['silicone']
