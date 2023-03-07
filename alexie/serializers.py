from rest_framework import serializers
from .models import (
    MainEmotion,
    GeneralEmotion,
    GeneralEmotionLog,
    Habit,
    HabitLog,
    Event,
    EventLog,
    MainHealth,
    Health,
    HealthLog
)


class MainEmotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainEmotion
        fields = "__all__"

class GeneralEmotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneralEmotion
        fields = "__all__"

class GeneralEmotionLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneralEmotionLog
        fields = "__all__"

class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"

class HealthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Health
        fields = "__all__"

class MainHealthSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainHealth
        fields = "__all__"

class HealthLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = HealthLog
        fields = "__all__"

class EventLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventLog
        fields = "__all__"

class HabitLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = HabitLog
        fields = "__all__"