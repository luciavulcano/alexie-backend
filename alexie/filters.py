from django_filters import rest_framework as filters
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

class HabitLogFilter(filters.FilterSet):

    class Meta:
        model = HabitLog
        fields = "__all__"

class EventLogFilter(filters.FilterSet):

    class Meta:
        model = EventLog
        fields = "__all__"

class MainHealthFilter(filters.FilterSet):

    class Meta:
        model = MainHealth
        fields = "__all__"

class HealthLogFilter(filters.FilterSet):

    class Meta:
        model = HealthLog
        fields = "__all__"