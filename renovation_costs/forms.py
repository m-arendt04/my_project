from django import forms
import renovation_costs.choicefields as choices


class PaintingCostForm(forms.Form):
    running_metre = forms.DecimalField(label='Metry bieżące malowania [m]', min_value=0.01)
    flat_height = forms.DecimalField(label='Wysokość mieszkania [m]', min_value=2.5)
    ceiling_area = forms.DecimalField(label='Powierzchnia sufitów [m2]', min_value=0.1)
    slot_area = forms.DecimalField(label='Powierzchnia otworów [m2]', min_value=0.1, initial=0)
    paints = forms.ChoiceField(label='Farba', choices=choices.paints)
    bases = forms.ChoiceField(label='Grunt', choices=choices.bases)


class WallpaperCostForm(forms.Form):
    running_metre = forms.DecimalField(label='Metry bieżące tapetowania [m]', min_value=0.01)
    flat_height = forms.DecimalField(label='Wysokość mieszkania [m]', min_value=2.5)
    slot_area = forms.DecimalField(label='Powierzchnia otworów [m2]', min_value=0.1, initial=0)
    wallpaper = forms.ChoiceField(label='Tapeta', choices=choices.wallpaper)
    glue = forms.ChoiceField(label='Klej do tapet', choices=choices.wallpaper_glue)


class SlotSizeCalc(forms.Form):
    window_height = forms.DecimalField(label='Wysokość [m]', min_value=0.1, required=False)
    window_weight = forms.DecimalField(label='Szerokość [m]', min_value=0.1, required=False)


class AreaSizeCalc(forms.Form):
    lenght = forms.DecimalField(label='Długość [m]', min_value=0.1, required=False)
    weight = forms.DecimalField(label='Szerokość [m]', min_value=0.1, required=False)


class CeramicGlazeCostForm(forms.Form):
    wall_running_metre = forms.DecimalField(label='Metry bieżące śćian [m]', decimal_places=2)
    wall_height = forms.DecimalField(label='Wysokość powierzchni pod glazurę [m]', decimal_places=2)
    floor_area = forms.DecimalField(label='Powierzchnia podłogi [m2]', decimal_places=2, initial=0)
    slot_area = forms.DecimalField(label='Powierzchnia otworów [m2]', decimal_places=2, initial=0)
    wall_tiles = forms.ChoiceField(label='Płytki ścienne', choices=choices.wall_tiles)
    floor_tiles = forms.ChoiceField(label='Płytki podłogowe', choices=choices.floor_tiles)
    fugue = forms.ChoiceField(label='Fuga', choices=choices.fugue)
    silicone = forms.ChoiceField(label='Silikon', choices=choices.silicone)