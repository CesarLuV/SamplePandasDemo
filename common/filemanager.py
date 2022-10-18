'''Main file for reading CSV files.'''

import pandas as pd
from os import getcwd as pwd
from typing import List

from common.constants import COUNTRIES
from common.utils import is_valid_range


def read_file(file_name: str = COUNTRIES) -> pd.DataFrame:
    data_frame = pd.read_csv(pwd() + file_name)
    return data_frame


def get_n_first_elements(data_frame: pd.DataFrame,
                         first_n_elements: int = 13) -> pd.DataFrame:
    return data_frame.head(first_n_elements)


def get_n_last_elements(data_frame: pd.DataFrame,
                        last_n_elements: int = 13) -> pd.DataFrame:
    return data_frame.tail(last_n_elements)


def get_file_headers(data_frame: pd.DataFrame) -> List[str]:
    return list(data_frame.columns)


def get_column_content(column_names: List[str], start: int = 0,
                       end: int = -1,
                       data_frame: pd.DataFrame = None) -> pd.Series:
    if is_valid_range(start=start, end=end, length=len(data_frame)):
        if end < 0:
            return data_frame[column_names][start:]
        return data_frame[column_names][start:end]
    # Default response for invalid ranges
    return None


def get_element_by_index(start: int = 0, end: int = -1,
                         data_frame: pd.DataFrame = None):
    if is_valid_range(start=start, end=end, length=len(data_frame)):
        if end < 0:
            return data_frame.iloc[start:]
        return data_frame.iloc[start:end]
    return None


def get_specific_fields_by_position(indexes_list: List[List[int]],
                                    data_frame: pd.DataFrame) -> str:
    res = ','.join(data_frame.iloc[elem[0], elem[1]] for elem in indexes_list)
    return res


def get_rows_by_column_name(col_name: List[str], data_frame: pd.DataFrame):
    res = [[index, [str(row[elem]) for elem in col_name]]
           for index, row in data_frame.iterrows()]
    return res


def get_rows_specific_content_by_column(col_name: str, field_content: str,
                                        data_frame: pd.DataFrame):
    res = data_frame.loc[data_frame[col_name] == field_content]
    return res


def sort_data_frame_by_column_name(col_name: List[str],
                                   data_frame: pd.DataFrame,
                                   ascending: bool = True):
    return data_frame.sort_values(col_name, ascending=ascending)


if __name__ == '__main__':
    data_frame = read_file()
    print(get_n_first_elements(data_frame, 3))
    print(get_n_last_elements(data_frame, 3))
    print(get_file_headers(data_frame))
    print(get_column_content(column_names=['country', 'beautiful thing'],
                             start=90, end=100, data_frame=data_frame))
    print(get_element_by_index(start=0, end=1, data_frame=data_frame))
    print(get_specific_fields_by_position([[2, 0], [2, 1], [2, 2]],
                                          data_frame))
    print(get_rows_by_column_name(['country', 'category'], data_frame))
    print(get_rows_specific_content_by_column('category', 'SKILLZ',
                                              data_frame))
    print(sort_data_frame_by_column_name(['country'], data_frame, False))
