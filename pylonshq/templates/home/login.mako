# -*- coding: utf-8 -*- 
<%inherit file="/base.mako"/>

<section class="masthead">
	<div id="masthead" class="masthead-page">
		<div id="${c.masthead_logo or 'pylons'}-small-logo" class="png_bg" alt="logo"></div>
	</div>
</section>
		
<div id="main" class="page">
	<div id="container">
		<h2>Login</h2>
    	${form.begin(current_url(request))}
    	${form.csrf()}
    	<div class="form-block">
    	    ${form.label("username", label=_('Username'))}
    	    ${form.text('username')}
			${form.errorlist("username", class_="form-error")}
    	</div>
    	<div class="form-block last-block">
    	    ${form.label("password", label=_('Password'))}
    	    ${form.password('password')}
			${form.errorlist("password", class_="form-error")}
    	</div> 
		<div class="form-buttons">
    		${form.submit("submit", "Login", class_="button")}
		</div>
    	${form.end()}
	</div>
</div>

