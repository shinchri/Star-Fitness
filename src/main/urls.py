from django.urls import path

from accounts.views import stripe_config, create_checkout_session, stripe_webhook, SuccessView, CancelledView
from .views import HomeView, MainView, MemberView

app_name = 'main'

urlpatterns = [
  path('', MainView.as_view(), name="main"),
  path('home/', HomeView.as_view(), name="home"),
  path('member/', MemberView.as_view(), name="member"),
  path('config/', stripe_config, name="config"),
  path('create-checkout-session/<int:id>/', create_checkout_session, name="create-checkout"),
  path('success/', SuccessView.as_view()),
  path('cancel/', CancelledView.as_view()),
  path('webhook/', stripe_webhook),
]