from rest_framework import serializers

from .models import (
    ProgramCategory,
    Program,
    LinuxDistribution,
    InitSystem,
    DisplayServerProtocol,
)


class ProgramCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramCategory
        fields = "__all__"


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"


class LinuxDistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinuxDistribution
        fields = "__all__"


class InitSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitSystem
        fields = "__all__"


class DisplayServerProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisplayServerProtocol
        fields = "__all__"
