# Generated by Django 3.2.4 on 2021-08-12 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('apps', '0003_auto_20210701_1730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baseplugin',
            options={'verbose_name': 'MODEL_NAME_BASE_PLUGIN', 'verbose_name_plural': 'MODEL_NAME_BASE_PLUGIN_PLURAL'},
        ),
        migrations.AlterModelOptions(
            name='basetab',
            options={'ordering': ['order', 'id'], 'verbose_name': 'MODEL_NAME_BASE_TAB', 'verbose_name_plural': 'MODEL_NAME_BASE_TAB_PLURAL'},
        ),
        migrations.AlterModelOptions(
            name='externalembeddedtab',
            options={'verbose_name': 'MODEL_NAME_EXTERNAL_EMBEDDED_TAB', 'verbose_name_plural': 'MODEL_NAME_EXTERNAL_EMBEDDED_TAB_PLURAL'},
        ),
        migrations.AlterModelOptions(
            name='externaliframeplugin',
            options={'verbose_name': 'MODEL_NAME_EXTERNAL_IFRAME_PLUGIN', 'verbose_name_plural': 'MODEL_NAME_EXTERNAL_IFRAME_PLUGIN_PLURAL'},
        ),
        migrations.AlterModelOptions(
            name='externaliframetab',
            options={'verbose_name': 'MODEL_NAME_EXTERNAL_IFRAME_TAB', 'verbose_name_plural': 'MODEL_NAME_EXTERNAL_IFRAME_TAB_PLURAL'},
        ),
        migrations.AlterModelOptions(
            name='htmlplugin',
            options={'verbose_name': 'MODEL_NAME_HTML_PLUGIN', 'verbose_name_plural': 'MODEL_NAME_HTML_PLUGIN_PLURAL'},
        ),
        migrations.AlterModelOptions(
            name='htmltab',
            options={'verbose_name': 'MODEL_NAME_HTML_TAB', 'verbose_name_plural': 'MODEL_NAME_HTML_TAB_PLURAL'},
        ),
        migrations.AlterModelOptions(
            name='rssplugin',
            options={'verbose_name': 'MODEL_NAME_RSS_PLUGIN', 'verbose_name_plural': 'MODEL_NAME_RSS_PLUGIN_PLURAL'},
        ),
        migrations.AlterField(
            model_name='baseplugin',
            name='container_pk',
            field=models.TextField(verbose_name='LABEL_CONTAINER_PK'),
        ),
        migrations.AlterField(
            model_name='baseplugin',
            name='container_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='LABEL_CONTAINER_TYPE'),
        ),
        migrations.AlterField(
            model_name='baseplugin',
            name='title',
            field=models.CharField(max_length=64, verbose_name='LABEL_TITLE'),
        ),
        migrations.AlterField(
            model_name='baseplugin',
            name='views',
            field=models.CharField(blank=True, max_length=255, verbose_name='LABEL_VIEWS'),
        ),
        migrations.AlterField(
            model_name='basetab',
            name='container_pk',
            field=models.TextField(verbose_name='LABEL_CONTAINER_PK'),
        ),
        migrations.AlterField(
            model_name='basetab',
            name='container_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype', verbose_name='LABEL_CONTAINER_TYPE'),
        ),
        migrations.AlterField(
            model_name='basetab',
            name='label',
            field=models.CharField(help_text='TAB_LABEL_HELPTEXT', max_length=12, verbose_name='LABEL_LABEL'),
        ),
        migrations.AlterField(
            model_name='basetab',
            name='opening_method',
            field=models.CharField(blank=True, max_length=32, verbose_name='LABEL_OPENING_METHOD'),
        ),
        migrations.AlterField(
            model_name='basetab',
            name='order',
            field=models.IntegerField(default=100, verbose_name='LABEL_ORDER'),
        ),
        migrations.AlterField(
            model_name='basetab',
            name='title',
            field=models.CharField(help_text='TAB_TITLE_HELPTEXT', max_length=64, verbose_name='LABEL_TITLE'),
        ),
        migrations.AlterField(
            model_name='externalembeddedtab',
            name='content_url',
            field=models.URLField(max_length=128, verbose_name='LABEL_CONTENT_URL'),
        ),
        migrations.AlterField(
            model_name='externalembeddedtab',
            name='element_id',
            field=models.CharField(blank=True, max_length=32, verbose_name='LABEL_ELEMENT_ID'),
        ),
        migrations.AlterField(
            model_name='externaliframeplugin',
            name='height',
            field=models.IntegerField(verbose_name='LABEL_HEIGHT'),
        ),
        migrations.AlterField(
            model_name='externaliframeplugin',
            name='service_url',
            field=models.URLField(max_length=255, verbose_name='LABEL_SERVICE_URL'),
        ),
        migrations.AlterField(
            model_name='externaliframeplugin',
            name='width',
            field=models.IntegerField(verbose_name='LABEL_WIDTH'),
        ),
        migrations.AlterField(
            model_name='externaliframetab',
            name='content_url',
            field=models.URLField(max_length=255, verbose_name='LABEL_CONTENT_URL'),
        ),
        migrations.AlterField(
            model_name='externaliframetab',
            name='height',
            field=models.IntegerField(verbose_name='LABEL_HEIGHT'),
        ),
        migrations.AlterField(
            model_name='externaliframetab',
            name='width',
            field=models.IntegerField(verbose_name='LABEL_WIDTH'),
        ),
        migrations.AlterField(
            model_name='htmlplugin',
            name='content',
            field=models.TextField(verbose_name='LABEL_CONTENT'),
        ),
        migrations.AlterField(
            model_name='htmltab',
            name='content',
            field=models.TextField(verbose_name='LABEL_CONTENT'),
        ),
        migrations.AlterField(
            model_name='rssplugin',
            name='feed_url',
            field=models.URLField(max_length=256, verbose_name='LABEL_FEED_URL'),
        ),
    ]