from django.db import models
from news.models.user_model import Users
from news.models.category_model import Categories
from news.models.validators import validate_title_words


class News(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[validate_title_words]
    )
    content = models.TextField()
    author = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="news"
    )
    created_at = models.DateField()
    image = models.ImageField(
        upload_to="img", null=True, blank=True
    )
    categories = models.ManyToManyField(
        Categories,
        related_name="news"
    )

    def __str__(self):
        return self.title
