# Generated by Django 5.0 on 2024-09-25 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobbies', '0005_alter_student_stumentor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('programmecode', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('programmename', models.TextField(max_length=50)),
                ('programmeaccdate', models.DateField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SHobby',
        ),
        migrations.AlterField(
            model_name='student',
            name='stumentor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hobbies.mentor'),
        ),
        migrations.AddField(
            model_name='student',
            name='stuprogramme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hobbies.programme'),
        ),
    ]
