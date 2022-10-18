'''Utilities file.'''


def is_valid_range(start: int = 0, end: int = -1, length: int = 0) -> bool:
    if length < 1:
        return False
    if start >= 0:
        if start < length:
            if end == -1:
                return True
            return start < end and end < length
    return False


if __name__ == '__main__':
    assert is_valid_range(start=0, end=10, length=10) is False
    assert is_valid_range(start=9, length=10) is True
    assert is_valid_range(end=9, length=10) is True
    assert is_valid_range(length=10) is True
    assert is_valid_range(start=0, end=10, length=0) is False
    assert is_valid_range(start=0, end=10) is False
    print('All test cases passed')
