
from django.contrib import admin
from info_academico.models import Materia, Libro, Progreso

class LibroInline(admin.TabularInline):
    model= Libro
    extra=0

@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
   
    fieldsets= [

        ("Información General", {"fields": ["nombre", "profesor"]}),
    ]

    inlines = [LibroInline]
    list_display = ['nombre', 'profesor', 'upper_case_name']
    search_fields = ['nombre']
    ordering = ['nombre']

    @admin.display(description='Nombre en MAYÚSCULA')
    def upper_case_name(self, obj):
        return obj.nombre.upper()


@admin.register(Progreso)
class ProgresoAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Fechas", {"fields": ["fecha_parcial1", "fecha_parcial2", "fecha_tp", "fecha_final", "fecha_final2"]}),
        ("Materia Relacionada", {"fields": ["materia"]}),
    ]
    list_display = ['materia', 'fecha_parcial1','fecha_parcial2', "fecha_tp",'fecha_final', 'fecha_final2']