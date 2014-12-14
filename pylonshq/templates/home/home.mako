# -*- coding: utf-8 -*-
<%inherit file="/base.mako"/>
<%namespace name="funcs" file="/funcs.mako"/>

<section>
	<div class="masthead">
		<div id="masthead" class="masthead-home">
			<div id="highlight-slideshow">
				<div class="highlight-item">
					<div id="pyramid-medium-logo" class="png_bg">
						<div id="home-highlights">
							<div id="highlight-content">
								<h2>Web development<br>with style, your way!</h2>
								##<ul>
								##	<li class="png_bg">Simple</li>
								##	<li class="png_bg">Fast</li>
								##	<li class="png_bg">Documented</li>
								##	<li class="png_bg">Tested</li>
								##</ul>
							</div>
							<div id="highlight-download">
								<div class="download png_bg">
									<h3>Download</h3>
									<div class="version">version 1.5</div>
									<div class="license">
										Open source, <a href="${request.application_url}/about/license">BSD-like license</a>
									</div>
								</div>
								<div class="options">
									##Install Pyramid
									<ul>
										<li class="package">
											<a href="https://pypi.python
											.org/packages/source/p/pyramid/pyramid-1.5.tar.gz#md5=8747658dcbab709a9c491e43d3b0d58b">pyramid-1.5.tar.gz</a>
										</li>
										<li class="command">
											$ easy_install -U pyramid
										</li>
										##<li class="command">
										##	$ pip install pyramid
										##</li>
									</ul>
								</div>
							</div>
							<div id="highlight-features">
								<ul>
									<li class="png_bg">Simple</li>
									<li class="png_bg">Fast</li>
									<li class="png_bg">Documented</li>
									<li class="png_bg">Tested</li>
								</ul>
							</div>
						</div>
					</div>
				</div>
				<div class="highlight-item">
					<div id="pyramid-tee-banner" class="png_bg">
						<div id="home-highlights">
							<div id="highlight-content">
								<h2>Not Built By Aliens<br>Pyramid T-Shirt!</h2>
								<p>Design was done by artist <a href="http://www.felixlaflamme.com/">Felix Laflamme</a>,<br> watch a work in progress video on <a href="http://www.youtube.com/watch?v=JWj3poGhZXE&list">YouTube</a></p>
								<h3>Want a T-Shirt?</h3>
								<h2><a href="http://pylonsproject.storenvy.com/">BUY HERE!</a></h2>
							</div>
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
				<h2>The Pylons Project</h2>
				<div class="about-pylons png_bg">The Pylons Project was founded by the people behind the Pylons web framework to develop web application framework technology in Python. Rather than focusing on a single web framework, the Pylons Project will develop a collection of related technologies. The first package is the Pyramid web framework.</div>
			</div>
			<div class="rightcol">
				<h2>Who's using Pylons Project software</h2>
				<div id="company-slideshow">
                    <ul>
    	        	    <li><a href="http://www.adroll.com/"><img src="${request.static_url('pylonshq:static/images/logos/adroll.jpg')}" /></a></li>
						<li><a href="http://getbirdseye.com/"><img src="${request.static_url('pylonshq:static/images/logos/birdseye.jpg')}" /></a></li>
    	        	    <li><a href="http://buzzumi.com/"><img src="${request.static_url('pylonshq:static/images/logos/buzzumi.jpg')}" /></a></li>
    	        	</ul>
    	        	<ul>
						<li><a href="http://www.bittorrent.com/"><img src="${request.static_url('pylonshq:static/images/logos/bittorrent.jpg')}" /></a></li>
						<li><a href="http://www.newcars.com/"><img src="${request.static_url('pylonshq:static/images/logos/carscom.jpg')}" /></a></li>
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
						<li><a href="http://www.surveymonkey.com/"><img src="${request.static_url('pylonshq:static/images/logos/surveymonkey.jpg')}" /></a></li>
    	        	    <li><a href="http://www.tineye.com/"><img src="${request.static_url('pylonshq:static/images/logos/tineye.jpg')}" /></a></li>
    	        	</ul>
    	        	<ul>
    	        	    <li><a href="http://www.wetafx.co.nz/"><img src="${request.static_url('pylonshq:static/images/logos/wetadigital.jpg')}" /></a></li>
    	        	    <li><a href="http://www.netsight.co.uk/"><img width='100px' src="${request.static_url('pylonshq:static/images/logos/netsight.jpg')}" /></a></li>
                        <li><a href="http://itcase.pro/"><img width='100px' src="${request.static_url('pylonshq:static/images/logos/itcase.png')}" /></a></li>
    	        	</ul>
    	    	</div>
			</div>
		</div>
	</div>
</section>

<div id="main" class="home">
	<div id="container">
		${funcs.flash()}
		<div id="latest-info" class="span-8">
			<h2>From the inside</h2>
			<div id="inside-rst">
				${inside|n}
			</div>
		</div>
		<div id="latest-discussions" class="span-8">
			<h2>Latest discussions</h2>
			% if discussions:
			<ul>
				% for message in discussions:
				<li>
					<div class="title">
						<a href="${message['link']}">${message['title']}</a>
					</div>
					<div class="author">
						${message['author']}
						<span class="updated">${message['updated']}</span>
					</div>
				</li>
				% endfor
			</ul>
			% else:
			<div class="title">
				No discussions for now... Come back later.
			</div>
			% endif
			<br>
			<h2>Latest tweets</h2>
			<a class="twitter-timeline" href="https://twitter.com/search?q=pyramid%2Cpylons" data-widget-id="366242367298211841">Tweets about "pyramid,pylons"</a>
            <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+"://platform.twitter.com/widgets.js";fjs.parentNode.insertBefore(js,fjs);}}(document,"script","twitter-wjs");</script>

		</div>
		<div id="latest-projects" class="span-8 last">
			<h2>Latest project activities</h2>
			% if projects:
			<ul>
				% for project in projects:
				<li>
					<div class="project">
						<a class="name" href="${project.html_url}">${project.name}</a>
						##<span class="downloads">
						##	<a href="${project.url}/zipball/master">ZIP</a> <a href="${project.url}/tarball/master">TGZ</a>
						##</span>
					</div>
					<div class="description">${project.description}</div>
				</li>
				% endfor
			</ul>
			% else:
			<div class="title">
				No activities for now... Come back later.
			</div>
			% endif
		</div>
		<div class="clear">&nbsp;</div>
	</div>
</div>
