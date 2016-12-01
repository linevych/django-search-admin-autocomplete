Django-search-admin-autocomplete
--------------------------------

Simple django app that add autocomplete to search inside admin panel.

Usage
=====

.. code-block:: python

    from search_admin_autocomplete.admin import SearchAutoCompleteAdmin

    class MyModelAdmin(SearchAutoCompleteAdmin)
        search_fields = ['search_field', ]

    admin.site.register(MyModel, MyModelAdmin)
