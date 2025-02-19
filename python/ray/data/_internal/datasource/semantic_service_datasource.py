from typing import TYPE_CHECKING, Iterator

from ray.data.block import Block
from ray.data.datasource.file_based_datasource import FileBasedDatasource
from ray.data.semantic_service import SemanticService

if TYPE_CHECKING:
    import pyarrow

class SemanticServiceDatasource(FileBasedDatasource):
    def __init__(
        self,
        host: str = "localhost",
        port: int = 8000,
        **file_based_datasource_kwargs,
    ):
        super().__init__("../TOMBSTONE", **file_based_datasource_kwargs)
        self.backend = SemanticService(host, port)

    def _read_stream(self, _f: "pyarrow.NativeFile", _path: str) -> Iterator[Block]:
        for table in self.backend.retrieve_data_all_mock():
            yield table
