from django.contrib.auth.views import LoginView, LogoutView

class MemberLoginView(LoginView):
    template_name = 'member_app/login.html'

class MemberLogoutView(LogoutView):
    pass  
