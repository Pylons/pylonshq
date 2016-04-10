# -*- coding: utf-8 -*-
<%inherit file="/page.mako"/>

<%def name="pagename()">Pyramid : Download Pyramid</%def>

<h1 class="title">Download Pyramid</h1>

<p>
	These files are provided for convenience and should be installed in development mode:
</p>

<code><pre># using pip
$ pip install -e .

# using setup.py
$ python setup.py develop</pre></code>

<p>For supported installation, see the
    <a href="http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/install.html">official documentation</a>
    or use one of the following commands:</p>

<code><pre># using pip
$ pip install pyramid

# using easy_install
$ easy_install pyramid</pre></code>

<div id="downloads">
	<ul>
		<li>
			<a href="https://github.com/Pylons/pyramid/tree/master">pyramid-master</a>
			<span class="downloads">
				<a href="https://github.com/Pylons/pyramid/zipball/master">ZIP</a>
				<a href="https://github.com/Pylons/pyramid/tarball/master">TGZ</a>
			</span>
		</li>
		% for archive in downloads:
		<li>
			<a href="https://github.com/Pylons/pyramid/tree/${archive.name}">pyramid-${archive.name}</a>
			<span class="downloads">
				<a href="${archive.zipball_url}">ZIP</a>
				<a href="${archive.tarball_url}">TGZ</a>
			</span>
		</li>
		% endfor
	</ul>
</div>