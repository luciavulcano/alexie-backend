from django.contrib.auth import get_user_model
from django.db import models


class MainEmotion(models.Model):

    description = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    created_by = models.ForeignKey(
        get_user_model(),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    created_in = models.DateTimeField(
        auto_now_add=True,
    )


class GeneralEmotion(models.Model):

    description = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    created_in = models.DateTimeField(
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )


class GeneralEmotionLog(models.Model):

    created_in = models.DateTimeField(
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        get_user_model(),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    emotion = models.ForeignKey(
        GeneralEmotion,
        related_name="logs",
        null=False,
        blank=False,
        on_delete=models.PROTECT,
    )


class Habit(models.Model):

    description = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    created_in = models.DateTimeField(
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )


class HabitLog(models.Model):

    created_in = models.DateTimeField(
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        get_user_model(),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    habit = models.ForeignKey(
        Habit,
        related_name="logs",
        null=False,
        blank=False,
        on_delete=models.PROTECT,
    )


class Event(models.Model):

    created_by = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    description = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    created_in = models.DateTimeField(
        auto_now_add=True,
    )


class EventLog(models.Model):

    created_in = models.DateTimeField(
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        get_user_model(),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    event = models.ForeignKey(
        Event,
        related_name="logs",
        null=False,
        blank=False,
        on_delete=models.PROTECT,
    )


class MainHealth(models.Model):

    description = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    created_by = models.ForeignKey(
        get_user_model(),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    created_in = models.DateTimeField(
        auto_now_add=True,
    )


class Health(models.Model):

    created_by = models.ForeignKey(
        get_user_model(),
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    description = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )
    created_in = models.DateTimeField(
        auto_now_add=True,
    )


class HealthLog(models.Model):

    created_in = models.DateTimeField(
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        get_user_model(),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    health = models.ForeignKey(
        Health,
        related_name="logs",
        null=False,
        blank=False,
        on_delete=models.PROTECT,
    )
