from functools import reduce
from operator import or_
from typing import List

from django.conf.urls import url
from django.contrib import admin
from django.db.models import Q, Model
from django.http import HttpRequest
from django.urls.resolvers import URLPattern

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse  # type: ignore
from django.http.response import HttpResponse, JsonResponse, HttpResponseBadRequest


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
    search_fields = []  # type: List[str]
    search_prefix = '__contains'
    max_results = 10

    def get_urls(self) -> List[URLPattern]:
        urls = super(SearchAutoCompleteAdmin, self).get_urls()
        api_urls = [url(r'^search/(?P<search_term>\w{0,50})$', self.search_api)]
        return api_urls + urls

    def search_api(self, request: HttpRequest, search_term: str) -> HttpResponse:
        """
        API view that perform search by search term for current model.
        """
        if len(self.search_fields) == 0:
            return HttpResponseBadRequest(reason='Mo search_fields defined in {}'.format(self.__class__.__name__))

        query = [Q(**{'{}{}'.format(field, self.search_prefix): search_term}) for field in self.search_fields]
        # https://github.com/python/mypy/issues/4150
        query = reduce(or_, query)  # type: ignore
        return JsonResponse(data=[{'keyword': self.get_instance_name(item), 'url': self.get_instance_url(item)}
                                  for item in self.model.objects.filter(query)[0:self.max_results]], safe=False)

    def get_instance_name(self, instance: Model) -> str:
        """
        Format instance name based on value of search fields.
        """
        values = []

        for field in self.search_fields:
            value = getattr(instance, field)
            if not value:
                continue
            values.append(str(value))

        if not values:
            return ""

        return ", ".join(values)

    def get_instance_url(self, instance: Model) -> str:
        """
        Returns url admin change view for model instance.
        """
        url_name = "admin:{}_{}_change".format(self.model._meta.app_label, str(self.model.__name__).lower())
        return reverse(url_name, args=(instance.pk,))
