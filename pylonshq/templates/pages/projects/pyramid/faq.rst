##########################
Frequently Asked Questions
##########################

Answers to some common questions. For more help visit #pyramid channel on
freenode

Find Pyramid Related Packages
=============================

Pyramid does not stand alone. There are many packages that integrate well and
and provide a lot of functionality you might want. Be that SQL, NoSQL,
Facebook/Twitter, Mobile technologies a lot of functionality is already
available. Check it out here:

* Pyramid has plenty of add-ons, be that mailers, RPC, debugging tools. Check
  them out `right here <http://docs.pylonsproject.org/docs/pyramid.html#pyramid-add-on-documentation>`_
* Checkout `Officially Supported Pyramid Libraries
  <http://docs.pylonsproject.org/docs/libraries.html>`_
* PyPI is full of `Pyramid related packages <http://pypi.python.org/pypi?%3Aaction=search&term=pyramid>`_
* `OpenComparisson Project <http://pyramid.opencomparison.org/>`_ has side by
  side comparissons of many packages.

Pylons to Pyramid Migration
===========================

Wondering how to do Pylons to Pyramid migration?

* `Akhet <http://sluggo.scrapping.cc/python/Akhet/>`_ will help any Pylons user
  convert their Pylons app to Pyramid. It utilizes `pyramid_handlers
  <http://docs.pylonsproject.org/projects/pyramid_handlers/dev/>`_ for routing.


Django Users
============

Are you coming from Django to Pyramid and not sure where to start. Get started
with the set of wonderful packages below.

* Default `pyramid_routesalchemy <http://docs.pylonsproject.org/projects/pyramid/current/narr/project.html#scaffolds-included-with-pyramid>`_ scaffold
* `Jinja2 Templates <http://jinja.pocoo.org/docs/>`_ using `pyramid_jinja2
  <http://docs.pylonsproject.org/projects/pyramid_jinja2/dev/>`_
* Beaker session using `pyramid_beaker
  <http://docs.pylonsproject.org/projects/pyramid_beaker/dev/>`_
* `FormAlchemy <http://docs.formalchemy.org/pyramid_formalchemy/>`_ for the Admin interface.
* For authentication read the tutorial by <http://michael.merickel.org/projects/pyramid_auth_demo>`_
* For forms look at `Deform
  <http://docs.pylonsproject.org/projects/deform/dev/>`_. Checkout the `Deform
  demos <http://deformdemo.repoze.org/>`_

Repoze.BFG to Pyramid Migration
===============================

Pyramid was repoze.bfg in its past life and migration is built in.

The `migration tutorial <http://docs.pylonsproject.org/projects/pyramid/current/tutorials/bfg/index.html>`_ is built in.


Authentication and Authorization
================================

* Follow this excellent `tutorial by Michael Merickel
  <http://michael.merickel.org/projects/pyramid_auth_demo>`_

Event Driven Pyramid
====================

* `Pyramid and Gevent Tutorial <http://michael.merickel.org/2011/6/21/tictactoe-and-long-polling-with-pyramid/>`_ by Michael Merickel
* `Pyramid, Socket.IO and Gevent <http://blog.abourget.net/2011/3/17/new-and-hot-part-4-pyramid-socket-io-gevent/>`_ by Alexandre Bourget


Caching with Pyramid
====================

Need caching to speed the sites up? Well tested, documented and widely known
libaries are available and are easy to use with Pyramid.

* Beaker using `pyramid_beaker
  <http://docs.pylonsproject.org/projects/pyramid_beaker/dev/>`_ is easy to
  install and use.
* `Retools <pypi.python.org/pypi/retools>`_, is a Beaker on steroids for Redis.


MongoDB
=======

Like MongoDB? Want get it going on Pyramid?

* Try `pyramid_mongodb <http://pypi.python.org/pypi/pyramid_mongodb>`_
  scaffold.
* Traversal and MongoDB
  <http://kusut.web.id/2011/03/27/pyramid-traversal-and-mongodb/>`_


Form Validation and Formatting Helpers
======================================

* Use `FormAlchemy <http://docs.formalchemy.org/pyramid_formalchemy/>`_ for the Admin interface.
* For authentication read the tutorial by <http://michael.merickel.org/projects/pyramid_auth_demo>`_
* For form handling look at `Deform
  <http://docs.pylonsproject.org/projects/deform/dev/>`_. Checkout the `Deform
  demos <http://deformdemo.repoze.org/>`_


Pyramid and Mobile
==================

Pyramid and jQuery Mobile play very nicely together.

* Checkout `pyramid_jqm <http://docs.pylonsproject.org/projects/pyramid_jqm/dev/>`_

fav.ico and Robot.txt serving
=============================

* `Pyramid Assets <http://pypi.python.org/pypi/pyramid_assetviews>`_ package will help you do it quickly
* `Dealing with Static Files <http://docs.pylonsproject.org/projects/pyramid_cookbook/dev/files.html>`_ if you want to understand how to do it.

Jinja2 Templates with Pyramid
=============================

Like Jinja2? It is super easy to get it working with Pyramid.

* Using `pyramid_jinja2 <http://docs.pylonsproject.org/projects/pyramid_jinja2/dev/>`_ is easy.

Deployment and WSGI Servers
===========================

Pyramid is compatible with all of the WSGI compliant servers. For development
purposes paste.httpserver can be run using **paster serve development.ini**

* paste.httpserver
* mod_wsgi / apache
* gunicorn
* CherryPy
* uWSGI

