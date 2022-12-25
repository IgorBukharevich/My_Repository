from .models import RegistrationVisitors
from django.forms import ModelForm, TextInput, EmailInput, Select


class RegistrationVisitorsForm(ModelForm):
    class Meta:
        model = RegistrationVisitors
        fields = [
            'name_visitor',
            'last_name_visitor',
            'email_visitor',
            'title_movie',
            'data_time_show',
            'hall',
            'place',
        ]

        widgets = {
            'name_visitor': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'last_name_visitor': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
            }),
            'email_visitor': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'title_movie': Select(attrs={
                'id': 'select_title_movie',
                'class': 'form-control',
                'placeholder': 'Название фильма',
            }),
            'data_time_show': Select(attrs={
                'id': 'select_date_show',
                'class': 'form-control',
                'placeholder': 'Дата показа',
            }),
        }
