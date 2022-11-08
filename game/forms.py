from django import forms
# [미션] models.py의 Weapon 모델 불러오기
from .models import Weapon

# [미션] forms의 ModelForm을 상속받는 WeaponForm 클래스 생성
# [미션] name 필드는 forms의 CharField로 생성 (label: '무기 이름')
# [미션] power 필드는 forms의 IntegerField로 생성 (label: '무기 공격력')
# [미션] WeaponForm 안에 Meta 클래스를 정의하여 model은 Weapon, fields는 Weapon 모델의 모든 필드로 지정
class WeaponForm(forms.ModelForm):
    name = forms.CharField(label='무기 이름')
    power = forms.IntegerField(label='무기 공격력')

    class Meta:
        model = Weapon
        fields = '__all__'
