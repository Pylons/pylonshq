def groupfinder(userid, request):
    if userid and hasattr(request, 'user') and request.user: 
        return [g.group_name for g in request.user.groups]
    return []