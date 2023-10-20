from django.core.exceptions import ValidationError


def validate_title_words(title):
    result = len(title.split())

    if result <= 1:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")
