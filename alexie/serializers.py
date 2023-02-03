from rest_framework import serializers
from .models import (
    MainEmotion,
    GeneralEmotion,
    GeneralEmotionLog,
    Habit,
    Event,
    Health
)


class MainEmotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MainEmotion

class GeneralEmotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneralEmotion

class GeneralEmotionLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneralEmotionLog

class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event

class HealthSerializer(serializers.ModelSerializer):

    class Meta:
        model = Health