from django.db import models
from django.utils.translation import ugettext_lazy as _




class Child(models.Model):
    name = models.CharField(_('name'), max_length=255)
    birthday = models.DateField(_('birthday'))
    family_conditions = models.TextField(_('family conditions'))

    def update(self, message='', picture='', *args, **kwargs):
        new_child = True
        if self.pk:
            new_child = False
            old_self = Child.objects.get(pk=self.pk)
        else:
            old_self = Child()
        changes = self.create_changes(old_self)
        picture = kwargs.pop('picture', '')

        return_value = self.save(*args, **kwargs)

        # If we get here, save succeeded
        update = ChildUpdate.objects.create(child=self, message=message)
        for change in changes:
            change.child_update = update
            change.save()

        return return_value



    def create_changes(self, old_self):
        """
        Creates ChildFieldUpdate objects for each field in the child to be
        saved that differs from the database record of that child.

        When creating a new child, ChildFieldUpdate objects are created for
        every field
        """
        excluded_fields = ['id']
        changes = []
        field_names = [field.name for field in self._meta.fields]
        for field_name in field_names:
            if field_name not in excluded_fields:
                new_value = getattr(self, field_name)
                if new_value != getattr(old_self, field_name):
                    change = ChildFieldUpdate(field_name=field_name,
                                              field_value=new_value)
                    changes.append(change)
        return changes


    def __unicode__(self):
        return self.name



    class Meta:
        verbose_name = _('child')
        verbose_name_plural = _('children')



class ChildUpdate(models.Model):
    child = models.ForeignKey(Child, related_name='updates')
    update_time = models.DateTimeField(_('update time'), auto_now_add=True,
            db_index=True)
    message = models.TextField(blank=True)

    class Meta:
        verbose_name = _('child update')
        verbose_name_plural = _('child updates')

    def __unicode__(self):
        return "%s %s" % (self.child.name, self.message)

class ChildFieldUpdate(models.Model):
    child_update = models.ForeignKey(ChildUpdate, verbose_name=_('child'),
            related_name='changes', db_index=True)
    field_name = models.CharField(_('field name'), max_length=100)
    field_value = models.TextField(_('field value'))





