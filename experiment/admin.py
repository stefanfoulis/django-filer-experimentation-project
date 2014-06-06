#-*- coding: utf-8 -*-
import copy
from django.contrib import admin
from app_data.forms import multiform_factory
from app_data.admin import AppDataModelAdmin
from .models import MyModel, Tag


MyModelMultiForm = multiform_factory(MyModel)


class MyModelAdmin(AppDataModelAdmin):
    multiform = MyModelMultiForm

    @property
    def declared_fieldsets(self):
        df = [
            (None, {'fields': ['title', 'description', 'is_awesome']}),
        ]
        mf = self.multiform()
        for form in mf.app_forms.values():
            if hasattr(form, 'admin_fieldsets'):
                for admin_fieldset in form.admin_fieldsets:
                    df.append(copy.deepcopy(admin_fieldset))
        return df


admin.site.register(MyModel, MyModelAdmin)
admin.site.register(Tag)


MyModelMultiForm.add_form('tagging', {'fields': ['public_tags']})