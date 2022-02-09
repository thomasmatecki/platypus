import imp

from rest_framework import serializers

from spacejam import models


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Space
        fields = "__all__"
