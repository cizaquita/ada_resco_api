from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    url = models.CharField(max_length=150, verbose_name='Url')
    content = models.TextField(verbose_name='Post')

    def __unicode__(self):
        return self.title

class Faction(models.Model):
    name = models.CharField(max_length=40, verbose_name='Nombre')
    image = models.ImageField(upload_to="factions",blank=True,null=True, verbose_name='Imagen/Logo')

    def __unicode__(self):
        return self.name

class Agent(models.Model):
    name = models.CharField(max_length=40, verbose_name='Nombre')
    faction = models.ForeignKey(Faction,blank=True,null=True)
    city = models.CharField(max_length=40, verbose_name='Ciudad')
    verified = models.BooleanField(blank=True,default=False, verbose_name='Verificado')
    ingress_nick = models.CharField(max_length=30, verbose_name='Ingress Nick')
    ingress_level = models.IntegerField(default=0, verbose_name='Ingress Nivel')
    telegram_nick = models.CharField(max_length=30, verbose_name='Telegram Nick')
    telegram_id = models.IntegerField(default=0, verbose_name='Telegram ID')
    geo_latitude = models.CharField(max_length=100,default="",blank=True,null=True, verbose_name='Latitud')
    geo_longitude = models.CharField(max_length=100,default="",blank=True,null=True, verbose_name='Longitud')

    def __unicode__(self):
        return self.ingress_nick
