from django.db import models

# Create your models here.


class COVIDData(models.Model):
    id_registro = models.CharField(max_length=100, blank=True)
    origen = models.CharField(max_length=30, blank=True)
    sector = models.CharField(max_length=30, blank=True)
    entidad_um = models.CharField(max_length=2, blank=True)
    sexo = models.CharField(max_length=10, blank=True)
    entidad_nac = models.CharField(max_length=2, blank=True)
    entidad_res = models.CharField(max_length=2, blank=True)
    municipio_res = models.CharField(max_length=30, blank=True)
    tipo_paciente = models.CharField(max_length=30, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    fecha_sintomas = models.DateField(null=True, blank=True)
    fecha_def = models.DateField(null=True, blank=True)
    intubado = models.CharField(max_length=30, blank=True)
    neumonia = models.CharField(max_length=30, blank=True)
    edad = models.IntegerField(default=0)
    nacionalidad = models.CharField(max_length=30, blank=True)
    embarazo = models.CharField(max_length=30, blank=True)
    habla_lengua_indig = models.CharField(max_length=30, blank=True)
    indigena = models.CharField(max_length=30, blank=True)
    diabetes = models.CharField(max_length=30, blank=True)
    epoc = models.CharField(max_length=30, blank=True)
    asma = models.CharField(max_length=30, blank=True)
    inmusupr = models.CharField(max_length=30, blank=True)
    hipertension = models.CharField(max_length=30, blank=True)
    otra_com = models.CharField(max_length=30, blank=True)
    cardiovascular = models.CharField(max_length=30, blank=True)
    obesidad = models.CharField(max_length=30, blank=True)
    renal_cronica = models.CharField(max_length=30, blank=True)
    tabaquismo = models.CharField(max_length=30, blank=True)
    otro_caso = models.CharField(max_length=30, blank=True)
    toma_muestra_lab = models.CharField(max_length=2, blank=True)
    resultado_lab = models.CharField(max_length=30, blank=True)
    toma_muestra_antigeno = models.CharField(max_length=30, blank=True)
    resultado_antigeno = models.CharField(max_length=30, blank=True)
    clasificacion_final = models.CharField(max_length=200, blank=True)
    migrante = models.CharField(max_length=30, blank=True)
    pais_nacionalidad = models.CharField(max_length=30)
    pais_origen = models.CharField(max_length=30, blank=True)
    uci = models.CharField(max_length=30, blank=True)
    fecha_ingreso_yr = models.IntegerField(default=0)
    fecha_ingreso_mt = models.IntegerField(default=0)
    fecha_ingreso_dy = models.IntegerField(default=0)
    fecha_ingreso_wk = models.IntegerField(default=0)
    fecha_sintomas_yr = models.IntegerField(default=0)
    fecha_sintomas_mt = models.IntegerField(default=0)
    fecha_sintomas_dy = models.IntegerField(default=0)
    fecha_sintomas_wk = models.IntegerField(default=0)
    fecha_def_yr = models.IntegerField(blank=True, null=True, default=None)
    fecha_def_mt = models.IntegerField(blank=True, null=True, default=None)
    fecha_def_dy = models.IntegerField(blank=True, null=True, default=None)
    fecha_def_wk = models.IntegerField(blank=True, null=True, default=None)

    def __str__(self):
        return str(self.id_registro) + ": " + self.sexo + " - " + \
               self.municipio_res + ", " + self.entidad_res + " -- " + \
               self.fecha_ingreso.strftime("%Y-%m-%d") + " -- DEF" if self.fecha_def else ""

    class Meta:
        db_table = "covid_data"

