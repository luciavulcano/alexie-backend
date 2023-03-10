from rest_framework import serializers
from django.contrib.auth import get_user_model
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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "first_name", "last_name")


class MainEmotionSerializer(serializers.ModelSerializer):

    created_by = UserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = MainEmotion
        fields = "__all__"


class GeneralEmotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneralEmotion
        fields = "__all__"


class GeneralEmotionLogSerializer(serializers.ModelSerializer):

    created_by = UserSerializer(default=serializers.CurrentUserDefault())
    class Meta:
        model = GeneralEmotionLog
        fields = "__all__"
    def to_representation(self, instance):
        self.fields['emotion'] = GeneralEmotionSerializer(read_only=True)
        return super().to_representation(instance)

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

    created_by = UserSerializer(default=serializers.CurrentUserDefault())

    class Meta:
        model = MainHealth
        fields = "__all__"


class HealthLogSerializer(serializers.ModelSerializer):

    created_by = UserSerializer(default=serializers.CurrentUserDefault())
    class Meta:
        model = HealthLog
        fields = "__all__"
    def to_representation(self, instance):
        self.fields['health'] = HealthSerializer(read_only=True)
        return super().to_representation(instance)

class EventLogSerializer(serializers.ModelSerializer):

    created_by = UserSerializer(default=serializers.CurrentUserDefault())
    class Meta:
        model = EventLog
        fields = "__all__" 
    def to_representation(self, instance):
        self.fields['event'] = EventSerializer(read_only=True)
        return super().to_representation(instance)

class HabitLogSerializer(serializers.ModelSerializer):

    created_by = UserSerializer(default=serializers.CurrentUserDefault())
    class Meta:
        model = HabitLog
        fields = "__all__"  
    def to_representation(self, instance):
        self.fields['habit'] = HabitSerializer(read_only=True)
        return super().to_representation(instance)
