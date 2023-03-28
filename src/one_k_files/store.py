import os


class Store:
    def save(self, file_path: str, content: bytes):
        pass

    def find_all(self, source: str):
        pass


class GroupedFileStore(Store):
    def save(self, file_path: str, content: bytes):
        self._create_destination(os.path.dirname(file_path))
        self._write_file(file_path, content)

    def find_all(self, source: str):
        with os.scandir(source) as entries:
            for entry in entries:
                yield (entry, self._read_file(entry.path))

    def _create_destination(self, destination_directory: str):
        if not os.path.isdir(destination_directory):
            os.makedirs(destination_directory)

    def _read_file(self, file_path: str):
        with open(file_path, "rb") as file:
            return file.read()

    def _write_file(self, file_path: str, file_bytes):
        with open(file_path, "wb") as file:
            file.write(file_bytes)
