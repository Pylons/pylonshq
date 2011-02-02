About Pyramid
=============

Pyramid is a very general open source Python web framework. As a framework,
its primary job is to make it easier for a developer to create an arbitrary
web application. The type of application being created isn’t really
important; it could be a spreadsheet, a corporate intranet, or an
“oh-so-Web-2.0” social networking platform. Pyramid is general enough that it
can be used in a wide variety of circumstances.

.. code-block:: python

   from pyramid.config import Configurator
   from pyramid.response import Response
   from paste.httpserver import serve

   def hello_world(request):
       return Response('Hello world!')

   def goodbye_world(request):
       return Response('Goodbye world!')

   if __name__ == '__main__':
       config = Configurator()
       config.add_view(hello_world)
       config.add_view(goodbye_world, name='goodbye')
       app = config.make_wsgi_app()
       serve(app, host='0.0.0.0')


Pyramid is developed using the following tenets.

Simplicity
----------

Pyramid takes a *"pay only for what you eat"* approach.  This means
that you can get results even if you have only a partial understanding of
Pyramid.  It doesn’t force you to use any particular technology to
produce an application, and we try to keep the core set of concepts that
you need to understand to a minimum.

Minimalism
----------

Pyramid concentrates on providing fast, high-quality solutions to
the fundamental problems of creating a web application: the mapping of URLs
to code, templating, security and serving static assets. We consider these
to be the core activities that are common to nearly all web applications.

Documentation
-------------

Pyramid's minimalism means that it is relatively easy for us to maintain
extensive and up-to-date documentation. It is our goal that no aspect of
Pyramid remains undocumented.

Speed
-----

Pyramid is designed to provide noticeably fast execution for common
tasks such as templating and simple response generation. Although the
“hardware is cheap” mantra may appear to offer a ready solution to speed
problems, the limits of this approach become painfully evident when one
finds him or herself responsible for managing a great many machines.

Reliability
-----------

Pyramid is developed conservatively and tested exhaustively. Where
Pyramid source code is concerned, our motto is: "If it ain’t tested, it’s
broke". Every release of Pyramid has 100% statement coverage via unit
tests.

Openness
--------

As with Python, the Pyramid software is distributed under a `permissive
open source license </about/license>`_.

History
-------

The code which exists today in Pyramid is not new.  Between June, 2008 and
November of 2010, it was known as ``repoze.bfg`` (see the `BFG website
<http://bfg.repoze.org>`_ for historical purposes).

When Pyramid was created in early December of 2010, a mass rename of code
from ``repoze.bfg`` was performed and features were added to (and removed
from) the resulting codebase to make it more useful for Pylons Framework 1.X
users.

