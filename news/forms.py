from django import forms
from news.models.category_model import Categories
from news.models.news_model import News


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "Nome"


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Título"
        self.fields["content"].label = 'Conteúdo'
        self.fields["author"].label = 'Autoria'
        self.fields["image"].label = 'URL da Imagem'
        self.fields["created_at"].label = 'Criado em'
        self.fields["created_at"].widget = forms.DateInput(
                attrs={"type": "date"})
        self.fields["categories"].widget = forms.CheckboxSelectMultiple(
            choices=[
                (category.id, category.name)
                for category in Categories.objects.all()
            ]
        )
