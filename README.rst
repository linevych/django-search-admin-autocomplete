Django-search-admin-autocomplete
--------------------------------

Simple django app that add autocomplete to search inside admin panel.

.. image:: doc/demo.gif

Installation
============

.. code-block:: python
    pip install django-search-admin-autocomplete

.. code-block:: python
    INSTALLED_APPS = [
    ...
    'search_admin_autocomplete',
    ...
]

Usage
=====
.. code-block:: python

    from search_admin_autocomplete.admin import SearchAutoCompleteAdmin

    class MyModelAdmin(SearchAutoCompleteAdmin)
        search_fields = ['search_field', ]

    admin.site.register(MyModel, MyModelAdmin)

