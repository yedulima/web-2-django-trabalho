from django import forms

class Temperature(forms.Form):
    CHOICES: list[tuple] = [
        ('Celsius', 'Celsius (°C)'),
        ('Fahrenheit', 'Fahrenheit (°F)'),
        ('Kelvin', 'Kelvin (K)'),
    ]

    first_choice = forms.ChoiceField(label="De", choices=CHOICES, widget=forms.Select(attrs={'style': 'font-size: .9em; border-radius: 4px;'}))
    second_choice = forms.ChoiceField(label="Para", choices=CHOICES, widget=forms.Select(attrs={'style': 'font-size: .9em; border-radius: 4px;'}))
    value = forms.FloatField(label="Valor", required=True, widget=forms.TextInput(attrs={'placeholder': 'Número', 'style': 'width: 150px; font-size: .9em; padding-left: 5px; border-radius: 4px;'}))

class Length(forms.Form):
    CHOICES: list[tuple] = [
        ('Metro', 'Metro (m)'),
        ('Centimetro', 'Centímetro (cm)'),
        ('Milimetro', 'Milímetro (mm)'),
    ]

    first_choice = forms.ChoiceField(label="De", choices=CHOICES, widget=forms.Select(attrs={'style': 'font-size: .9em; border-radius: 4px;'}))
    second_choice = forms.ChoiceField(label="Para", choices=CHOICES, widget=forms.Select(attrs={'style': 'font-size: .9em; border-radius: 4px;'}))
    value = forms.FloatField(label="Valor", required=True, widget=forms.TextInput(attrs={'placeholder': 'Número', 'style': 'width: 150px; font-size: .9em; padding-left: 5px; border-radius: 4px;'}))

class Weight(forms.Form):
    CHOICES: list[tuple] = [
        ('Kilograma', 'Kilograma (kg)'),
        ('Grama', 'Grama (g)'),
    ]

    first_choice = forms.ChoiceField(label="De", choices=CHOICES, widget=forms.Select(attrs={'style': 'font-size: .9em; border-radius: 4px;'}))
    second_choice = forms.ChoiceField(label="Para", choices=CHOICES, widget=forms.Select(attrs={'style': 'font-size: .9em; border-radius: 4px;'}))
    value = forms.FloatField(label="Valor", required=True, widget=forms.TextInput(attrs={'placeholder': 'Número', 'style': 'width: 150px; font-size: .9em; padding-left: 5px; border-radius: 4px;'}))