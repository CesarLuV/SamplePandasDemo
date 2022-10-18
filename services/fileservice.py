'''Service layer for Pandas process.'''

from typing import List

from common.filemanager import read_file as rf
from common.filemanager import get_file_headers as fh


class FileService():
    def __init__(self, filename: str = None) -> None:
        self.__data_frame = rf(filename) if filename else rf()

    def get_column_names(self) -> List[str]:
        return fh(self.__data_frame)
