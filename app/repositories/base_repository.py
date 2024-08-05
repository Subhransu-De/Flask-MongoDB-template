from abc import ABC, abstractmethod


class BaseRepository(ABC):
    def __init__(self, database):
        self.db = database

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def update(self, id, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass
