# -*- coding: utf-8 -*- 
<%inherit file="/page.mako"/>

<%def name="pagename()">Download Pylons Framework</%def>

<h1>Download Pylons Framework</h1>

<div id="downloads">
	<ul>
		<li>
			pylons-master
			<span class="downloads">
				<a href="https://github.com/Pylons/pylons/zipball/master">ZIP</a>
				<a href="https://github.com/Pylons/pylons/tarball/master">TGZ</a>
			</span>
		</li>
		% for archive in downloads:
		<li>
			pylons-${archive}
			<span class="downloads">
				<a href="https://github.com/Pylons/pylons/zipball/${archive}">ZIP</a>
				<a href="https://github.com/Pylons/pylons/tarball/${archive}">TGZ</a>
			</span>
		</li>
		% endfor
	</ul>
</div>