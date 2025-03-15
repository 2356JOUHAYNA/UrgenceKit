# Generated by Django 4.2.9 on 2024-04-30 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_numerourgence_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='Default Kit Name', max_length=100)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('purchase_count', models.IntegerField(default=0)),
                ('item1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kit_item1', to='home.product')),
                ('item2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kit_item2', to='home.product')),
                ('item3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kit_item3', to='home.product')),
                ('item4', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kit_item4', to='home.product')),
                ('item5', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kit_item5', to='home.product')),
                ('item6', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kit_item6', to='home.product')),
                ('magazin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.magazin')),
            ],
        ),
    ]
