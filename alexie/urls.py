from alexie import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("main/emotions", views.MainEmotionViewSet)
router.register("general/emotions/logs", views.GeneralEmotionLogViewSet)
router.register("general/emotions", views.GeneralEmotionViewSet)
router.register("habits", views.HabitViewSet)
router.register("events", views.EventViewSet)
router.register("health", views.HealthViewset)