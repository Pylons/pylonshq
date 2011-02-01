How to Participate
==================

Most interaction with the Pylons Project is done via `The Pylons GitHub
organization <https://github.com/organizations/Pylons>`_, via the
`Pylons-devel mailing list <http://groups.google.com/group/pylons-devel>`_,
or via the ``#pylons`` channel on `FreeNode <http://freenode.net/>`._

Reporting a Bug
---------------

When reporting a bug, be as thorough as possible.  Including additional
detail is encouraged.  Bugs with a Pylons Project package should be reported
to the individual issue tracker on GitHub_.

1) Create a GitHub account
!!!!!!!!!!!!!!!!!!!!!!!!!!

You will need to `create a GitHub account <https://github.com/signup/free>`_
account to report the bug.

2) Determine if your bug is really a bug
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   
You should not file a bug if you are:
   
* **Proposing features and ideas**: you should provide a pull request or send
    a mail to the `mailing list
    <http://groups.google.com/group/pylons-devel>`_.

* **Requesting support**: there are a variety of ways to request support,
  from the `mailing list <http://groups.google.com/group/pylons-devel>`_, 
  `Stackoverflow <http://stackoverflow.com/questions/tagged/pylons>`_, or IRC
  at ``#pylons`` on `FreeNode <http://freenode.net/>`_.

3) Make sure your bug hasn't already been reported
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Before creating an issue, search through the appropriate Issue tracker on
GitHub_. If you find a bug like yours, and it hasn't yet been fixed, check to
see if you have new information that could be reported to help the developers
fix it.

4) Collect information about the bug
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

To provide the developers with enough information to fix a bug, they'll need
to be able to easily repeat the conditions and observe it themselves.  The
the likelihood that a bug will be fixed is directly correlated to the
developer's ability to create the conditions under which the bug may be
observed.

Often a bug report should include a Python traceback (`see a Python traceback
<http://pastebin.com/TyaPKpt9>`_).  We will also need to know what platform
you're running (Windows, OSX, Linux), and which Python interpreter you're
running if its not CPython (e.g. Jython, Google App Engine).

5) Submit the bug
!!!!!!!!!!!!!!!!!

By default GitHub_ will email you to let you know when new comments have been
made on your bug report. In the event you've turned this feature off, you
should check back on occasion to ensure you don't miss any questions a
developer trying to fix the bug might ask.

.. _issue_trackers:

Issue Trackers
--------------

Bugs are reported and tracked via GitHub_'s issue trackers. Each Pylons Project
has its own issue tracker:

* `pyramid issue tracker <https://github.com/Pylons/pyramid/issues>`_
* `pyramid_beaker issue tracker <https://github.com/Pylons/pyramid_beaker/issues>`_
* `pyramid_xmlrpc issue tracker <https://github.com/Pylons/pyramid_xmlrpc/issues>`_
* `pyramid_jinja2 issue tracker <https://github.com/Pylons/pyramid_jinja2/issues>`_
* `Pylons Project issue tracker <https://github.com/Pylons/pylonshq/issues>`_ (All
  bugs with the pylonshq.com/pylonsproject.org website should be reported here.)

Additional projects follow the same pattern
(``https://github.com/Pylons/<projectname>/issues``).

Working on Code
---------------

To fix bugs or add features to a package managed by the Pylons project, an
account on GitHub_ is required. All Pylons Project packages are under the
`Pylons organization on github <http://github.com/Pylons>`_.

The general practice for contributing new features and bug fixes is to `fork
the package <http://help.github.com/forking/>`_ and make changes within a
checkout of the forked repository. Then send a `pull request
<http://help.github.com/pull-requests/>`_.  This allows the developers to
review the patches and accept them, or comment on what needs to be addressed
before the change sets can be accepted.

.. _GitHub: http://github.com/
