from alexie import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("main/health", views.MainHealthViewset)
router.register("main/emotions", views.MainEmotionViewSet)
router.register("general/emotions/logs", views.GeneralEmotionLogViewSet)
router.register("general/emotions", views.GeneralEmotionViewSet)
router.register("habits/logs", views.HabitLogViewSet)
router.register("habits", views.HabitViewSet)
router.register("events/logs", views.EventLogViewSet)
router.register("events", views.EventViewSet)
router.register("health/logs", views.HealthLogViewset)
router.register("health", views.HealthViewset)