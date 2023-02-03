from django_filters import rest_framework as filters
from .models import (
    MainEmotion,
    GeneralEmotion,
    GeneralEmotionLog,
    Habit,
    Event,
    Health
)

class MainEmotionFilter(filters.FilterSet):

    class Meta:
        model = MainEmotion
        fields = "__all__"

class GeneralEmotionFilter(filters.FilterSet):

    class Meta:
        model = GeneralEmotion
        fields = "__all__"

class GeneralEmotionLogFilter(filters.FilterSet):

    class Meta:
        model = GeneralEmotionLog
        fields = "__all__"

class HabitFilter(filters.FilterSet):

    class Meta:
        model = Habit
        fields = "__all__"

class EventFilter(filters.FilterSet):

    class Meta:
        model = Event
        fields = "__all__"

class HealthFilter(filters.FilterSet):

    class Meta:
        model = Health
        fields = "__all__"