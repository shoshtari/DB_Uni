# Generated by Django 4.2.2 on 2023-06-27 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_skills'),
        ('jobs', '0002_job_address_job_benefit_job_is_remote_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
            ],
            options={
                'verbose_name': 'Score',
                'verbose_name_plural': 'Scores',
            },
        ),
        migrations.CreateModel(
            name='JobOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_accepted', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.employee')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
            ],
            options={
                'verbose_name': 'Job Offer',
                'verbose_name_plural': 'Job Offers',
            },
        ),
        migrations.AddConstraint(
            model_name='score',
            constraint=models.UniqueConstraint(fields=('employee', 'job'), name='unique_score'),
        ),
        migrations.AddConstraint(
            model_name='joboffer',
            constraint=models.UniqueConstraint(fields=('job', 'employee'), name='unique_job_offer'),
        ),
        migrations.AddConstraint(
            model_name='joboffer',
            constraint=models.CheckConstraint(check=models.Q(('is_accepted', True), ('is_rejected', True), _negated=True), name='check_accepted_rejected'),
        ),
    ]