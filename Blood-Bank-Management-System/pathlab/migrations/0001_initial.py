# Generated by Django 2.1.2 on 2018-12-12 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0011_auto_20181212_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='PathLabUser2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=1000)),
                ('lastname', models.CharField(max_length=1000, null=True)),
                ('address', models.CharField(max_length=1000)),
                ('bloodgroup', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=3)),
                ('testtype', models.CharField(choices=[('Regular Checkup1', 'Regular Checkup1'), ('Regular Checkup2', 'Regular Checkup2'), ('Regular Checkup3', 'Regular Checkup3')], max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('Result', models.CharField(default='NA', max_length=1000)),
                ('feedback', models.CharField(default='NA', max_length=1000)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.UserProfile')),
            ],
        ),
    ]
