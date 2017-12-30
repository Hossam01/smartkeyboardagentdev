from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = "__all__"


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Themes
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ThemePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemePhoto
        fields = "__all__"

class CitySerlaizer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class AdvertiserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertiser
        fields = "__all__"

class TypedWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypedWords
        fields = "__all__"

class AcceptedAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcceptedAdvertisement
        fields = "__all__"


class RejectedAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = RejectedAdvertisement
        fields = "__all__"

