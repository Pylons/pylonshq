# -*- coding: utf-8 -*- 
<%inherit file="/page.mako"/>

<h1>History of Pylons</h1>
<h2>Pylons 0.8 (2005 - 2006)</h2>
<p>
	Developed at a time when many Python frameworks (30+ of them) were vying for users, Ben Bangert, noticed that another Python framework, Bricks had a similar goal and merged development efforts with James Gardner to work on the web development framework that became Pylons.
</p>
<p>
	Pylons first came into existence in September, 2005. Initially it was a customization of the Myghty Python Templating Framework, utilizing page handler customization to provide a MVC oriented web framework. Rather than running under mod_python as was common for Myghty, Pylons ran using Myghty's WSGI handler under Paste.
</p>
<p>
	Unlike most other Python frameworks at the time, Pylons focused heavily on utilizing the WSGI specification for a flexible component based approach to a web application stack. Session handling, caching, the default templating language, and the request/response objects were all handled by Myghty, while Paste was used to load and run the application.
</p>
<h2>Pylons 0.9 - 0.9.7 (2006 - 2009)</h2>
<p>
	Pylons 0.9 was released during O'Reilly's 2006 OSCON and brought some major changes to the internal architecture.
</p>
<p>
	Running as a Myghty page handler customization became a less than optimal design decision, and Pylons 0.9 made a clear break by running entirely as a WSGI application that then used Myghty as needed for templates only. Session handling and caching were handled by a new 3rd party package called Beaker that was based on the caching/session handling subsystem used by Myghty. Request and response objects were provided by light-weight WSGI wrappers in Paste, which was also still used to run and load the web application.
</p>
<p>
	During the development of the 0.9 series, several features of Paste were extracted into smaller, more focused packages. The testing suite became WebTest, the WSGI wrappers became WebOb, and the interactive debugging environment became WebError. Pylons 0.9 follows these developments by switching from using Paste to the new packages which provide more functionality with little to no backwards incompatibility issues.
</p>
<h2>Pylons 1.0 and beyond (2010-)</h2>
<p>
	Pylons 1.0 aims to be a finished and polished web application framework utilizing the newly extracted, and mature Python packages developed in the past few years symbiotically with Pylons.
</p>
<p>
	Current projections are for a Pylons 1.0 release in early 2010.
</p>