History of Pylons
=================

Pylons initially started and referred just the Pylons Framework before the merger that resulted in the Pylons Project. The below timeline starts with the Pylons Framework to provide the background for how the Pylons Project came to be, how the developers ended up merging their efforts, and the origin projects. Some background is also provided on the other frameworks that merged to form the Pylons Project.

Pylons 0.8 (2005 - 2006)
-------------------------

Pylons was developed at a time when many Python frameworks (30+ of them) were vying for users. Ben Bangert noticed that another Python framework, Bricks, had a similar goal and merged development efforts with James Gardner to work on the web development framework that became Pylons.

Pylons first came into existence in September, 2005. Initially it was a customization of the Myghty Python Templating Framework, utilizing page handler customization to provide a MVC oriented web framework. Rather than running under mod_python as was common for Myghty, Pylons ran using Myghty's WSGI handler under Paste.

Unlike most other Python frameworks at the time, Pylons focused heavily on utilizing the WSGI specification for a flexible component based approach to a web application stack. Session handling, caching, the default templating language, and the request/response objects were all handled by Myghty, while Paste was used to load and run the application, and Routes was created to handle URL dispatching and generation. Around this time, Phil Jenvey joined the development team and began working actively on Pylons.

Pylons 0.9 - 0.9.7 (2006 - 2009)
--------------------------------

Pylons 0.9 was released during O'Reilly's 2006 OSCON and brought some major changes to the internal architecture.

Running as a Myghty page handler customization became a less than optimal design decision, and Pylons 0.9 made a clear break by running entirely as a WSGI application that then used Myghty as needed for templates only. Session handling and caching were handled by a new 3rd party package called Beaker that was based on the caching/session handling subsystem used by Myghty. Request and response objects were provided by light-weight WSGI wrappers in Paste, which was also still used to run and load the web application.

During the development of the 0.9 series, several features of Paste were extracted into smaller, more focused packages. The testing suite became WebTest, the WSGI wrappers became WebOb, and the interactive debugging environment became WebError. Pylons 0.9 follows these developments by switching from using Paste to the new packages which provide more functionality with little to no backwards incompatibility issues.

Pylons 1.0 and 1.1 (2010-2011)
------------------------------

Pylons 1.0 is a polished release of the Pylons framework, to be followed by a Pylons 1.1 in 2011 that will include additional forward-compatible Pyramid capabilities to ease the transition to the new web framework.

