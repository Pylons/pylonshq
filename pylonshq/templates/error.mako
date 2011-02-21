# -*- coding: utf-8 -*- 
<%inherit file="base.mako"/>

<section class="masthead">
	<div id="masthead" class="masthead-page">
		<div id="pylons-small-logo" class="png_bg" alt="logo"></div>
	</div>
</section>
		
<div id="main" class="exception">
	<div id="container">
		<div class="error-number span-12">${number}</div>
		<div class="error-message span-12 last">
			<h2>${error}</h2>
			${message}
		</div>
	</div>
</div>

