from django import forms
from .models import Video

class UploadFileForm(forms.Form):
    class Meta:
        model=Video
        label='파일을 선택해주세요.'
        fields = ["docfile"]

        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['docfile'].required = False