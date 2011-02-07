# -*- coding: utf-8 -*- 
<%inherit file="/page.mako"/>

<%def name="pagename()">Pyramid : Download Pyramid</%def>

<h1 class="title">Download Pyramid</h1>

<p>
	These files are provided for convenience and should be installed in development mode, <b>$ python setup.py develop</b>. For supported installation use <b>$ easy_install pyramid</b> or <b>$ pip install pyramid</b> commands.
</p>
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
			<a href="https://github.com/Pylons/pyramid/tree/${archive}">pyramid-${archive}</a>
			<span class="downloads">
				<a href="https://github.com/Pylons/pyramid/zipball/${archive}">ZIP</a>
				<a href="https://github.com/Pylons/pyramid/tarball/${archive}">TGZ</a>
			</span>
		</li>
		% endfor
	</ul>
</div>