Participating
=============

Unfortunately no code is perfect, sometimes bugs will occur, or a feature is
desired. When reporting bugs, being as thorough as possible, and including
additional details makes a huge improvement. No one should feel discouraged in
attempting to fix a bug or suggest a feature that might be missing.

Most interaction with the Pylons Project is done via `The Pylons GitHub
organization <https://github.com/organizations/Pylons>`_.

Reporting a Bug
---------------

Bugs with a Pylons Project package should be reported to the individual issue
tracker on GitHub_. First, some general guidelines on reporting a bug.

1) Create a GitHub account
!!!!!!!!!!!!!!!!!!!!!!!!!!

You will need to  `create a GitHub account <https://github.com/signup/free>`_
account to report and correspond regarding the bug you are reporting.

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

Search through the appropriate Issue tracker on GitHub_. If a bug like yours
was found, check to see if you have new information that could be reported to
help the developers fix it.

4) Collect information about the bug
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

To have the best chance of having a bug fixed, we need to be able to easily
replicate the conditions that caused it. Most of the time this information
will be from a Python traceback message, though some bugs might be in design,
spelling, or other errors on the website/docs/code.

If the error is from a Python traceback (`see a Python traceback 
<http://pastebin.com/TyaPKpt9>`_), include it in the bug report being filed.
We will also need to know what platform you're running (Windows, OSX, Linux),
and which Python interpreter you're running if its not CPython (e.g. Jython, 
Google App Engine).

5) Submit the bug
!!!!!!!!!!!!!!!!!

By default GitHub_ will email you to let you know when new comments have been
made on your bug. In the event you've turned this feature off, you should
check back on occasion to ensure you don't miss any questions a developer
trying to fix the bug might ask.

.. _issue_trackers:

Issue Trackers
--------------

Bugs are reported and tracked on GitHub_'s issue trackers. Each Pylons Project
has their own:

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
the package <http://help.github.com/forking/>`_ in question and make changes
there. Then send a `pull request <http://help.github.com/pull-requests/>`_.
This allows the developers to review the patches and accept them, or comment
on what needs to be addressed before the change sets can be accepted.

.. _conduct:

Community Code of Conduct
=========================

The Pylons Project developers work their hardest to adhere to a common
community code of conduct based heavily on the `Ubuntu Code of Conduct
<http://www.ubuntu.com/community/conduct>`_. We would greatly appreciate it if
everyone contributing and interacting with projects under Pylons also followed
this Code of Conduct.

Be considerate.
---------------

Your work will be used by other people, and you in turn will depend on the
work of others. Any decision you take will affect users and colleagues, and we
expect you to take those consequences into account when making decisions. For
example, when we are in a feature freeze, please don't upload dramatically new
versions of critical system software, as other people will be testing the
frozen system and will not be expecting big changes.

Be respectful.
--------------

The Pylons community and its members treat one another with respect. Everyone
can make a valuable contribution to Pylons. We may not always agree, but
disagreement is no excuse for poor behavior and poor manners. We might all
experience some frustration now and then, but we cannot allow that frustration
to turn into a personal attack. It's important to remember that a community
where people feel uncomfortable or threatened is not a productive one. We
expect members of the Pylons community to be respectful when dealing with
other contributors as well as with people outside the Pylons project and with
users of Pylons.

Be collaborative.
-----------------

Pylons and Free Software are about collaboration and working together.
Collaboration reduces redundancy of work done in the Free Software world, and
improves the quality of the software produced. You should aim to collaborate
with other Pylons maintainers, as well as with the upstream community that is
interested in the work you do. Your work should be done transparently and
patches from Pylons should be given back to the community when they are made,
not just when the distribution releases. If you wish to work on new code for
existing upstream projects, at least keep those projects informed of your
ideas and progress. It may not be possible to get consensus from upstream or
even from your colleagues about the correct implementation of an idea, so
don't feel obliged to have that agreement before you begin, but at least keep
the outside world informed of your work, and publish your work in a way that
allows outsiders to test, discuss and contribute to your efforts.

When you disagree,
------------------

consult others. Disagreements, both political and technical, happen all the
time and the Pylons community is no exception. The important goal is not to
avoid disagreements or differing views but to resolve them constructively. You
should turn to the community and to the community process to seek advice and
to resolve disagreements. There are several Project Teams and Team Leaders,
who may be able to help you figure out which direction will be most
acceptable. If you really want to go a different way, then we encourage you to
make a derivative distribution or alternative set of packages that still build
on the work we've done to utilize as common of a core as possible.

When you are unsure,
--------------------

ask for help. Nobody knows everything, and nobody is expected to be perfect in
the Pylons community (except of course the BDFL). Asking questions avoids
many problems down the road, and so questions are encouraged. Those who are
asked should be responsive and helpful. However, when asking a question, care
must be taken to do so in an appropriate forum. Off-topic questions, such as
requests for help on a development mailing list, detract from productive
discussion.

Step down considerately.
------------------------

Developers on every project come and go and Pylons is no different. When you
leave or disengage from the project, in whole or in part, we ask that you do
so in a way that minimizes disruption to the project. This means you should
tell people you are leaving and take the proper steps to ensure that others
can pick up where you leave off.

.. _GitHub: http://github.com/
