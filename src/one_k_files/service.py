import os
from resolver import ExportPathResolver
from store import Store


class FileGroupingService:
    def __init__(self, store: Store, resolver: ExportPathResolver):
        self._store = store
        self._resolver = resolver

    def groupFiles(self, output_directory: str, input_directory: str):
        for file_tuple in self._store.find_all(input_directory):
            (entry, content) = file_tuple
            file_subpath = self._resolver.resolve(entry.name)
            file_path = os.path.join(output_directory, file_subpath)
            self._store.save(file_path, content)
