from django.db import models
from django.utils.translation import ugettext_lazy as _

class Child(models.Model):
    name = models.CharField(_('name'), max_length=255)
    birthday = models.DateField(_('birthday'))
    picture = models.ImageField(_('picture'))
    family_conditions = models.TextField(_('family conditions'))

    class Meta:
        verbose_name = _('child')
        verbose_name_plural = _('children')

class ChildUpdate(models.Model):
    child = models.ForeignKey(Child, related_name='updates')
    update_time = models.DateTimeField(_('update time'), auto_now_add=True,
            db_index=True)
    change_message = models.TextField(blank=True)
    picture = models.ImageField(blank=True)

    class Meta:
        verbose_name = _('child update')
        verbose_name_plural = _('child updates')

class ChildFieldUpdate(models.Model):
    child = models.ForeignKey(Child, verbose_name=_('child'),
            related_name='changes', db_index=True)
    field = models.CharField(_('field name'), max_length=100)




