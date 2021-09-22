# Generated by Django 3.2.7 on 2021-09-22 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='native',
            name='cohort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.cohort'),
        ),
        migrations.AlterField(
            model_name='native',
            name='image',
            field=models.ImageField(default='', upload_to='./media/uploads/'),
        ),
        migrations.CreateModel(
            name='Thought',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('native', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.native')),
            ],
        ),
    ]
