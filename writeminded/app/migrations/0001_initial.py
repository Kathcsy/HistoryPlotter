# Generated by Django 4.1.2 on 2022-12-14 05:12

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('period', models.CharField(max_length=100, null=True)),
                ('description', models.TextField()),
                ('actual_material', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_name', models.CharField(max_length=100)),
                ('quiz_desc', models.TextField(default=None)),
                ('quiz_date', models.DateField(blank=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email_address', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='uploadfilemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True, unique=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('file', models.FileField(null=True, upload_to='')),
                ('cover', models.ImageField(null=True, upload_to='')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
            options={
                'db_table': 'uploadfile',
            },
        ),
        migrations.CreateModel(
            name='Relations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ideafile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.uploadfilemodel')),
                ('materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.materials')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='QuizRepo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.AddField(
            model_name='quiz',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_num', models.IntegerField()),
                ('question', models.CharField(max_length=500)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quiz')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
        migrations.AddField(
            model_name='materials',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
        migrations.AddField(
            model_name='materials',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project'),
        ),
        migrations.CreateModel(
            name='groupmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ideafile', models.CharField(max_length=200, null=True, unique=True)),
                ('name', models.CharField(max_length=20, null=True, unique=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
            options={
                'db_table': 'groupfiles',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100)),
                ('isAnswer', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question')),
            ],
        ),
    ]
