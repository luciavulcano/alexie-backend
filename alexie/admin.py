from django.contrib import admin

from .models import (
    Event,
    EventLog,
    GeneralEmotion,
    GeneralEmotionLog,
    Habit,
    HabitLog,
    Health,
    HealthLog,
)

# Register your models here.
admin.site.register(GeneralEmotion)
admin.site.register(Health)
admin.site.register(Event)
admin.site.register(Habit)
admin.site.register(GeneralEmotionLog)
admin.site.register(EventLog)
admin.site.register(HabitLog)
admin.site.register(HealthLog)
