##########################
Frequently Asked Questions
##########################

Answers to some common questions. For more help visit #pyramid channel on
freenode.

Find Pyramid Related Packages
=============================

Pyramid does not stand alone. There are many packages that integrate well and
and provide a lot of functionality you might want. Be that SQL, NoSQL,
Facebook/Twitter, or mobile technologies, a lot of functionality is already
available. Check it out here:

* Pyramid has plenty of add-ons, including mailers, RPC, debugging tools. Check
  them out `right here <http://docs.pylonsproject.org/en/latest/docs/pyramid.html#pyramid-add-on-documentation>`_.
* Check out `Officially Supported Pyramid Libraries
  <http://docs.pylonsproject.org/en/latest/docs/libraries.html>`_.
* PyPI is full of `Pyramid related packages <http://pypi.python.org/pypi?%3Aaction=search&term=pyramid>`_.
* `OpenComparison Project <http://pyramid.opencomparison.org/>`_ has side by
  side comparisons of many packages.

Pylons to Pyramid Migration
===========================

Wondering how to do Pylons to Pyramid migration?

* `Akhet <http://sluggo.scrapping.cc/python/Akhet/>`_ will help any Pylons user
  convert their Pylons app to Pyramid. It utilizes `pyramid_handlers
  <http://docs.pylonsproject.org/projects/pyramid_handlers/en/latest/>`_ for routing.


Django Users
============

Are you coming from Django to Pyramid and not sure where to start? Get started
with the set of wonderful packages below.

* Default `alchemy <http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/project.html#scaffolds-included-with-pyramid>`_ scaffold.
* `Jinja2 Templates <http://jinja.pocoo.org/docs/>`_ using `pyramid_jinja2
  <http://docs.pylonsproject.org/projects/pyramid_jinja2/en/latest/>`_.
* Beaker session using `pyramid_beaker
  <http://docs.pylonsproject.org/projects/pyramid_beaker/en/latest/>`_.
* `FormAlchemy <http://docs.formalchemy.org/pyramid_formalchemy/>`_ for the Admin interface.
* For authentication read the `tutorial by Michael Merickel <http://michael.merickel.org/projects/pyramid_auth_demo>`_.
* For forms look at `Deform <http://docs.pylonsproject.org/projects/deform/en/latest/>`_.
  Check out the `Deform demos <http://deformdemo.repoze.org/>`_.

Repoze.BFG to Pyramid Migration
===============================

Pyramid was named repoze.bfg in its past life, and the `migration tutorial
<http://docs.pylonsproject.org/projects/pyramid/en/latest/tutorials/bfg/index.html>`_
is built in.

Authentication and Authorization
================================

* Follow this excellent `tutorial by Michael Merickel
  <http://michael.merickel.org/projects/pyramid_auth_demo>`_.

Event Driven Pyramid
====================

* `Pyramid and Gevent Tutorial <http://michael.merickel.org/2011/6/21/tictactoe-and-long-polling-with-pyramid/>`_ by Michael Merickel.
* `Pyramid, Socket.IO and Gevent <http://blog.abourget.net/2011/3/17/new-and-hot-part-4-pyramid-socket-io-gevent/>`_ by Alexandre Bourget.

Caching with Pyramid
====================

Need caching to speed the sites up? Well tested, documented, and widely known
libaries are available and are easy to use with Pyramid.

* Beaker using `pyramid_beaker
  <http://docs.pylonsproject.org/projects/pyramid_beaker/en/latest/>`_ is easy
  to install and use.
* `Retools <https://pypi.python.org/pypi/retools>`_, is a Beaker on steroids for Redis.

MongoDB
=======

Like MongoDB? Want to get it going on Pyramid?

* Try `pyramid_mongodb <http://pypi.python.org/pypi/pyramid_mongodb>`_
  scaffold.
* `Traversal and MongoDB
  <http://kusut.web.id/2011/03/27/pyramid-traversal-and-mongodb/>`_

Form Validation and Formatting Helpers
======================================

* Use `FormAlchemy <http://docs.formalchemy.org/pyramid_formalchemy/>`_ for
  the Admin interface.
* For form handling look at `Deform
  <http://docs.pylonsproject.org/projects/deform/en/latest/>`_. Check out the
  `Deform demos <http://deformdemo.repoze.org/>`_.

Pyramid and Mobile
==================

Pyramid and jQuery Mobile play very nicely together.

* Check out `pyramid_jqm <http://docs.pylonsproject.org/projects/pyramid_jqm/en/latest/>`_.

fav.ico and Robot.txt serving
=============================

* `Pyramid Assets <http://pypi.python.org/pypi/pyramid_assetviews>`_ package
  will help you do it quickly.
* `Dealing with Static Files <http://docs.pylonsproject.org/projects/pyramid_cookbook/en/latest/static_assets/index.html>`_
  if you want to understand how to do it.

Jinja2 Templates with Pyramid
=============================

Like Jinja2? It is super easy to get it working with Pyramid.

* Using `pyramid_jinja2 <http://docs.pylonsproject.org/projects/pyramid_jinja2/en/latest/>`_ is easy.

Deployment and WSGI Servers
===========================

Pyramid is compatible with all of the WSGI compliant servers. For development
purposes paste.httpserver can be run using ``paster serve development.ini``.

* Waitress
* paste.httpserver
* mod_wsgi / apache
* gunicorn
* CherryPy
* uWSGI
