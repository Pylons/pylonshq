##################################
Pyramid Frequently Asked Questions
##################################

What is the difference between Pyramid and Pylons, the web framework?
=====================================================================

Pyramid is a web framework that was first released in January 2011. It
doesn't "share any DNA" with Pylons 1.0. The Pylons 1.x web framework will be
maintained indefinitely by The Pylons Project.  There may be a Pylons 1.1
release aimed at easing a transition to Pyramid eventually.  However, as of
the release of Pyramid 1.0 on January 31, 2011, the Pylons web framework has
effectively been shifted into "legacy" status.

Existing Pylons 1.0 code will be able to run "inside" Pyramid via the use
of a fallback handler that sends requests to an existing Pylons application.
When run within the fallback handler, Pylons 1.0 applications may be ported
piecemeal to Pyramid. As each bit of functionality is translated into Pyramid
code, the fallback application will continue to handle yet-to-be ported
functionality.

.. _should_i_port:

Why is Pyramid any different than the hundred other Python web frameworks?
==========================================================================

See `What Makes Pyramid Unique <http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/introduction.html#what-makes-pyramid-unique>`_.

Does Pyramid run on Python 3?
=============================

Pyramid 1.3a1+ runs on Python 3.2 and better.  Earlier versions run on Python
2 only.

Where are the Pyramid add-ons?
==============================

Pyramid supports extensibility through add-ons, including mailers, RPC, and debugging tools.

* `Officially supported add-ons for Pyramid <http://docs.pylonsproject.org/en/latest/docs/pyramid.html#supported-add-ons>`_.

Where are the Pyramid related packages?
=======================================

Pyramid does not stand alone. There are many packages that integrate well and
and provide a lot of functionality you might want. SQL, NoSQL,
Facebook/Twitter, mobile technologies, and a lot more functionality is already
available.

* `Officially Supported Pyramid Libraries <http://docs.pylonsproject.org/en/latest/docs/libraries.html>`_
* `Pyramid related packages on PyPI <http://pypi.python.org/pypi?%3Aaction=search&term=pyramid>`_.
  Might not be "official".
* `OpenComparison Project <http://pyramid.opencomparison.org/>`_ has side by
  side comparisons of many packages.

Where are the best places to learn Pyramid when coming from Django?
===================================================================

* Use a the `alchemy scaffold <http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/project.html#scaffolds-included-with-pyramid>`_
  to quickly start a project with an SQL database for persistent storage.
* You can use `Jinja2 templates <http://jinja.pocoo.org/docs/>`_ with the
  add-on `pyramid_jinja2 <http://docs.pylonsproject.org/projects/pyramid_jinja2/en/latest/>`_.
* Use sessions with the Beaker add-on `pyramid_beaker <http://docs.pylonsproject.org/projects/pyramid_beaker/en/latest/>`_.
* `FormAlchemy <http://docs.formalchemy.org/pyramid_formalchemy/>`_ can be
  used to recreate the Django Admin interface.
* For authentication read the `tutorial by Michael Merickel <http://michael.merickel.org/projects/pyramid_auth_demo>`_.
* For forms look at `Deform <http://docs.pylonsproject.org/projects/deform/en/latest/>`_.
  Check out the `Deform demos <http://deformdemo.repoze.org/>`_.

How do I implement authentication and authorization?
====================================================

Follow this excellent `tutorial by Michael Merickel <http://michael.merickel.org/projects/pyramid_auth_demo>`_.

How do I implement event driven applications in Pyramid?
========================================================

* `Pyramid and Gevent Tutorial <http://michael.merickel.org/2011/6/21/tictactoe-and-long-polling-with-pyramid/>`_
  by Michael Merickel.
* `Pyramid, Socket.IO and Gevent <http://blog.abourget.net/2011/3/17/new-and-hot-part-4-pyramid-socket-io-gevent/>`_
  by Alexandre Bourget.

How do I implement caching in Pyramid?
======================================

* `Retools <https://pypi.python.org/pypi/retools>`_ is Beaker on steroids for
  Redis.
* Beaker uses `pyramid_beaker <http://docs.pylonsproject.org/projects/pyramid_beaker/en/latest/>`_.

How do I use MongoDB with Pyramid?
==================================

* Try the `pyramid_mongodb <http://pypi.python.org/pypi/pyramid_mongodb>`_ scaffold.
* Read the article `Traversal and MongoDB
  <http://kusut.web.id/2011/03/27/pyramid-traversal-and-mongodb/>`_.

How do I validate form input and use formatting helpers?
========================================================

* `pyramid_formalchemy <http://docs.formalchemy.org/pyramid_formalchemy/>`_
  provides a CRUD interface for pyramid based on FormAlchemy.
* For form generation and handling, try `Deform
  <http://docs.pylonsproject.org/projects/deform/en/latest/>`_.
  Check out the `Deform demos <http://deformdemo.repoze.org/>`_.

How can I create mobile applications in Pyramid?
================================================

Pyramid and jQuery Mobile play very nicely together. Check out
`pyramid_jqm <http://docs.pylonsproject.org/projects/pyramid_jqm/en/latest/>`_.

How do I serve favicon.ico, Robot.txt, and other static assets?
===============================================================

* `pyramid_assetviews <http://pypi.python.org/pypi/pyramid_assetviews>`_ is a
  small module that allows you to add root-relative views to your project.
* The Pyramid Cookbook contains a recipe for working with `Static Assets <http://docs.pylonsproject.org/projects/pyramid_cookbook/en/latest/static_assets/index.html>`_.

How do I use Jinja2 templates with Pyramid?
===========================================

You can use `Jinja2 templates <http://jinja.pocoo.org/docs/>`_ with the add-on
`pyramid_jinja2 <http://docs.pylonsproject.org/projects/pyramid_jinja2/en/latest/>`_.

How do I deploy Pyramid? Which WSGI servers does Pyramid support?
=================================================================

Pyramid is compatible with all of the WSGI compliant servers. For development
purposes ``paste.httpserver`` can be run using ``paster serve development.ini``.

* Waitress
* paste.httpserver
* mod_wsgi / apache
* gunicorn
* CherryPy
* uWSGI

Should I port my Pylons 1.0 project to Pyramid?
===============================================

Pyramid 1.0 was released on Jan 31, 2011.

Read the draft release of the `Pylons-to-Pyramid Migration Guide <https://bytebucket.org/sluggo/pyramid-docs/wiki/html/migration.html>`_
and the guide `Pyramid for Pylons Users <http://docs.pylonsproject.org/projects/pyramid_cookbook/en/latest/pylons/index.html>`_.

We've heard reports from several Pylons users that they have ported smaller
apps without too much difficulty.  `Akhet <http://sluggo.scrapping.cc/python/Akhet/>`_
will help any Pylons user convert their Pylons app to Pyramid. It utilizes
`pyramid_handlers <http://docs.pylonsproject.org/projects/pyramid_handlers/en/latest/>`_
for routing.  For larger Pylons apps, you may want to wait for the migration
guide document to reach non-draft status before attempting a port.

However, there are a few things you can do now to ease a later migration to
Pyramid:

1) Avoid the use of Pylons global objects except directly in action methods.
   There is no other well-known way to access them, unless
   self._py_object.request has been implemented.

   Pylons global objects refer to 'request', 'session', 'cache', 'response',
   'tmpl_context', 'config', 'url' objects that are imported from ``pylons``.

   This also affects your ability to use your domain models outside of a
   Pylons app (a command line script). Domain models shouldn't depend
   on Pylons globals to work, nor should you pass Pylons globals into class
   methods of your domain models. Pass variables that contain just the
   data the model needs.

2) Ensure all of your routes are explicit and named. All routes in Pyramid
   must be named (uniquely), and there is no minimization available.

If your Pylons app is already set up like this, then your domain models will
most likely require no changes at all. Templates might need slight
alterations and controllers will need some changes.

What is the difference between Pyramid and repoze.bfg?
======================================================

Pyramid *is* repoze.bfg, with:

- a new name and a new set of import locations, and

- a few added features to meet the expectations of Pylons 1.0 users.

repoze.bfg 1.3 (made November 1, 2010) will be its last major release. Minor
updates will be made for critical bug fixes (and so there may be a 1.3.1,
1.3.2, etc), but new feature development will take place in Pyramid.

How do I get more help and support with Pyramid?
================================================
See `Get Support </community/get-support>`_.

