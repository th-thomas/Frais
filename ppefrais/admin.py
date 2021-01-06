from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser, FicheFrais, FraisForfait, LigneFraisHorsForfait, Etat


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser


class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('statut', 'adresse', 'code_postal', 'date_embauche',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(FicheFrais),
admin.site.register(LigneFraisHorsForfait),
admin.site.register(FraisForfait),
admin.site.register(Etat)
