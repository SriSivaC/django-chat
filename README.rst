===========
django-chat
===========

.. image:: https://codeclimate.com/github/tomi77/django-chat/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/django-chat
   :alt: Code Climate

A simple Django chat application

Installation
============

.. sourcecode:: sh

   pip install django-chat

Quick start
===========

Add ``chat`` to `INSTALLED_APPS`. ``django.contrib.auth`` and ``django.contrib.contenttypes`` are also required.

.. sourcecode:: python

   INSTALLED_APPS = [
       ...
       'django.contrib.contenttypes',
       'django.contrib.auth',
       'chat',
   ]

Create database

.. sourcecode:: sh

   ./manage.py migrate
