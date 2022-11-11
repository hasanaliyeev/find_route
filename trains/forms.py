from django import forms

from cities.models import City
from trains.models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название поезда'
    }))
    travel_time = forms.IntegerField(label='Время поезда', widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
    from_city = forms.ModelChoiceField(queryset=City.objects.all(), label='Откуда', widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    to_city = forms.ModelChoiceField(queryset=City.objects.all(), label='Куда', widget=forms.Select(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Train
        fields = '__all__'
