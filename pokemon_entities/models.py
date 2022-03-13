from django.db import models


class Pokemon(models.Model):
    title = models.CharField("Имя покемона на русском", max_length=200)
    title_en = models.CharField("Имя покемона на английском", max_length=200, blank=True)
    title_jp = models.CharField("Имя покемона на японском", max_length=200, blank=True)
    image = models.ImageField("Изображение покемона", blank=True, null=True)
    text = models.TextField("Описание покемона", blank=True)
    previous_evolution = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Эволюция", related_name="next_evolution"
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon, verbose_name="Покемон", on_delete=models.CASCADE
    )
    lat = models.FloatField("Широта")
    lon = models.FloatField("Долгота")
    appeared_at = models.DateTimeField("Время появления", null=True, blank=True)
    disappeared_at = models.DateTimeField("Время исчезновения", null=True, blank=True,)
    level = models.IntegerField("Уровень", blank=True, null=True)
    health = models.IntegerField("Количество здоровья", blank=True, null=True)
    strength = models.IntegerField("Сила", blank=True, null=True)
    defence = models.IntegerField("Защита", blank=True, null=True)
    stamina = models.IntegerField("Выносливость", blank=True, null=True)

    def __str__(self):
        return self.pokemon.title
