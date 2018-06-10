import re
from datetime import datetime
from django import forms
from .models import Entidade, ContatoEntidade, Oficio

class FormEntidade(forms.ModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data

        if cleaned_data.get('inicio_mandato') > cleaned_data.get('fim_mandato'):
            raise forms.ValidationError('O inicio do mandato não pode ser posterior ao fim do mandato!')

    class Meta:
        model = Entidade
        exclude = []


class FormContatoEntidade(forms.ModelForm):

    def clean_telefone(self):
        data = re.sub('\D', '', self.cleaned_data.get('telefone', ''))

        if len(data) not in (10, 11):
            raise forms.ValidationError('Telefone inválido!')

        return data

    def clean_fax(self):
        data = re.sub('\D', '', self.cleaned_data.get('fax', ''))

        if len(data) not in (0, 10, 11):
            raise forms.ValidationError('Fax inválido!')

        return data

    def clean_whatsapp(self):
        data = re.sub('\D', '', self.cleaned_data.get('whatsapp', ''))

        if len(data) not in (0, 10, 11):
            raise forms.ValidationError('Whatsapp inválido!')

        return data

    def clean(self):
        cleaned_data = self.cleaned_data

        telefone = re.sub('\D', '', self.cleaned_data.get('telefone', ''))
        fax = re.sub('\D', '', self.cleaned_data.get('fax', ''))
        whatsapp = re.sub('\D', '', self.cleaned_data.get('whatsapp', ''))

        if telefone == fax or telefone == whatsapp or fax == whatsapp:
            raise forms.ValidationError('Telefones não devem ser iguais!')

        return cleaned_data

    class Meta:
        model = ContatoEntidade
        exclude = []


class FormOficio(forms.ModelForm):

    def clean_data(self):
        data = self.cleaned_data.get('data','')

        if datetime.now().today() > data:
            raise forms.ValidationError('O oficio não pode ser anterior a date atual!')

        return data

    class Meta:
        model = Oficio
        exclude = []