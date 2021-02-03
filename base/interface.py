from abc import ABCMeta, abstractmethod

class VarificationInterface(metaclass=ABCMeta):
    @abstractmethod
    def send(self):
        pass
