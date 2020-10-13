from django.core.exceptions import ValidationError

def phone_validator(value):
    if value[:2] in [f"0{i}" for i in range(1, 10)]:
        return value
    else:
        raise ValidationError("the format is not true")
