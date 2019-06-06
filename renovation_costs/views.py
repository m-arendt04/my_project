from django.shortcuts import render
from django.views import View

from renovation_costs.forms import PaintingCostForm, SlotSizeCalc, WallpaperCostForm
from renovation_costs.models import Paint, Base, Wallpaper, WallpaperGlue


class RenovationCategoriesView(View):
    def get(self, request):
        return render(request, 'renovation_costs/renovation_cost_main.html')


class PaintingCostView(View):
    def get(self, request):
        form = PaintingCostForm()
        form_calc = SlotSizeCalc()
        ctx = {
            'form': form,
            'form_door_window_calc': form_calc
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
            base = form.cleaned_data['bases']

            paint_area = running_metre * flat_height + ceiling_area - slot_area
            chosen_paint = Paint.objects.get(pk=paint)
            chosen_base = Base.objects.get(pk=base)

            result_of_paint = round(paint_area / chosen_paint.production_per_litr / chosen_paint.capacity, 0) \
                              * chosen_paint.price
            result_of_base = round(paint_area / chosen_base.production_per_litr / chosen_base.capacity, 0) \
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
            chosen_wallpaper = Wallpaper.objects.get(pk=wallpaper)
            chosen_glue = WallpaperGlue.objects.get(pk=glue)

            result_of_wallpaper = round(wallpaper_area / chosen_wallpaper.capacity, 0) * chosen_wallpaper.price
            result_of_glue = round(wallpaper_area/chosen_glue.usage, 0) * chosen_glue.price

            ctx = {
                'costs_of_wallpaper': round(result_of_wallpaper, 2),
                'costs_of_glue': round(result_of_glue, 2),
                'chosen_wallpaper': chosen_wallpaper,
                'chosen_glue': chosen_glue,
            }
            return render(request, 'renovation_costs/wallpaper_cost_view_done.html', ctx)

