Django-search-admin-autocomplete
--------------------------------

Simple django app that add autocomplete to search inside admin panel.

.. image:: https://raw.githubusercontent.com/linevych/django-search-admin-autocomplete/master/doc/demo.gif

Requirements
============

- Python: 3.5+
- Django: >=1.11

Installation
============

.. code-block:: bash

    pip install django-search-admin-autocomplete
    # OR
    pip install git+https://github.com/linevych/django-search-admin-autocomplete.git

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

Customization
=====
If admin/change_list.html is customized

admin.py

.. code-block:: python

    from search_admin_autocomplete.admin import SearchAutoCompleteAdmin

    class MyModelAdmin(SearchAutoCompleteAdmin)
    
        change_list_template = 'admin/custom-list.html'
    
        search_fields = ['search_field', ]

    admin.site.register(MyModel, MyModelAdmin)

admin/custom-list.html

.. code-block:: html

    {% extends 'search_admin_autocomplete/change_list.html' %}

    {% block object-tools %}
    Your custom html...
    {{ block.super }}
    {% endblock %}

MyPy
====

This project supports MyPy but to run type checks you need Python 3.6+.

.. code-block:: python

    pip install -r requirements_dev.txt
    PYTHONPATH="$PYTHONPATH:$PWD/example" mypy search_admin_autocomplete
