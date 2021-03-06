# Generated by Django 3.1.3 on 2021-02-07 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_auto_20210121_2322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendence',
            old_name='year',
            new_name='semester',
        ),
        migrations.RemoveField(
            model_name='student',
            name='year',
        ),
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(choices=[('MCA', 'MCA'), ('BCA', 'BCA'), ('PGDCA', 'PGDCA'), ('O Level', 'O Level')], max_length=100, null=True),
        ),
    ]
