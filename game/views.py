from django.shortcuts import render, redirect
from random import *
from .models import Weapon
# [미션] forms.py의 WeaponForm 불러오기
from .forms import WeaponForm

# Create your views here.
win = 0
draw = 0
lose = 0

def game_list(request):
    return render(request, 'game/game_list.html')

def rsp_select(request):
    global win, draw, lose
    context = {
        'win': win,
        'draw': draw,
        'lose': lose,
    }
    return render(request, 'game/rsp_select.html', context)

def rsp_result(request, pick):
    global win, draw, lose
    rsp = ['가위', '바위', '보']
    com = choice(rsp)

    if pick == com:
        result = '무승부'
        draw += 1
    elif (pick == '가위' and com == '보') or (pick == '바위' and com == '가위') or (pick == '보' and com == '바위'):
        result = '승리'
        win += 1
    else :
        result = '패배'
        lose += 1

    context = {
        'pick': pick,
        'com': com,
        'result': result,
        'win': win,
        'draw': draw,
        'lose': lose,
    }
    return render(request, 'game/rsp_result.html', context)

def rsp_reset(request):
    global win, draw, lose
    win, draw, lose = 0, 0, 0
    return redirect('game:rsp_select')

def weapon_create(request):
    if request.method == 'POST':
        # [미션] request.POST 방식으로 전달된 값이 저장되는 WeaponForm 객체 생성
        # [미션] None을 지우고 작성
        weapon_form = WeaponForm(request.POST)
        
        # [미션] WeaponForm으로 넘어온 값이 유효한지 is_valid()를 이용하여 확인
        # [미션] None을 지우고 작성
        if weapon_form.is_valid():
            # [미션] weapon_form을 저장
            weapon_form.save()
            return redirect('game:weapon_list')
    else:
        # [미션] WeaponForm 객체 생성
        # [미션] None을 지우고 작성
        weapon_form = WeaponForm()
    
    context = {
        # [미션] weapon_form을 딕셔너리 형식으로 html에 넘겨주기
        # [미션] None을 지우고 작성
        'weapon_form': weapon_form,
    }
    return render(request, 'game/weapon_form.html', context)

def weapon_list(request):
    weapons = Weapon.objects.all()

    # [미션] default_weapons 딕셔너리 자유롭게 수정하기 (형식 : {'무기 이름' : 무기 공격력})
    default_weapons = {
        '주먹도끼': 1,
        '수상한 막대기': 7,
        '낡은 검': 5,
        '가벼운 물총': 3,
        '수학의 정석': 9,
    }
    
    if len(weapons) == 0:
        # [미션] 반복문을 이용해 default_weapons의 key값을 name, value값을 power로 Weapon 객체 생성 (Django ORM)
        # [미션] None을 지우고 작성
        for weapon in default_weapons:
            Weapon.objects.create(
                name = weapon,
                power = default_weapons[weapon],
            )
        # 모든 Weapon 객체들을 다시 불러오기
        weapons = Weapon.objects.all()

    context = {
        'weapons': weapons,
    }
    return render(request, 'game/weapon_list.html', context)
