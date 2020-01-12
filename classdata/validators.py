from django.core.exceptions import ObjectDoesNotExist, ValidationError, MultipleObjectsReturned
from django.utils.deconstruct import deconstructible

@deconstructible
class CharFieldValidator:
    """
    class validator fo validating string should have char or spaces
    """
    def __call__(self, data):
        if data and not all(ch.isalpha() or ch.isspace() for ch in data):
            msg = "This field should have only character or spaces"
            raise ValidationError(msg)
