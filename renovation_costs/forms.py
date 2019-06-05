from django import forms
import renovation_costs.choicefields as choices


class PaintingCostForm(forms.Form):
    running_metre = forms.DecimalField(label='Metry bieżące malowania [m]', min_value=0.01)
    flat_height = forms.DecimalField(label='Wysokość mieszkania [m]', min_value=2.5)
    ceiling_area = forms.DecimalField(label='Powierzchnia sufitów [m2]', min_value=0.1)
    slot_area = forms.DecimalField(label='Powierzchnia otworów', min_value=0.1, initial=0)
    paints = forms.ChoiceField(label='Farba', choices=choices.paints)
    bases = forms.ChoiceField(label='Grunt', choices=choices.bases)


class DoorWindowSizeCalc(forms.Form):
    window_height = forms.DecimalField(label='Wysokość [m]', min_value=0.1, required=False)
    window_weight = forms.DecimalField(label='Szerokość [m]', min_value=0.1, required=False)
