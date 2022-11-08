from django import forms
# [코드 작성] models.py의 Comment 모델 추가로 불러오기
from .models import Posting, Comment

class PostingForm(forms.ModelForm):
    title = forms.CharField(label='제목')
    content = forms.CharField(label='내용', strip=False, widget=forms.Textarea)

    class Meta:
        model = Posting
        fields = ['title', 'content',]

# [코드 작성] forms의 ModelForm을 상속받는 CommentForm 클래스 생성
# [코드 작성] label은 ''로 설정
# [코드 작성] models의 TextField는 forms의 CharField에 widget을 적용하여 구현
# [코드 작성] TextField에 attrs={'rows':2}를 적용하여 2줄로 설정
# [코드 작성] Meta 클래스를 정의하여 Comment 모델을 기반으로 하고, 어떤 필드를 form으로 사용할 것인지 지정
class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', strip=False, widget=forms.Textarea(attrs={'rows':2}))

    class Meta:
        model = Comment
        fields = ['content',]
