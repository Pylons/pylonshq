# -*- coding: utf-8 -*- 
<%inherit file="/base.mako"/>
<%namespace name="funcs" file="/funcs.mako"/>

<section>
	<div class="masthead">
		<div id="masthead" class="masthead-home">
			<div id="pyramid-medium-logo" class="png_bg">
				<div id="home-highlights">
					<div id="highlight-content">
						<h2>Web Development<br>done right, your way !</h2>
						<ul>
							<li class="png_bg">Simple</li>
							<li class="png_bg">Fast</li>
							<li class="png_bg">Documented</li>
							<li class="png_bg">Tested</li>
						</ul>
					</div>
					<div id="highlight-download" class="auto-height">
						<div class="download png_bg">
							<h3>Download</h3>
							version 1.0
						</div>
						<div class="options">
							Download packages
							<ul>
								<li class="package">
									<a href="https://github.com/Pylons/pyramid/zipball/1.0">1.0.zip</a>
								</li>
								<li class="package last">
									<a href="https://github.com/Pylons/pyramid/tarball/1.0">1.0.tar.gz</a>
								</li>
							</ul>
							or $ easy_install pyramid
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</section>

<section>
	<div class="feature">
		<div id="feature">
			<div class="leftcol">
				<h4>The Pylons Project</h4>
				<div class="about-pylons png_bg">The Pylons Project was founded by the people behind the Pylons web framework to develop web application framework technology in Python. Rather than focusing on a single web framework, the Pylons Project will develop a collection of related technologies.</div>
			</div>
			<div class="rightcol">
				<h4>Some companies or projects using Pylons Project</h4>
				<div id="company-slideshow">
    	        	<ul>
    	        	    <li><a href="http://www.adroll.com/"><img src="${request.static_url('pylonshq:static/images/logos/adroll.jpg')}" /></a></li>
    	        	    <li><a href="http://www.bittorrent.com/"><img src="${request.static_url('pylonshq:static/images/logos/bittorrent.jpg')}" /></a></li>
						<li><a href="http://digg.com/"><img src="${request.static_url('pylonshq:static/images/logos/digg.jpg')}" /></a></li>
    	        	</ul>
    	        	<ul>
    	        	    <li><a href="https://www.dropbox.com/"><img src="${request.static_url('pylonshq:static/images/logos/dropbox.jpg')}" /></a></li>
						<li><a href="http://www.freshbooks.com/"><img src="${request.static_url('pylonshq:static/images/logos/freshbooks.jpg')}" /></a></li>
    	        	    <li><a href="http://www.imagemoversdigital.com/"><img src="${request.static_url('pylonshq:static/images/logos/imagemoversdigital.jpg')}" /></a></li>
    	        	</ul>
    	        	<ul>
						<li><a href="http://www.lolapps.com/"><img src="${request.static_url('pylonshq:static/images/logos/lolapps.jpg')}" /></a></li>
    	        	    <li><a href="http://www.mochimedia.com/"><img src="${request.static_url('pylonshq:static/images/logos/mochimedia.jpg')}" /></a></li>
						<li><a href="http://www.opera.com/"><img src="${request.static_url('pylonshq:static/images/logos/opera.jpg')}" /></a></li>
    	        	</ul>
    	        	<ul>
    	        	    <li><a href="http://oreilly.com/"><img src="${request.static_url('pylonshq:static/images/logos/oreilly.jpg')}" /></a></li>
    	        	    <li><a href="http://saucelabs.com/"><img src="${request.static_url('pylonshq:static/images/logos/saucelabs.jpg')}" /></a></li>
    	        	    <li><a href="http://www.reddit.com/"><img src="${request.static_url('pylonshq:static/images/logos/reddit.jpg')}" /></a></li>
					</ul>
    	        	<ul>
    	        	    <li><a href="http://sourceforge.net/"><img src="${request.static_url('pylonshq:static/images/logos/sourceforge.jpg')}" /></a></li>
    	        	    <li><a href="http://www.tineye.com/"><img src="${request.static_url('pylonshq:static/images/logos/tineye.jpg')}" /></a></li>
    	        	    <li><a href="http://www.wetafx.co.nz/"><img src="${request.static_url('pylonshq:static/images/logos/wetadigital.jpg')}" /></a></li>
    	        	</ul>
    	    	</div>
			</div>
		</div>
	</div>
</section>
		
<div id="main" class="home">
	<div id="container">
		${funcs.flash()}
		<div id="latest-news" class="span-8">
			<h3>Latest news</h3>
		</div>
		<div id="latest-something" class="span-8">
			<h3>Latest ...</h3>
		</div>
		<div id="latest-projects" class="span-8 last">
			<h3>Latest project activities</h3>
			<ul>
				% for project in projects:
				<li>
					<div class="project">
						<a class="name" href="${project.url}">${project.name}</a>
						<span class="downloads">
							<a href="${project.url}/zipball/master">ZIP</a> <a href="${project.url}/tarball/master">TGZ</a>
						</span>
					</div>
					<div class="description">${project.description}</div>
				</li>
				% endfor
			</ul>
		</div>
		<div class="clear">&nbsp;</div>
	</div>
</div>
