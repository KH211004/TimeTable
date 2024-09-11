# Generated by Django 5.0.7 on 2024-09-10 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fac_id', models.IntegerField(null=True)),
                ('faculty_name', models.CharField(max_length=10)),
                ('theory_hours', models.IntegerField()),
                ('practical_hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Friday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1', models.CharField(max_length=100)),
                ('slot2', models.CharField(max_length=100)),
                ('slot3', models.CharField(max_length=100)),
                ('slot4', models.CharField(max_length=100)),
                ('slot5', models.CharField(max_length=100)),
                ('slot6', models.CharField(max_length=100)),
                ('slot7', models.CharField(max_length=100)),
                ('slot8', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LoadAllocate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=10, null=True)),
                ('theory_hours', models.IntegerField()),
                ('pract_hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Monday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1', models.CharField(max_length=100)),
                ('slot2', models.CharField(max_length=100)),
                ('slot3', models.CharField(max_length=100)),
                ('slot4', models.CharField(max_length=100)),
                ('slot5', models.CharField(max_length=100)),
                ('slot6', models.CharField(max_length=100)),
                ('slot7', models.CharField(max_length=100)),
                ('slot8', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sem_4_C',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1', models.CharField(max_length=100)),
                ('slot2', models.CharField(max_length=100)),
                ('slot3', models.CharField(max_length=100)),
                ('slot4', models.CharField(max_length=100)),
                ('slot5', models.CharField(max_length=100)),
                ('slot6', models.CharField(max_length=100)),
                ('slot7', models.CharField(max_length=100)),
                ('slot8', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sem_4_C_lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch1', models.CharField(max_length=500)),
                ('batch2', models.CharField(max_length=500)),
                ('batch3', models.CharField(max_length=500)),
                ('batch4', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Sem_4_D',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1', models.CharField(max_length=100)),
                ('slot2', models.CharField(max_length=100)),
                ('slot3', models.CharField(max_length=100)),
                ('slot4', models.CharField(max_length=100)),
                ('slot5', models.CharField(max_length=100)),
                ('slot6', models.CharField(max_length=100)),
                ('slot7', models.CharField(max_length=100)),
                ('slot8', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sem_4_D_lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch1', models.CharField(max_length=500)),
                ('batch2', models.CharField(max_length=500)),
                ('batch3', models.CharField(max_length=500)),
                ('batch4', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Sem_6_C',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1', models.CharField(max_length=100)),
                ('slot2', models.CharField(max_length=100)),
                ('slot3', models.CharField(max_length=100)),
                ('slot4', models.CharField(max_length=100)),
                ('slot5', models.CharField(max_length=100)),
                ('slot6', models.CharField(max_length=100)),
                ('slot7', models.CharField(max_length=100)),
                ('slot8', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sem_6_C_lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch1', models.CharField(max_length=500)),
                ('batch2', models.CharField(max_length=500)),
                ('batch3', models.CharField(max_length=500)),
                ('batch4', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Sem_6_D',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1', models.CharField(max_length=100)),
                ('slot2', models.CharField(max_length=100)),
                ('slot3', models.CharField(max_length=100)),
                ('slot4', models.CharField(max_length=100)),
                ('slot5', models.CharField(max_length=100)),
                ('slot6', models.CharField(max_length=100)),
                ('slot7', models.CharField(max_length=100)),
                ('slot8', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sem_6_D_lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch1', models.CharField(max_length=500)),
                ('batch2', models.CharField(max_length=500)),
                ('batch3', models.CharField(max_length=500)),
                ('batch4', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('sub_name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('semester', models.IntegerField()),
                ('theory_hours', models.IntegerField()),
                ('practical_hours', models.IntegerField()),
                ('allocated', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Thursday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1', models.CharField(max_length=100)),
                ('slot2', models.CharField(max_length=100)),
                ('slot3', models.CharField(max_length=100)),
                ('slot4', models.CharField(max_length=100)),
                ('slot5', models.CharField(max_length=100)),
                ('slot6', models.CharField(max_length=100)),
                ('slot7', models.CharField(max_length=100)),
                ('slot8', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tuesday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1', models.CharField(max_length=100)),
                ('slot2', models.CharField(max_length=100)),
                ('slot3', models.CharField(max_length=100)),
                ('slot4', models.CharField(max_length=100)),
                ('slot5', models.CharField(max_length=100)),
                ('slot6', models.CharField(max_length=100)),
                ('slot7', models.CharField(max_length=100)),
                ('slot8', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Wednesday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot1', models.CharField(max_length=100)),
                ('slot2', models.CharField(max_length=100)),
                ('slot3', models.CharField(max_length=100)),
                ('slot4', models.CharField(max_length=100)),
                ('slot5', models.CharField(max_length=100)),
                ('slot6', models.CharField(max_length=100)),
                ('slot7', models.CharField(max_length=100)),
                ('slot8', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=15)),
                ('slot', models.CharField(max_length=5)),
                ('availability', models.IntegerField()),
                ('faculty_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable_app.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='LabAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('slot', models.CharField(max_length=5)),
                ('batch', models.CharField(max_length=5)),
                ('lab_no', models.CharField(max_length=5)),
                ('sem', models.IntegerField()),
                ('division', models.CharField(max_length=2)),
                ('faculty_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable_app.faculty')),
                ('sub_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable_app.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty_Subject_Totalhours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_hours', models.IntegerField()),
                ('faculty_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable_app.faculty')),
                ('sub_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable_app.subject')),
            ],
        ),
        migrations.AddField(
            model_name='faculty',
            name='sub_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable_app.subject'),
        ),
        migrations.CreateModel(
            name='TheoryAllocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=15)),
                ('faculty_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable_app.faculty')),
                ('sub_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetable_app.subject')),
            ],
        ),
    ]