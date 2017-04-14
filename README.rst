===========
django-chat
===========

.. image:: https://codeclimate.com/github/tomi77/django-chat/badges/gpa.svg
   :target: https://codeclimate.com/github/tomi77/django-chat
   :alt: Code Climate

A simple chat

Installation
============

.. sourcecode:: sh

   pip install django-chat

Quick start
===========

Enable ``chat`` and ``django.contrib.auth``

.. sourcecode:: python

   INSTALLED_APPS = [
       ...
       'django.contrib.auth',
       'chat',
   ]
