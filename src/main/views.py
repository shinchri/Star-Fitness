import stripe
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.views import generic, View

from accounts.models import StripeCustomer, Membership

# Create your views here.
class MainView(generic.TemplateView):
  template_name = 'main/main.html'

class HomeView(generic.TemplateView):
  template_name = 'main/index.html'

class MemberView(View):
  
  def get(self, request):
    try:
      if not request.user.is_authenticated:
        return render(request, 'main/member.html')
      # Retrieve the subscription and product 
      stripe_customer = StripeCustomer.objects.get(user=request.user)
      stripe.api_key = settings.STRIPE_SECRET_KEY
      subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
      product = stripe.Product.retrieve(subscription.plan.product)

      # Feel free to fetch any additional data from 'subscription' or 'product'
      # https://stripe.com/docs/api/subscriptions/object
      # https://stripe.com/docs/api/products/object

      context = {
        'subscription': subscription,
        'product': product,
      }

      return render(request, 'main/member.html', context)

    except StripeCustomer.DoesNotExist:
      return render(request, 'main/member.html')