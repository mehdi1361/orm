from django.conf import settings
from django.core.mail import send_mail
from base.interface import VarificationInterface
import kavenegar
from rest_framework.response import Response

class EmailVerification(VarificationInterface):

    def __init__(self, verification, email):
        self.verification = verification
        self.email = email

    def send(self):
        subject = 'security code'
        print("valllue:", subject


              )
        message = f'the security code is {self.verification}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.email, ]
        send_mail(subject, message, email_from, recipient_list)


class MobileVerification(VarificationInterface):
    def __init__(self, verification, number):
        self.verification = verification
        self.nubmer = number

    def send(self):
        try:
            api = kavenegar.KavenegarAPI('566A7551674C5341504563716D4B344E465747454767556F4C672B61456B424B36476359372B682F6C6D383D')
            params = {
                'sender': '10004346',
                'receptor': self.nubmer,
                'message': f'the seccurity code is {self.verification}'
            }
            Response(api.sms_send(params))

        except kavenegar.APIException:
            raise Exception('this is a not api')
        except kavenegar.HTTPException:
            raise Exception('the http error')


class Veriffy(object):
    def finde_send(self, object_type):
        return object_type.send()
