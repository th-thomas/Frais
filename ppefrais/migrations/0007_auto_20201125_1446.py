# Generated by Django 3.1.3 on 2020-11-25 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ppefrais', '0006_auto_20201118_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statut',
            fields=[
                ('statutId', models.AutoField(primary_key=True, serialize=False)),
                ('statutLibelle', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameField(
            model_name='visiteur',
            old_name='date_embauhe',
            new_name='date_embauche',
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statutId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ppefrais.statut')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]