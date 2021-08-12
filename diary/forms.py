from django import forms
from django.core.exceptions import ValidationError

from .models import Page


class PageForm(forms.ModelForm):
    # memo = forms.CharField(max_length=80, validators=[validate_no_hash])

    class Meta:
        model = Page
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data['title']
        if '*' in title:
            raise ValidationError('*는 포함 될 수 없습니다')

        return title



    # title = forms.CharField(max_length=100, label='제목')
    # content = forms.CharField(widget=forms.Textarea, label='내용')
    # feeling = forms.CharField(max_length=80, label='감정 상태')
    # score = forms.IntegerField(label='감정 점수')
    # dt_created = forms.DateField(label='작성일')
