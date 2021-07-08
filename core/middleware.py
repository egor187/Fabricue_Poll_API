from django.contrib.auth import authenticate, login


def auto_login(get_response):
    """
    Middleware for  users 'auto-login'
    """

    def middleware(request):

        if not request.user.is_authenticated:
            user = authenticate(username="postman", password="test12345")
            login(request, user)

        response = get_response(request)
        return response

    return middleware


