from django.contrib.auth.models import User
import random
from user.models import Verification
import re
from common.user.verification import Veriffy, EmailVerification, MobileVerification
from base.interface import VarificationInterface


class VerificationUser(VarificationInterface):
    def __init__(self, **kwargs):

        self.list_key = list(kwargs.keys())
        self.list_value = list(kwargs.values())

    def send(self):
        v = Verification()
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        code = random.randint(1111, 9999)

        if self.list_value[1][:3] in ["090", "091", "092", "093"] or re.search(regex, self.list_value[1]):
            v.verification = code
            v.device = self.list_key[1].lower()
            u, _ = User.objects.get_or_create(username=self.list_value[0])
            u.set_password(self.list_value[0])
            u.save()
            v.user = u
            v.active = True
            v.save()

            if v.device == "mail":
                obg = Veriffy()
                obg.finde_send(EmailVerification(v.verification, self.list_value[1]))

            if v.device == "mobile":
                obg = Veriffy()
                obg.finde_send(MobileVerification(v.verification, self.list_value[1]))

        else:
            raise Exception("please enter mobile number or email address")
