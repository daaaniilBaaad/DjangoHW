from django.core.exceptions import ValidationError
from django.forms import ModelForm

from blog.models import BlogPost


BANNED_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]

class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content',)

    def clean_title(self):
        title = self.cleaned_data['title']
        for word in BANNED_WORDS:
            if word.lower() in title.lower():
                raise ValidationError(f"Название содержит запрещённое слово: «{word}»")
        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        for word in BANNED_WORDS:
            if word.lower() in content.lower():
                raise ValidationError(f"Содержимое содержит запрещённое слово: «{word}»")
        return content
