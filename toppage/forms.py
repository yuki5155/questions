from django import forms
from .models import Data, Convert


class DataForm(forms.ModelForm):
    class Meta:
        #ここにDataのmodelsを読みこむ
        model = Data
        #日にちは自動なのでいらない
        fields = ("name","food",)

class ConvertForm(forms.ModelForm):
    class Meta:
        model = Convert
        fields =('name',)