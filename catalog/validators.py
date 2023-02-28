import re

from rest_framework import serializers


class PhoneValidator:
    def __call__(self, value):
        pattern = re.compile(r'^[78]\d{10}$')
        if not pattern.match(value):
            raise serializers.ValidationError(
                'Номер телефона должен начинаться с 7 или 8 и содержать 11 цифр'
            )
        return value


class NumbersPageValidator:
    def __call__(self, value):
        if value < 0:
            raise serializers.ValidationError(
                'Количество страниц не может быть отрицательным'
            )


