# -*- coding: utf-8 -*-

#### FLASH MESSAGES
<%def name="flash()">
% for q in ('','info','notice','error','success'):
	% if request.session.peek_flash(queue=q):
	<div class="${q or 'info'}">
		<% flash = request.session.pop_flash(queue=q) %>
		${h.literal('<br>'.join(flash))}
	</div>
	% endif
% endfor
</%def>