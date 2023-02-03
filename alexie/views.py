from rest_framework import viewsets
from .serializers import (
    MainEmotionSerializer,
    GeneralEmotionSerializer,
    GeneralEmotionLogSerializer,
    HabitSerializer,
    EventSerializer,
    HealthSerializer,
)
from .filters import (
    MainEmotionFilter,
    GeneralEmotionFilter,
    GeneralEmotionLogFilter,
    HabitFilter,
    EventFilter,
    HealthFilter,
)
from .models import (
    MainEmotion,
    GeneralEmotion,
    GeneralEmotionLog,
    Habit,
    Event,
    Health
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

class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filterset_class = EventFilter

class HealthViewset(viewsets.ModelViewSet):

    queryset = Health.objects.all()
    serializer_class = HealthSerializer
    filterset_class = HealthFilter