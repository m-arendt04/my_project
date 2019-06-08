import math

from django.shortcuts import render
from django.views import View

from renovation_costs.forms import PaintingCostForm, SlotSizeCalc, WallpaperCostForm, CeramicGlazeCostForm, \
    AreaSizeCalc, PlasterCostForm, FloorPanelCostForm
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

    def post(self, request):
        form = PaintingCostForm(request.POST)
        if form.is_valid():
            running_metre = form.cleaned_data['running_metre']
            flat_height = form.cleaned_data['flat_height']
            slot_area = form.cleaned_data['slot_area']
            ceiling_area = form.cleaned_data['ceiling_area']
            paint = form.cleaned_data['paints']
            base = form.cleaned_data['base']

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
            result_of_glue = math.ceil(wallpaper_area / chosen_glue.usage_per_unit) * chosen_glue.price

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
        form_calc_1 = SlotSizeCalc()
        form_calc_2 = AreaSizeCalc()

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
            silicone_running_metre = form.cleaned_data['silicone_running_metre']
            silicone = form.cleaned_data['silicone']

            ceramic_glaze_area_walls = wall_running_metre * wall_height - slot_area
            ceramic_glaze_area_floor = floor_area
            chosen_wall_tiles = Product.objects.get(pk=wall_tiles)
            chosen_floor_tiles = Product.objects.get(pk=floor_tiles)
            chosen_fugue = Product.objects.get(pk=fugue)
            chosen_silicone = Product.objects.get(pk=silicone)

            wall_tiles_result = math.ceil(
                ceramic_glaze_area_walls / chosen_wall_tiles.usage_per_unit
            ) * chosen_wall_tiles.price
            floor_tiles_result = math.ceil(
                ceramic_glaze_area_floor / chosen_floor_tiles.usage_per_unit
            ) * chosen_floor_tiles.price
            fugue_result = math.ceil(
                (ceramic_glaze_area_floor + ceramic_glaze_area_walls) / chosen_fugue.usage_per_unit
            ) * chosen_fugue.price
            silicone_result = math.ceil(
                silicone_running_metre / chosen_silicone.usage_per_unit
            ) * chosen_silicone.price

            ctx = {
                'wall_tiles_result': round(wall_tiles_result, 2),
                'floor_tiles_result': round(floor_tiles_result, 2),
                'fugue_result': round(fugue_result, 2),
                'silicone_result': round(silicone_result, 2),
                'products': {
                    'floor_tiles': chosen_floor_tiles,
                    'wall_tiles': chosen_wall_tiles,
                    'fugue': chosen_fugue,
                    'silicone': chosen_silicone,
                }
            }

            return render(request, 'renovation_costs/ceramic_glaze_cost_view_done.html', ctx)


class PlasterCostView(View):
    def get(self, request):
        form = PlasterCostForm()
        form_calc_1 = SlotSizeCalc()

        ctx = {
            'form': form,
            'form_slot_calc': form_calc_1,
        }

        return render(request, 'renovation_costs/plaster_cost_view.html', ctx)

    def post(self, request):
        form = PlasterCostForm(request.POST)
        if form.is_valid():
            running_metre = form.cleaned_data['running_metre']
            flat_height = form.cleaned_data['flat_height']
            slot_area = form.cleaned_data['slot_area']
            ceiling_area = form.cleaned_data['ceiling_area']
            layers_of_plaster = int(form.cleaned_data['layers_of_plaster'])
            plaster = form.cleaned_data['plaster']
            base = form.cleaned_data['base']

            plaster_area = running_metre * flat_height + ceiling_area - slot_area
            chosen_plaster = Product.objects.get(pk=plaster)
            chosen_base = Product.objects.get(pk=base)

            result_of_plaster = math.ceil(
                plaster_area * layers_of_plaster / chosen_plaster.usage_per_unit
            ) * chosen_plaster.price
            result_of_base = math.ceil(
                plaster_area / chosen_base.usage_per_unit
            ) * chosen_base.price

            ctx = {
                'costs_of_plaster': round(result_of_plaster, 2),
                'costs_of_base': round(result_of_base, 2),
                'chosen_plaster': chosen_plaster,
                'chosen_base': chosen_base,
            }
            return render(request, 'renovation_costs/plaster_cost_view_done.html', ctx)


class FloorPanelCostView(View):
    def get(self, request):
        form = FloorPanelCostForm()

        return render(request, 'renovation_costs/floor_panel_cost_view.html', {'form': form})

    def post(self, request):
        form = FloorPanelCostForm(request.POST)
        if form.is_valid():
            floor_area = form.cleaned_data['floor_area']
            room_circuit = form.cleaned_data['room_circuit']
            board = form.cleaned_data['board']
            floor_panel = form.cleaned_data['floor_panel']
            floor_panel_bed = form.cleaned_data['floor_panel_bed']
            foil = form.cleaned_data['foil']

            chosen_floor_panel = Product.objects.get(pk=floor_panel)
            chosen_floor_panel_bed = Product.objects.get(pk=floor_panel_bed)
            chosen_foil = Product.objects.get(pk=foil)
            chosen_board = Product.objects.get(pk=board)
            floor_panel_result = floor_area * (
                    chosen_floor_panel.price + chosen_floor_panel_bed.price + chosen_foil.price
            )
            board_result = math.ceil(room_circuit / chosen_board.usage_per_unit) * chosen_board.price

            ctx = {
                'costs_of_floor_panel': round(floor_panel_result, 2),
                'costs_of_board': round(board_result, 2),
                'chosen_floor_panel': chosen_floor_panel,
                'chosen_floor_panel_bed': chosen_floor_panel_bed,
                'chosen_foil': chosen_foil,
                'chosen_board': chosen_board,
            }

            return render(request, 'renovation_costs/floor_panel_cost_view_done.html', ctx)
