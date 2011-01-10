# -*- coding: utf-8 -*-

## HEADER NAV
<%def name="header_nav(active)">\
<%
    active_nav = {}
    active_nav[active or 'home'] = ' class="selected"'
%>\
<nav class="header-nav">
	<ul>
		<li><a href="${request.application_url}"${active_nav.get('home', '') | n}>Home</a></li>
		<li><a href="${request.application_url}/pylons"${active_nav.get('pylons', '') | n}>Pylons Project</a></li>
		<li><a href="${request.application_url}/projects"${active_nav.get('projects', '') | n}>Projects</a></li>
		<li><a href="${request.application_url}/community"${active_nav.get('community', '') | n}>Community</a></li>
		<li class="last"><a href="${request.application_url}/tools"${active_nav.get('tools', '') | n}>Tools</a></li>
	</ul>
</nav>
</%def>

## FOOTER NAV
<%def name="footer_nav(active)">\
<%
    active_nav = {}
    active_nav[active or ''] = ' class="selected"'
%>\
<nav class="footer-nav">
	<div class="span-5">
		<h4>Pylons Project</h4>
		<ul>
			<li><a href="${request.application_url}/pylons/about"${active_nav.get('pylons-about', '') | n}>About</a></li>
			<li><a href="${request.application_url}/pylons/history"${active_nav.get('pylons-history', '') | n}>History</a></li>
			<li><a href="${request.application_url}/pylons/open-source"${active_nav.get('pylons-open-source', '') | n}>Open Source</a></li>
			<li><a href="${request.application_url}/pylons/licence"${active_nav.get('pylons-licence', '') | n}>Licence</a></li>
			##<li><a href="${request.application_url}/news">News</a></li>
		</ul>
	</div>
	<div class="span-5">
		<h4>Projects</h4>
		Pyramid
		<ul>
			<li><a href="${request.application_url}/projects/pyramid/about"${active_nav.get('projects-pyramid-about', '') | n}>About</a></li>
			<li><a href="${request.application_url}/projects/pyramid/download"${active_nav.get('projects-pyramid-download', '') | n}>Download</a></li>
			<li><a href="http://docs.pylonshq.com/pyramid/dev/">Documentation</a></li>
			##<li><a href="#">Tutorials</a></li>
			##<li><a href="#">Guides</a></li>
			##<li><a href="#">Cookbook</a></li>
		</ul>
		Pylons Framework
		<ul>
			<li><a href="${request.application_url}/projects/pylons-framework/about"${active_nav.get('projects-pylons-framework-about', '') | n}>About</a></li>
			<li><a href="${request.application_url}/projects/pylons-framework/download"${active_nav.get('projects-pylons-framework-download', '') | n}>Download</a></li>
			<li><a href="http://docs.pylonshq.com/pylons/dev/">Documentation</a></li>
		</ul>
	</div>
	<div class="span-5">
		<h4>Community</h4>
		<ul>
			<li><a href="${request.application_url}/community/how-to-participate"${active_nav.get('community-how-to-participate', '') | n}>How to participate</a></li>
			<li><a href="${request.application_url}/community/how-to-contribute"${active_nav.get('community-how-to-contribute', '') | n}>How to contribute</a></li>
			<li><a href="${request.application_url}/community/get-support"${active_nav.get('community-get-support', '') | n}>Get support</a></li>
			<li><a href="${request.application_url}/community/blogs"${active_nav.get('community-blogs', '') | n}>Blogs</a></li>
			##<li><a href="#">Jobs</a></li>
		</ul>
	</div>
	<div class="span-5">
		<h4>Tools</h4>
		<ul>
			<li><a href="${request.application_url}/tools/pastebins"${active_nav.get('tools-pastebins', '') | n}>Pastebins</a></li>
			##<li><a href="${request.application_url}/tools/tracebacks"${active_nav.get('tools-tracebacks', '') | n}>Tracebacks</a></li>
		</ul>
	</div>
	<div class="span-4 last">
		<h4>Follow Us</h4>
		<ul>
			<li>
				<a href="#"><img src="${request.static_url('pylonshq:static/images/social/feed.png')}"></a>
				<a href="#"><img src="${request.static_url('pylonshq:static/images/social/twitter.png')}"></a>
				<a href="#"><img src="${request.static_url('pylonshq:static/images/social/facebook.png')}"></a>
			</li>
		</ul>
	</div>
</nav>
</%def>

