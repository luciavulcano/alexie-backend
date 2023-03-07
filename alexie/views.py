from rest_framework import viewsets
from .serializers import (
    MainEmotionSerializer,
    GeneralEmotionSerializer,
    GeneralEmotionLogSerializer,
    HabitSerializer,
    EventSerializer,
    HealthSerializer,
    HabitLogSerializer,
    EventLogSerializer,
    MainHealthSerializer,
    HealthLogSerializer
)
from .filters import (
    MainEmotionFilter,
    GeneralEmotionFilter,
    GeneralEmotionLogFilter,
    HabitFilter,
    EventFilter,
    HealthFilter,
    HabitLogFilter,
    EventLogFilter,
    HealthLogFilter,
    MainHealthFilter
)
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

class MainEmotionViewSet(viewsets.ModelViewSet):

    queryset = MainEmotion.objects.all()
    serializer_class = MainEmotionSerializer
    filterset_class = MainEmotionFilter

class GeneralEmotionViewSet(viewsets.ModelViewSet):

    queryset = GeneralEmotion.objects.all()
    serializer_class = GeneralEmotionSerializer
    filterset_class = GeneralEmotionFilter

class GeneralEmotionLogViewSet(viewsets.ModelViewSet):

    queryset = GeneralEmotionLog.objects.all()
    serializer_class = GeneralEmotionLogSerializer
    filterset_class = GeneralEmotionLogFilter

class HabitViewSet(viewsets.ModelViewSet):

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    filterset_class = HabitFilter

class HabitLogViewSet(viewsets.ModelViewSet):

    queryset = HabitLog.objects.all()
    serializer_class = HabitLogSerializer
    filterset_class = HabitLogFilter

class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_class = EventFilter

class EventLogViewSet(viewsets.ModelViewSet):

    queryset = EventLog.objects.all()
    serializer_class = EventLogSerializer
    filterset_class = EventLogFilter

class HealthViewset(viewsets.ModelViewSet):

    queryset = Health.objects.all()
    serializer_class = HealthSerializer
    filterset_class = HealthFilter

class HealthLogViewset(viewsets.ModelViewSet):

    queryset = HealthLog.objects.all()
    serializer_class = HealthLogSerializer
    filterset_class = HealthLogFilter

class MainHealthViewset(viewsets.ModelViewSet):

    queryset = MainHealth.objects.all()
    serializer_class = MainHealthSerializer
    filterset_class = MainHealthFilter