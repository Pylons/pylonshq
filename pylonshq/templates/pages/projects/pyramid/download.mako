# -*- coding: utf-8 -*- 
<%inherit file="/page.mako"/>

<%def name="pagename()">Download Pyramid</%def>

<h1 class="title">Download Pyramid</h1>

<div id="downloads">
	<ul>
		<li>
			pyramid-master
			<span class="downloads">
				<a href="https://github.com/Pylons/pyramid/zipball/master">ZIP</a>
				<a href="https://github.com/Pylons/pyramid/tarball/master">TGZ</a>
			</span>
		</li>
		% for archive in downloads:
		<li>
			pyramid-${archive}
			<span class="downloads">
				<a href="https://github.com/Pylons/pyramid/zipball/${archive}">ZIP</a>
				<a href="https://github.com/Pylons/pyramid/tarball/${archive}">TGZ</a>
			</span>
		</li>
		% endfor
	</ul>
</div>