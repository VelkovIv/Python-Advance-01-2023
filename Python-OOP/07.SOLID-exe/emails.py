from abc import ABC, abstractmethod


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass


class IContent(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def format(self):
        pass


class MyContent(IContent):

    def format(self):
        return ''.join(['<myML>', self.text, '</myML>'])


class IMProtocol(ABC):
    def __init__(self, protocol):
        self.protocol = protocol

    @property
    def protocol(self):
        return self.__protocol

    @protocol.setter
    def protocol(self, value):
        if value == 'IM':
            self.__protocol = value


class IMSender(IMProtocol):
    def __init__(self, protocol, info_sender):
        super().__init__(protocol)
        self.info_sender = info_sender

    def get_sender(self):
        return ''.join(["I'm ", self.info_sender])


class IMReceiver(IMProtocol):
    def __init__(self, protocol, info_receiver):
        super().__init__(protocol)
        self.info_receiver = info_receiver

    def get_receiver(self):
        return ''.join(["I'm ", self.info_receiver])


class Email(IEmail):

    def __init__(self):
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        self.__sender = sender.get_sender()

    def set_receiver(self, receiver):
        self.__receiver = receiver.get_receiver()

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


# email = Email('IM', 'MyML')
# email.set_sender('qmal')
# email.set_receiver('james')
# email.set_content('Hello, there!')
# print(email)

# email = Email('IM')
# email.set_sender('qmal')
# email.set_receiver('james')
# content = MyContent('Hello, there!')
# email.set_content(content)
# print(email)

email = Email()

protocol = 'IM'
sender = IMSender('qmal', protocol)
receiver = IMReceiver('james', protocol)

email.set_sender(sender)
email.set_receiver(receiver)
content = MyContent('Hello, there!')
email.set_content(content)
print(email)
