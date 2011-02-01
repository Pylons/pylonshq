.. _featuresbugs:

Adding Features and Reporting Bugs
==================================

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

.. _contributing:

Contributing Source Code and Documentation
==========================================

Pylons Project subprojects follow a coding style, with minimum standards:
http://docs.pylonsproject.org/community/codestyle.html .  All substantive
code contributions to the Pylons Project must be tested; see
http://docs.pylonsproject.org/community/testing.html .

For substantive contributions to its major projects, The Pylons Project
requires the following of its contributors:

- An assignment of half-ownership of submitted code or documentation for
  substantive contributions to its official projects.  We require the
  assignment because we're interested in, eventually, giving the copyright to
  the code to a foundation.  Obtaining half-ownership of the code makes it
  possible for us to do this credibly without chasing people for permission
  to do so when that time comes.

- Assurance that the contributor will not check in incompatibly-licensed
  code.

- Assurance that the contributor will not allow his submission credentials to
  be used by a third party who may not agree to the constraints of a
  contribution agreement.

- Assurance that the submitted code does not infringe upon or violate the
  rights of a third party.

- Assurance that the contributor understands any licensing exceptions local
  to the repository he is contributing to.

"Signing" a contribution agreement is simple: just add your name and a date
to the bottom of a "CONTRIBUTORS.txt" file found in the root of the Pylons
project you'd like to contribute to.  Optimally, this will be done when you
submit code through GitHub (whether via a pull request from a separate
repository fork, or by direct push if you have push access to the canonical
project repository).  Your intent to abide by the contributor agreement is
signified by your commit to the "CONTRIBUTORS.txt" file with your name and a
date.

Examples of "substantive" contributions:

- Submitting a new feature for review.

- Submitting artwork.

- Submitting a new chapter to documentation.

For bugfixes and other minor contributions, signing the contributor file is
usually not required.  However, the reviewer of a particular submission is
the arbiter of whether that submission requires the signing of the
contributors file.

A sample of the current contributor agreement is reproduced in full below::

    Pylons Project Contributor Agreement
    ====================================

    The submitter agrees by adding his or her name within the section below
    named "Contributors" and submitting the resulting modified document to
    the canonical shared repository location for this software project
    (whether directly, as a user with "direct commit access", or via a "pull
    request"), he or she is signing a contract electronically.  The submitter
    becomes a Contributor after a) he or she signs this document by adding
    their name beneath the "Contributors" section below, and b) the resulting
    document is accepted into the canonical version control repository.

    Treatment of Account
    ---------------------

    Contributor will not allow anyone other than the Contributor to use his
    or her username or source repository login to submit code to a Pylons
    Project source repository. Should Contributor become aware of any such
    use, Contributor will immediately by notifying Agendaless Consulting.
    Notification must be performed by sending an email to
    webmaster@agendaless.com.  Until such notice is received, Contributor
    will be presumed to have taken all actions made through Contributor's
    account. If the Contributor has direct commit access, Agendaless
    Consulting will have complete control and discretion over capabilities
    assigned to Contributor's account, and may disable Contributor's account
    for any reason at any time.

    Legal Effect of Contribution
    ----------------------------

    Upon submitting a change or new work to a Pylons Project source
    Repository (a "Contribution"), you agree to assign, and hereby do assign,
    a one-half interest of all right, title and interest in and to copyright
    and other intellectual property rights with respect to your new and
    original portions of the Contribution to Agendaless Consulting. You and
    Agendaless Consulting each agree that the other shall be free to exercise
    any and all exclusive rights in and to the Contribution, without
    accounting to one another, including without limitation, the right to
    license the Contribution to others under the Repoze Public License. This
    agreement shall run with title to the Contribution. Agendaless Consulting
    does not convey to you any right, title or interest in or to the Program
    or such portions of the Contribution that were taken from the
    Program. Your transmission of a submission to the Pylons Project source
    Repository and marks of identification concerning the Contribution itself
    constitute your intent to contribute and your assignment of the work in
    accordance with the provisions of this Agreement.

    License Terms
    -------------

    Code committed to the Pylons Project source repository (Committed Code)
    must be governed by the Repoze Public License
    (http://repoze.org/LICENSE.txt, aka "the RPL") or another license
    acceptable to Agendaless Consulting.  Until Agendaless Consulting
    declares in writing an acceptable license other than the RPL, only the
    RPL shall be used.  A list of exceptions is detailed within the
    "Licensing Exceptions" section of this document, if one exists.

    Representations, Warranty, and Indemnification
    ----------------------------------------------

    Contributor represents and warrants that the Committed Code does not
    violate the rights of any person or entity, and that the Contributor has
    legal authority to enter into this Agreement and legal authority over
    Contributed Code. Further, Contributor indemnifies Agendaless Consulting
    against violations.

    Cryptography
    ------------

    Contributor understands that cryptographic code may be subject to
    government regulations with which Agendaless Consulting and/or entities
    using Committed Code must comply. Any code which contains any of the
    items listed below must not be checked-in until Agendaless Consulting
    staff has been notified and has approved such contribution in writing.

    - Cryptographic capabilities or features

    - Calls to cryptographic features

    - User interface elements which provide context relating to cryptography

    - Code which may, under casual inspection, appear to be cryptographic.

    Notices
    -------

    Contributor confirms that any notices required will be included in any
    Committed Code.

    Licensing Exceptions
    ====================

    None

    List of Contributors
    ====================

    The below-signed are contributors to a code repository that is part of
    the project named "XXX".  Each below-signed contributor has read,
    understand and agrees to the terms above in the section within this
    document entitled "Pylons Project Contributor Agreement" as of the date
    beside his or her name.

    Contributors
    ------------

    - Wile E. Coyote, 2010/11/08

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

