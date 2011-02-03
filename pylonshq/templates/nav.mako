# -*- coding: utf-8 -*-

## HEADER NAV
<%def name="header_nav(active)">\
<%
    active_nav = {}
    active_nav[active or 'home'] = ' class="selected"'
%>\
<nav>
	<div class="header-nav">
		<ul>
			<li><a href="${request.application_url}"${active_nav.get('home', '') | n}>Home</a></li>
			<li><a href="http://docs.pylonsproject.org/">Documentation</a></li>
			<li>
				<a href="${request.application_url}/about"${active_nav.get('about', '') | n}>About</a>
				<div class="header-nav-submenu">
					<ul>
						<li><a href="${request.application_url}/about/pylons">Pylons Project</a></li>
						<li><a href="${request.application_url}/about/history">History</a></li>
						<li><a href="${request.application_url}/about/license">License</a></li>
					</ul>
				</div>
			</li>
			<li>
				<a href="${request.application_url}/projects"${active_nav.get('projects', '') | n}>Projects</a>
				<div class="header-nav-submenu">
					<ul>
						<li><span class="title">Pyramid</span></li>
						<li><a href="${request.application_url}/projects/pyramid/about">About</a></li>
						<li><a href="${request.application_url}/projects/pyramid/download">Download</a></li>
						<li><a href="http://docs.pylonsproject.org/projects/pyramid/1.0/">Documentation</a></li>
						<li><a href="http://docs.pylonsproject.org/projects/pyramid_cookbook/dev/">Cookbook</a></li>
						<li><a href="http://docs.pylonsproject.org/projects/pyramid_tutorials/dev/">Tutorials</a></li>
						<li>&nbsp;</li>
						<li><span class="title">Pylons Framework</span></li>
						<li><a href="${request.application_url}/projects/pylons-framework/about">About</a></li>
						<li><a href="${request.application_url}/projects/pylons-framework/download">Download</a></li>
						<li><a href="http://docs.pylonsproject.org/projects/pylons_framework/dev/">Documentation</a></li>
					</ul>
				</div>
			</li>
			<li>
				<a href="${request.application_url}/community"${active_nav.get('community', '') | n}>Community</a>
				<div class="header-nav-submenu">
					<ul>
						<li><a href="${request.application_url}/community/how-to-participate">How to participate</a></li>
						<li><a href="${request.application_url}/community/how-to-contribute">How to contribute</a></li>
						<li><a href="${request.application_url}/community/code-of-conduct">Code of conduct</a></li>
						<li><a href="${request.application_url}/community/get-support">Get support</a></li>
						<li><a href="${request.application_url}/community/blogs">Blogs</a></li>
					</ul>
				</div>
			</li>
			<li class="last">
				<a href="${request.application_url}/tools"${active_nav.get('tools', '') | n}>Tools</a>
				<div class="header-nav-submenu">
					<ul>
						<li><a href="${request.application_url}/tools/pastebins">Pastebins</a></li>
					</ul>
				</div>
			</li>
		</ul>
	</div>
</nav>
</%def>

## FOOTER NAV
<%def name="footer_nav(active)">\
<%
    active_nav = {}
    active_nav[active or ''] = ' class="selected"'
%>\
<nav>
	<div class="footer-nav">
		<div class="span-6">
			<h4>About</h4>
			<ul>
				<li><a href="${request.application_url}/about/pylons"${active_nav.get('about-pylons', '') | n}>Pylons Project</a></li>
				<li><a href="${request.application_url}/about/history"${active_nav.get('about-history', '') | n}>History</a></li>
				<li><a href="${request.application_url}/about/license"${active_nav.get('about-license', '') | n}>License</a></li>
			</ul>
		</div>
		<div class="span-6">
			<h4>Projects</h4>
			Pyramid
			<ul>
				<li><a href="${request.application_url}/projects/pyramid/about"${active_nav.get('projects-pyramid-about', '') | n}>About</a></li>
				<li><a href="${request.application_url}/projects/pyramid/download"${active_nav.get('projects-pyramid-download', '') | n}>Download</a></li>
				<li><a href="http://docs.pylonsproject.org/projects/pyramid/1.0/">Documentation</a></li>
				<li><a href="http://docs.pylonsproject.org/projects/pyramid_cookbook/dev/">Cookbook</a></li>
				<li><a href="http://docs.pylonsproject.org/projects/pyramid_tutorials/dev/">Tutorials</a></li>
			</ul>
			Pylons Framework
			<ul>
				<li><a href="${request.application_url}/projects/pylons-framework/about"${active_nav.get('projects-pylons-framework-about', '') | n}>About</a></li>
				<li><a href="${request.application_url}/projects/pylons-framework/download"${active_nav.get('projects-pylons-framework-download', '') | n}>Download</a></li>
				<li><a href="http://docs.pylonsproject.org/projects/pylons_framework/dev/">Documentation</a></li>
			</ul>
		</div>
		<div class="span-6">
			<h4>Community</h4>
			<ul>
				<li><a href="${request.application_url}/community/how-to-participate"${active_nav.get('community-how-to-participate', '') | n}>How to participate</a></li>
				<li><a href="${request.application_url}/community/how-to-contribute"${active_nav.get('community-how-to-contribute', '') | n}>How to contribute</a></li>
				<li><a href="${request.application_url}/community/code-of-conduct"${active_nav.get('community-code-of-conduct', '') | n}>Code of conduct</a></li>
				<li><a href="${request.application_url}/community/get-support"${active_nav.get('community-get-support', '') | n}>Get support</a></li>
				<li><a href="${request.application_url}/community/blogs"${active_nav.get('community-blogs', '') | n}>Blogs</a></li>
			</ul>
		</div>
		<div class="span-6 last">
			<h4>Tools</h4>
			<ul>
				##%if not request.user:
				##<li><a href="${request.application_url}/login"${active_nav.get('tools-login', '') | n}>Login</a></li>
				##% else:
				##<li><a href="#">${request.user.username}</a></li>
				##<li><a href="${request.application_url}/logout"${active_nav.get('tools-logout', '') | n}>Logout</a></li>
				##% endif
				<li><a href="${request.application_url}/tools/pastebins"${active_nav.get('tools-pastebins', '') | n}>Pastebins</a></li>
				<li>&nbsp;</li>
				##<li>
				##	<a href="#"><img src="${request.static_url('pylonshq:static/images/social/feed.png')}"></a>
				##	<a href="#"><img src="${request.static_url('pylonshq:static/images/social/twitter.png')}"></a>
				##	<a href="#"><img src="${request.static_url('pylonshq:static/images/social/facebook.png')}"></a>
				##</li>
			</ul>
		</div>
	</div>
</nav>
</%def>

