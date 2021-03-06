# Generated by Django 3.2.8 on 2021-11-13 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_auto_20211112_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto_Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('valor_total', models.FloatField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.cliente')),
                ('id_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.produto')),
            ],
        ),
    ]
