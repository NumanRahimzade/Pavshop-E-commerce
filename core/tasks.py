from itertools import product
import time
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from celery import shared_task

from core.models import Subscription
from blog.models import *
from product.models import ProductVersion, Review, ProductImages
from datetime import datetime, timezone, timedelta
from core.publisher import Publish



@shared_task
def process_func():
    time.sleep(15)
    return 'Process done'


@shared_task
def send_mail_to_subscribers():
    # select email from Subscriber # (('idris',), ('idris'), ('idris'))
    # email_list = Subscription.objects.filter(is_active=True).values_list('email', flat=True)
    email_list = []
    g = User.objects.filter(is_active=True).values_list('last_login','username', 'email')
    for gg in g:
        now = datetime.now(timezone.utc)
        if (now-gg[0] > timedelta(days=0)):
            email_list.append(gg[2])
    products = ProductVersion.objects.annotate(num_tags=models.Count('reviews')).filter(created_at__gte=datetime.now(timezone.utc)-timedelta(days=30)).order_by('-num_tags')[:5]
    
    # mail_text = render_to_string('email-subscribers.html', {
    #     'products': products, 
    # })    ##### in case of use of different service
    # mail_text = "salam"
    Publish(data={"body": str(products), "subject": "News about site", "recipients": list(email_list), "subtype": "html"  }, event_type="send_mail")
    # msg = EmailMultiAlternatives(subject='Products', body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list, )
    # msg.attach_alternative(mail_text, "text/html")
    # msg.send()  #### msg part out in  case of use of different service
    # print(email_list)
# 1. background task
# 2. paralel
# 3. periodic task