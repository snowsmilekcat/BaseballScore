from django import forms

from .models import User#modelsファイルからUserモデルのインポート

class UserForm(forms.ModelForm):#Djangoモデルに対応したFormを自動で生成する。
    class Meta:
        model = User
        fields = ['name', 'back_number','position','sub_position']
