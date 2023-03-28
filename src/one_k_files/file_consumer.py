import os
from resolver import ExportPathResolver


class FileConsumer:
    def __init__(self, destination: str, resolver: ExportPathResolver):
        self._destination = destination
        self._resolver = resolver

    def _write_file(self, file_path: str, file_bytes):
        with open(file_path, "wb") as file:
            file.write(file_bytes)

    def consume(self, file_tuple: tuple):
        (entry, content) = file_tuple
        file_subpath = self._resolver.resolve(entry.name)
        file_path = os.path.join(self._destination, file_subpath)
        directory = os.path.dirname(file_path)
        if not os.path.isdir(directory):
            os.makedirs(directory)
        self._write_file(file_path, content)
