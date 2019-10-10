import json

from django.contrib import admin
from django.conf.urls import url
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseBadRequest


class SearchAutoCompleteAdmin(admin.ModelAdmin):
    """
    Basic admin class that allows to enable search autocomplete for certain model.

    Usage:

    .. code-block:: python

        class MyModelAdmin(SearchAutoCompleteAdmin)
            search_fields = ['search_field', ]

        admin.site.register(MyModel, MyModelAdmin)
    """
    change_list_template = 'search_admin_autocomplete/change_list.html'
    search_prefix = '__contains'
    
    def __init__(self, *args, **kwargs):
        super(SearchAutoCompleteAdmin, self).__init__(*args, **kwargs)
        try:
            field_id = [f for f in self.model._meta.get_fields() if type(f) is AutoField]
            self.field_id = field_id[0].name
        except Exception:
            self.field_id = 'id'

    def get_urls(self):
        urls = super(SearchAutoCompleteAdmin, self).get_urls()
        api_urls = [
            url(r'^search/(?P<search_term>\w{0,50})$', self.search_api)
        ]
        return api_urls + urls

    def search_api(self, request, search_term):
        """
        API view that perform search by search term for current model.

        :param request: request
        :param search_term: word to search.
        :type search_term: str
        :return: JSON response with search results.
        """
        if not self.search_fields:
            return HttpResponseBadRequest(reason='Mo search_fields defined in {}'.format(self.__name__))
        elif not search_term:
            return HttpResponseBadRequest(reason='Mo search term provided')
        else:
            keyword = self.search_fields[0]
            options = {
                keyword + self.search_prefix: search_term,
            }
            data = []

            for instance in self.model.objects.filter(**options):
                data.append(
                    {
                        'keyword': getattr(instance, keyword),
                        'url': self.get_change_form_url(
                            self.model, instance, self.model._meta.app_label, self.field_id)
                    }
                )

            data = json.dumps(data)

            return HttpResponse(content=data, content_type='application/json')

    @staticmethod
    def get_change_form_url(model, instance, app_label, field_id):
        """
        Returns url admin change view for model instance.

        :param model: django model.
        :param instance: model instance.
        :param app_label: current django app label.
        :return: url to change form.
        """
        return reverse(
            "admin:%s_%s_change" % (app_label, str(model.__name__).lower()), args=(getattr(instance, field_id),)
        )
