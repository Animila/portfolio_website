from django.forms import ModelForm, TextInput, DateTimeInput, DateTimeField, Textarea, ImageField

from home.models import News


class NewsForm(ModelForm):

    widgets = {
        "title": TextInput(attrs={
            'placeholder': 'Заголовок новости',
            'id': "exampleFormControlInput1",
        }),
        'time': DateTimeField(),
        'description': Textarea(attrs={
            'id': "exampleFormControlTextarea1"
        }),
        'image': ImageField(allow_empty_file=True)
    }

    class Meta:
        model = News
        fields = ('title', 'time', 'description', 'image')

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        for filed_name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control rounded-0"
