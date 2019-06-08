from django import forms
import renovation_costs.choicefields as choices


class PaintingCostForm(forms.Form):
    running_metre = forms.DecimalField(label='Metry bieżące malowania [m]', min_value=0.01,
                                       help_text='Suma długości ścian do pomalowania')
    flat_height = forms.DecimalField(label='Wysokość mieszkania [m]', min_value=2.5)
    ceiling_area = forms.DecimalField(label='Powierzchnia sufitów [m2]', min_value=0.1)
    slot_area = forms.DecimalField(label='Powierzchnia otworów [m2]', min_value=0.1, initial=0,
                                   help_text='Suma powierzchni okien i drzwi')
    paints = forms.ChoiceField(label='Farba', choices=choices.paints)
    base = forms.ChoiceField(label='Grunt', choices=choices.bases)


class WallpaperCostForm(forms.Form):
    running_metre = forms.DecimalField(label='Metry bieżące tapetowania [m]', min_value=0.01,
                                       help_text='Suma długości ścian do pomalowania')
    flat_height = forms.DecimalField(label='Wysokość mieszkania [m]', min_value=2.5)
    slot_area = forms.DecimalField(label='Powierzchnia otworów [m2]', min_value=0.1, initial=0,
                                   help_text='Suma powierzchni okien i drzwi')
    wallpaper = forms.ChoiceField(label='Tapeta', choices=choices.wallpaper)
    glue = forms.ChoiceField(label='Klej do tapet', choices=choices.wallpaper_glue)


class SlotSizeCalc(forms.Form):
    window_height = forms.DecimalField(label='Wysokość [m]', min_value=0.1, required=False)
    window_weight = forms.DecimalField(label='Szerokość [m]', min_value=0.1, required=False)


class AreaSizeCalc(forms.Form):
    lenght = forms.DecimalField(label='Długość [m]', min_value=0.1, required=False)
    weight = forms.DecimalField(label='Szerokość [m]', min_value=0.1, required=False)


class CeramicGlazeCostForm(forms.Form):
    wall_running_metre = forms.DecimalField(label='Metry bieżące śćian [m]', decimal_places=2,
                                            help_text='Suma długości ścian do pomalowania')
    wall_height = forms.DecimalField(label='Wysokość powierzchni pod glazurę [m]', decimal_places=2)
    floor_area = forms.DecimalField(label='Powierzchnia podłogi [m2]', decimal_places=2, initial=0)
    slot_area = forms.DecimalField(label='Powierzchnia otworów [m2]', decimal_places=2, initial=0,
                                   help_text='Suma powierzchni okien i drzwi')
    wall_tiles = forms.ChoiceField(label='Płytki ścienne', choices=choices.wall_tiles)
    floor_tiles = forms.ChoiceField(label='Płytki podłogowe', choices=choices.floor_tiles)
    fugue = forms.ChoiceField(label='Fuga', choices=choices.fugue)
    silicone_running_metre = forms.DecimalField(label='Metry bieżące silikonowania [m]', decimal_places=2,
                                                help_text='Wlicz tutaj wszystkie łączenia powierzchni płytek '
                                                          'takie jak narożniki pomieszczeń, łaczenie płytek podłogowych'
                                                          ' i ściennych ')
    silicone = forms.ChoiceField(label='Silikon', choices=choices.silicone)


class PlasterCostForm(forms.Form):
    running_metre = forms.DecimalField(label='Metry bieżące szpachlowania [m]', min_value=0.01,
                                       help_text='Suma długości ścian do pomalowania')
    flat_height = forms.DecimalField(label='Wysokość mieszkania [m]', min_value=2.5)
    ceiling_area = forms.DecimalField(label='Powierzchnia sufitów [m2]', min_value=0.1)
    slot_area = forms.DecimalField(label='Powierzchnia otworów [m2]', min_value=0.1, initial=0,
                                   help_text='Suma powierzchni okien i drzwi')
    layers_of_plaster = forms.ChoiceField(label='Ile razy chcesz szpachlować ?', choices=choices.layers_of_plaster)
    plaster = forms.ChoiceField(label='Gładź szpachlowa', choices=choices.plaster)
    base = forms.ChoiceField(label='Grunt budowlany', choices=choices.plaster_base)


class FloorPanelCostForm(forms.Form):
    floor_area = forms.DecimalField(label='Powierzchnia podłogi [m2]', min_value=0.1)
    room_circuit = forms.DecimalField(label='Obwód pomieszczenia [m]', min_value=0.1)
    board = forms.ChoiceField(label='Listwa przypodłogowa', choices=choices.board)
    floor_panel = forms.ChoiceField(label='Panel podłogowy', choices=choices.floor_panels)
    floor_panel_bed = forms.ChoiceField(label='Podkład pod panele', choices=choices.floor_panel_bed)
    foil = forms.ChoiceField(label='Folia izolacyjna', choices=choices.foil)