import abc


class Command(abc.ABC):
    @abc.abstractmethod
    def build(self, parameter):
        """ Build method should be implemented. """
