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

#    def save(self, *args, **kwargs):
#        new_child = True
#        if self.pk:
#            new_child = False
#            old_self = Child.objects.get(pk=self.pk)
#        else:
#            old_self = Child()
#        changes = self.create_changes(old_self)
#        message = kwargs.pop('message', '')
#        picture = kwargs.pop('picture', '')
#
#        super(Child, self).save(*args, **kwargs)
#
#        # If we get here, save succeeded
#        log_entry = ChildUpdate.objects.create()
#
#
#
#    def create_changes(self, old_self):
#        """
#        Creates ChildFieldUpdate objects for each field in the child to be
#        saved that differs from the database record of that child.
#
#        When creating a new child, ChildFieldUpdate objects are created for
#        every field
#        """
#
#        excluded_fields = ['id']
#        changes = []
#        field_names = [field.name for field in self._meta.fields]
#        for field_name in field_names:
#            if field_name not in excluded_fields:
#                new_value = getattr(self, field_name)
#                if new_value != getattr(old_self, field_name):
#                    change = ChildFieldUpdate(field_name=field_name,
#                                              field_value=new_value)
#                    changes.append(change)
#
#
#
#
#
#
#    class Meta:
#        verbose_name = _('child')
#        verbose_name_plural = _('children')
#
#
#
#class ChildUpdate(models.Model):
#    child = models.ForeignKey(Child, related_name='updates')
#    update_time = models.DateTimeField(_('update time'), auto_now_add=True,
#            db_index=True)
#    message = models.TextField(blank=True)
#    picture = models.ImageField(blank=True)
#
#    class Meta:
#        verbose_name = _('child update')
#        verbose_name_plural = _('child updates')
#
#class ChildFieldUpdate(models.Model):
#    child = models.ForeignKey(Child, verbose_name=_('child'),
#            related_name='changes', db_index=True)
#    field_name = models.CharField(_('field name'), max_length=100)
#    field_value = models.TextField(_('field value'))
#
#
#
#
#
