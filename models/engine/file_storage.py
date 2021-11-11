#!/usr/bin/python3

class FileStorage:
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        for key, value in self.__file_path:
            if key ==



