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

    class Meta:
        verbose_name = "Faction"
        verbose_name_plural = "Factions"

    def __unicode__(self):
        return self.name

class Agent(models.Model):
    name = models.CharField(max_length=40, verbose_name='Nombre')
    profile_picture = models.CharField(max_length=100,default="",blank=True,null=True, verbose_name='Foto Perfil')
    faction = models.ForeignKey(Faction,blank=True,null=True)
    city = models.CharField(max_length=40, verbose_name='Ciudad')
    verified = models.BooleanField(blank=True,default=False, verbose_name='Verificado')
    verified_for = models.CharField(max_length=50,default="",blank=True,null=True, verbose_name='Verificado Por')
    # Nivel de verificación: 0 ninguno, 1 perfil agente, 2 en persona, 3 para OPS, 1337 cizaquita amo y senior de ADA xD!
    verified_level = models.IntegerField(default=0, verbose_name='Nivel de verificación')
    ingress_nick = models.CharField(max_length=30, verbose_name='Ingress Nick')
    ingress_level = models.IntegerField(default=0, verbose_name='Ingress Nivel')
    telegram_nick = models.CharField(max_length=30, verbose_name='Telegram Nick')
    telegram_id = models.IntegerField(default=0, verbose_name='Telegram ID')
    geo_latitude = models.CharField(max_length=100,default="",blank=True,null=True, verbose_name='Latitud')
    geo_longitude = models.CharField(max_length=100,default="",blank=True,null=True, verbose_name='Longitud')
    trivia_points = models.IntegerField(default=0, verbose_name='Puntos Trivia')


    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agents"

    def __unicode__(self):
        return self.ingress_nick