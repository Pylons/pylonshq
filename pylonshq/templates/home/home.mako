# -*- coding: utf-8 -*- 
<%inherit file="/base.mako"/>
<%namespace name="funcs" file="/funcs.mako"/>
<%!
    from datetime import datetime
%>

<section>
	<div class="masthead">
		<div id="masthead" class="masthead-home">
			<div id="pyramid-medium-logo" class="png_bg">
				<div id="home-highlights">
					<div id="highlight-content">
						<h2>Web development<br>done right, your way!</h2>
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
				<h2>The Pylons Project</h2>
				<div class="about-pylons png_bg">The Pylons Project was founded by the people behind the Pylons web framework to develop web application framework technology in Python. Rather than focusing on a single web framework, the Pylons Project will develop a collection of related technologies. The first package is the Pyramid web framework.</div>
			</div>
			<div class="rightcol">
				<h2>Companies and projects using Pylons Project software</h2>
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
		<div id="latest-info" class="span-8">
			<h2>From the inside</h2>
			<h4>Pyramid 1.0 released</h4>
			<p>Pyramid 1.0 was released on January 30, 2011. Thanks to everyone who contributed to making this release possible. Read the official announcement on <a href="http://groups.google.com/group/pylons-devel/browse_thread/thread/2e0c1d669924ea3f">Google Groups</a>.</p>
			<h4>What's up with Pylons 1.x?</h4>
			<p>Since Pyramid has reached non-alpha release, Pylons the web framework was shifted into legacy status. Read more about <a href="http://docs.pylonsproject.org/faq/pylonsproject.html#what-does-the-pylons-project-mean-for-pylons-the-web-framework">what the Pylons Project mean for Pylons the web framework</a>.</p>
			<h4>Pylons merges with repoze.bfg</h4>
			<p>The Pylons framework developers have merged efforts with the <a href="http://bfg.repoze.org/">repoze.bfg</a> framework under the <a href="https://github.com/Pylons">Pylons Project</a> banner. Read about the <a href="http://docs.pylonsproject.org/">Pylons Project</a> and the joint effort, the <a href="http://docs.pylonsproject.org/projects/pyramid/dev/">Pyramid web framework</a>, and <a href="http://be.groovie.org/post/1558848023/notes-on-the-pylons-repoze-bfg-merger">notes on the merger</a>.</p>
<script src="http://widgets.twimg.com/j/2/widget.js"></script>
<script>
new TWTR.Widget({
  version: 2,
  type: 'search',
  search: '#pyramid #pylons',
  interval: 6000,
  title: '',
  subject: '',
  width: 310,
  height: 310,
  theme: {
    shell: {
      background: '#dddddd',
      color: '#222222'
    },
    tweets: {
      background: '#ffffff',
      color: '#333333',
      links: '#1b5fd6'
    }
  },
  features: {
    scrollbar: true,
    loop: true,
    live: true,
    hashtags: true,
    timestamp: true,
    avatars: true,
    toptweets: true,
    behavior: 'default'
  }
}).render().start();
</script>
		</div>
		<div id="latest-discussions" class="span-8">
			<h2>Latest discussions</h2>
			<ul>
				% for message in discussions:
				<li class="png_bg">
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
		</div>
		<div id="latest-projects" class="span-8 last">
			<h2>Latest project activities</h2>
			<ul>
				% for project in projects:
				<li class="png_bg">
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
