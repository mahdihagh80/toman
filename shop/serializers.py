from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from shop.models import Product, ProductImage

from django.core.exceptions import ValidationError


def validate_image_size(image):
    max_size_kb = 2000
    if image.size > max_size_kb * 1024:
        raise ValidationError(f"Image file size must be less than {max_size_kb} KB.")


class ImageUploaderSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image']
        extra_kwargs = {'image': {'validators': [validate_image_size]}}

class ProductCreationSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']

    def to_internal_value(self, data):
        images = ProductImage.objects.filter(pk__in=data['images'])
        data.pop('images', None)
        data = super().to_internal_value(data)
        data['images'] = images
        return data

    def validate(self, data):
        if len(data.get('images', [])) > 5:
            raise ValidationError("You can add at most 5 images per product.")
        return data

    def create(self, validated_data):
        images = validated_data.pop('images')
        instance = super(ProductCreationSerializer, self).create(validated_data)
        for img in images:
            img.product = instance
            img.save()
        instance.all_images = images
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['images'] = [{'id': img.id, 'image_url': img.image.url} for img in instance.all_images]
        return data


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['title', 'description', 'price']

