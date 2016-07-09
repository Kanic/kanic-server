from rest_framework import serializers

from .models import Make, Model


class ModelRetrieveSerializer(serializers.ModelSerializer):
    make_id = serializers.PrimaryKeyRelatedField(queryset=Make.objects.all())
    make_name = serializers.CharField(source='make.name')
    class Meta:
        model = Model
        fields = (
            'id',
            'make_name',
            'make_id',
            'name',
            'niceName',
            'years'
        )


class ModelListSerializer(serializers.ModelSerializer):
    make_id = serializers.PrimaryKeyRelatedField(queryset=Make.objects.all())
    make = serializers.CharField(source='make.name')
    class Meta:
        model = Model
        fields = (
            'id',
            'make',
            'make_id',
            'name',
            'niceName',
            'years'
        )


class MakeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Make
        fields = (
            'id',
            'name',
            'niceName'
        )


class MakeListWithModelsSerializer(serializers.ModelSerializer):
    model_set = ModelRetrieveSerializer(many=True, read_only=True)
    class Meta:
        model = Make
        fields = (
            'id',
            'name',
            'niceName',
            'model_set'
        )
        depth = 1
