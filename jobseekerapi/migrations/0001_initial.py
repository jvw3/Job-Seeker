# Generated by Django 4.1.3 on 2022-12-06 18:01

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('goal', models.CharField(max_length=200)),
                ('requirements', models.TextField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='BoardJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_interviewed', models.BooleanField()),
                ('interview_rounds', models.IntegerField(blank=True, null=True)),
                ('salary_rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('location_rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('culture_rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('leadership_rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('team_rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('job_score', models.IntegerField(blank=True, null=True)),
                ('category_state', models.CharField(blank=True, max_length=50)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='jobseekerapi.board')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewPrep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_info', models.TextField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Seeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=5000)),
                ('current_role', models.CharField(max_length=100)),
                ('elevator_pitch', models.TextField(blank=True, max_length=1000, null=True)),
                ('is_admin', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PriorityRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('location', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('culture', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('leadership', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('team', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobseekerapi.board')),
            ],
        ),
        migrations.CreateModel(
            name='PrepQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobseekerapi.interviewprep')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobseekerapi.question')),
            ],
        ),
        migrations.AddField(
            model_name='interviewprep',
            name='questions',
            field=models.ManyToManyField(related_name='questions', through='jobseekerapi.PrepQuestion', to='jobseekerapi.question'),
        ),
        migrations.AddField(
            model_name='interviewprep',
            name='seeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobseekerapi.seeker'),
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('is_complete', models.BooleanField()),
                ('interview_feedback', models.TextField(max_length=10000)),
                ('board_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interviews', to='jobseekerapi.boardjob')),
                ('prep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prep', to='jobseekerapi.interviewprep')),
            ],
        ),
        migrations.CreateModel(
            name='CustomPrepInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
                ('content', models.TextField(max_length=10000)),
                ('prep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='custom_preps', to='jobseekerapi.interviewprep')),
            ],
        ),
        migrations.AddField(
            model_name='boardjob',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobseekerapi.company'),
        ),
        migrations.AddField(
            model_name='boardjob',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobseekerapi.job'),
        ),
        migrations.CreateModel(
            name='BoardCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobseekerapi.board')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobseekerapi.category')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='categories',
            field=models.ManyToManyField(related_name='categories', through='jobseekerapi.BoardCategory', to='jobseekerapi.category'),
        ),
        migrations.AddField(
            model_name='board',
            name='seeker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boards', to='jobseekerapi.seeker'),
        ),
    ]
