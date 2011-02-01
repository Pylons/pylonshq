# -*- coding: utf-8 -*- 
<%inherit file="/page.mako"/>

<%def name="pagename()">Download Pyramid</%def>

<h1>Download Pyramid</h1>

<ul>
	% for archive in downloads:
	<li>pyramid-${archive}</li>
	% endfor
</ul>