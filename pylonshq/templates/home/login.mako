# -*- coding: utf-8 -*- 
<%inherit file="/page.mako"/>

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


