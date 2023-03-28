import re
import os


class ExportPathResolver:
    def resolve(self, name: str):
        pass


class ByLanguageDirResolver(ExportPathResolver):
    def _build_dest_dir(self, name: str):
        search = re.search(r"(\w+)-(\d{1,3}\.txt)", name)
        groups = search.groups()
        return os.path.join(groups[0], groups[1])

    def resolve(self, name: str):
        return self._build_dest_dir(name)
