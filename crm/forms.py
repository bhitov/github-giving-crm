from django import forms
from models import Child
from django.utils.translation import ugettext_lazy as _


class ChildForm(forms.ModelForm):

    update_message = forms.CharField(_('update message'), widget=forms.Textarea)

    def save(self, *args, **kwargs):
        instance = super(ChildForm, self).save(commit=False, *args, **kwargs)
        print self.cleaned_data
        instance.update(message=self.cleaned_data['update_message'])
        return instance

    class Meta:
        model = Child
