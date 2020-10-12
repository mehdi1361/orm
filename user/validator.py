from django.core.exceptions import ValidationError

def phone_validator(value):
    if value.startwith('01'):
        return value

    elif value.startwith('09'):
        return value

    else:
        raise ValidationError("the format is not true")
