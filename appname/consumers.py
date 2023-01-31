from channels.generic.websocket import WebsocketConsumer


class HelloConsumer(WebsocketConsumer):
    groups = ["broadcast"]

    def connect(self):
        self.user = self.scope["user"]
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        if self.user.is_authenticated:
            self.send(text_data=f"Hello {self.user.first_name:} {self.user.last_name}!")
        else:
            self.send(text_data="Hello anonymous!")

    def disconnect(self, close_code):
        ...
