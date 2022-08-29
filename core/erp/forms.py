from django.forms import *
from .models import Category


class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # faço um for para colocar atributos\ classes que são iguais em todos itens do formularios
        for form in self.visible_fields():
             form.field.widget.attrs.update({'class': 'special'})
        
        self.fields['name'].widget.attrs['autofocus'] = True



    class Meta:
        model = Category
        fields = '__all__'
        #exclude = ['name']
        labels = {
            'name' : 'Nome',
            'desc': 'Descrição'
        }
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Entre com seu nome'
                }
            ),

            'desc' : Textarea(
             attrs={
                    'rows': 3,
                    'cols': 3
                }

            )
        }