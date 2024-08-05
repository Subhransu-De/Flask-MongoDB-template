from abc import ABC, abstractmethod


class BaseRepository(ABC):
    def __init__(self, database):
        self.db = database

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def find_by_id(self, identifier):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def update(self, identifier, data):
        pass

    @abstractmethod
    def delete(self, identifier):
        pass
