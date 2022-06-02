import json
from django.conf import settings


class Publish:
    channel_name = "events"

    def __init__(self, data, event_type):
        self.data = data 
        self.event_type = event_type
        self._publish()
        # data = {
        #     "body": "Salam necesen?",
        #     "subject": "Salam",
        #     "recipients": ['idris.sabanli@gmail.com', 'yusif@gmail.com'],
        #     "subtype": "html"
        # }
        

    def _stringfy(self):
        return json.dumps({
            "data": self.data,
            "event_type": self.event_type
        })

    def _publish(self):
        settings.REDIS_CLIENT.publish(self.channel_name, self._stringfy())

        # stringfy() = '{"data": {"body": "Salam necesen?","subject": "Salam", "recipients": ["idris.sabanli@gmail.com", "yusif@gmail.com"], "subtype": "html"}, event_type="send_mail" }'