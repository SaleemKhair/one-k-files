import os


class FileProducer:
    def __init__(self, source_directory: str):
        self._source_directory = source_directory

    def _generate_entries(self):
        with os.scandir(self._source_directory) as entries:
            for entry in entries:
                yield (entry, self._read_file(entry.path))

    def _read_file(self, file_path: str):
        with open(file_path, "rb") as file:
            return file.read()

    def produce(self):
        return self._generate_entries()
