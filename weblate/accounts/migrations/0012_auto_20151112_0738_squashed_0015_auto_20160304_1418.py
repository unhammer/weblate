# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import weblate.trans.fields


class Migration(migrations.Migration):

    replaces = [('accounts', '0012_auto_20151112_0738'), ('accounts', '0013_auto_20151222_1006'), ('accounts', '0014_auto_20160302_1025'), ('accounts', '0015_auto_20160304_1418')]

    dependencies = [
        ('trans', '0058_componentlist'),
        ('accounts', '0011_auto_20150916_0952'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(choices=[(b'az', 'Az\u0259rbaycan'), (b'be', '\u0411\u0435\u043b\u0430\u0440\u0443\u0441\u043a\u0430\u044f'), (b'be@latin', 'Bie\u0142aruskaja'), (b'br', 'Brezhoneg'), (b'ca', 'Catal\xe0'), (b'cs', '\u010ce\u0161tina'), (b'da', 'Dansk'), (b'de', 'Deutsch'), (b'en', 'English'), (b'el', '\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac'), (b'es', 'Espa\xf1ol'), (b'fi', 'Suomi'), (b'fr', 'Fran\xe7ais'), (b'fy', 'Frysk'), (b'gl', 'Galego'), (b'he', '\u05e2\u05d1\u05e8\u05d9\u05ea'), (b'hu', 'Magyar'), (b'id', b'Indonesia'), (b'ja', '\u65e5\u672c\u8a9e'), (b'ko', '\ud55c\uad6d\uc5b4'), (b'ksh', 'K\xf6lsch'), (b'nl', 'Nederlands'), (b'pl', 'Polski'), (b'pt', 'Portugu\xeas'), (b'pt-br', 'Portugu\xeas brasileiro'), (b'ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), (b'sk', 'Sloven\u010dina'), (b'sl', 'Sloven\u0161\u010dina'), (b'sr', '\u0421\u0440\u043f\u0441\u043a\u0438'), (b'sv', 'Svenska'), (b'tr', 'T\xfcrk\xe7e'), (b'uk', '\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430'), (b'zh-hans', '\u7b80\u4f53\u5b57'), (b'zh-hant', '\u6b63\u9ad4\u5b57')], max_length=10, verbose_name='Interface Language'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(choices=[(b'az', 'Az\u0259rbaycan'), (b'be', '\u0411\u0435\u043b\u0430\u0440\u0443\u0441\u043a\u0430\u044f'), (b'be@latin', 'Bie\u0142aruskaja'), (b'br', 'Brezhoneg'), (b'ca', 'Catal\xe0'), (b'cs', '\u010ce\u0161tina'), (b'da', 'Dansk'), (b'de', 'Deutsch'), (b'en', 'English'), (b'el', '\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac'), (b'es', 'Espa\xf1ol'), (b'fi', 'Suomi'), (b'fr', 'Fran\xe7ais'), (b'fy', 'Frysk'), (b'gl', 'Galego'), (b'he', '\u05e2\u05d1\u05e8\u05d9\u05ea'), (b'hu', 'Magyar'), (b'id', b'Indonesia'), (b'ja', '\u65e5\u672c\u8a9e'), (b'ko', '\ud55c\uad6d\uc5b4'), (b'ksh', 'K\xf6lsch'), (b'nl', 'Nederlands'), (b'pl', 'Polski'), (b'pt', 'Portugu\xeas'), (b'pt-BR', 'Portugu\xeas brasileiro'), (b'ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), (b'sk', 'Sloven\u010dina'), (b'sl', 'Sloven\u0161\u010dina'), (b'sr', '\u0421\u0440\u043f\u0441\u043a\u0438'), (b'sv', 'Svenska'), (b'tr', 'T\xfcrk\xe7e'), (b'uk', '\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430'), (b'zh-Hans', '\u7b80\u4f53\u5b57'), (b'zh-Hant', '\u6b63\u9ad4\u5b57')], max_length=10, verbose_name='Interface Language'),
        ),
        migrations.AddField(
            model_name='profile',
            name='dashboard_component_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='trans.ComponentList', verbose_name='Default component list'),
        ),
        migrations.AddField(
            model_name='profile',
            name='dashboard_view',
            field=models.IntegerField(choices=[(1, 'Your subscriptions'), (2, 'Your languages'), (3, 'All projects'), (4, 'Component list')], default=1, verbose_name='Default dashboard view'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(choices=[('az', 'Az\u0259rbaycan'), ('be', '\u0411\u0435\u043b\u0430\u0440\u0443\u0441\u043a\u0430\u044f'), ('be@latin', 'Bie\u0142aruskaja'), ('br', 'Brezhoneg'), ('ca', 'Catal\xe0'), ('cs', '\u010ce\u0161tina'), ('da', 'Dansk'), ('de', 'Deutsch'), ('en', 'English'), ('el', '\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac'), ('es', 'Espa\xf1ol'), ('fi', 'Suomi'), ('fr', 'Fran\xe7ais'), ('fy', 'Frysk'), ('gl', 'Galego'), ('he', '\u05e2\u05d1\u05e8\u05d9\u05ea'), ('hu', 'Magyar'), ('id', 'Indonesia'), ('it', 'Italiano'), ('ja', '\u65e5\u672c\u8a9e'), ('ko', '\ud55c\uad6d\uc5b4'), ('ksh', 'K\xf6lsch'), ('nl', 'Nederlands'), ('pl', 'Polski'), ('pt', 'Portugu\xeas'), ('pt-br', 'Portugu\xeas brasileiro'), ('ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), ('sk', 'Sloven\u010dina'), ('sl', 'Sloven\u0161\u010dina'), ('sr', '\u0421\u0440\u043f\u0441\u043a\u0438'), ('sv', 'Svenska'), ('tr', 'T\xfcrk\xe7e'), ('uk', '\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430'), ('zh-hans', '\u7b80\u4f53\u5b57'), ('zh-hant', '\u6b63\u9ad4\u5b57')], max_length=10, verbose_name='Interface Language'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='secondary_languages',
            field=models.ManyToManyField(blank=True, help_text='Choose languages you can understand, strings in those languages will be shown in addition to the source string.', related_name='secondary_profile_set', to='lang.Language', verbose_name='Secondary languages'),
        ),
        migrations.CreateModel(
            name='AutoGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', weblate.trans.fields.RegexField(default='^.*$', help_text='Regular expression which is used to match user email.', max_length=200, verbose_name='Email regular expression')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='Group to assign')),
            ],
            options={
                'ordering': ('group__name',),
                'verbose_name': 'Automatic group assignment',
                'verbose_name_plural': 'Automatic group assignments',
            },
        ),
        migrations.AlterField(
            model_name='profile',
            name='subscriptions',
            field=models.ManyToManyField(blank=True, help_text='You can receive notifications for subscribed projects and they are shown on dashboard by default.', to='trans.Project', verbose_name='Subscribed projects'),
        ),
    ]
