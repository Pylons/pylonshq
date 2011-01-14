# -*- coding: utf-8 -*- 
<%inherit file="base.mako"/>

<section class="masthead">
	<div id="masthead" class="masthead-page">
		<div id="${c.masthead_logo or 'pylons'}-small-logo" class="png_bg" alt="logo"></div>
	</div>
</section>
		
<div id="main" class="page">
	<div id="container">
		${next.body()}
	</div>
</div>

