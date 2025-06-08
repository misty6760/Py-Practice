# 기존 방식
from typing import Union, Optional
def process_data1(value: Union[int, str], optional_param: Optional[int] = None) -> Union[float, str]:
    pass

# 새로운 방식
def process_data2(value: int | str, optional_param: int | None = None) -> float | str:
    pass

# isinstance와 issubclass에서도 사용 가능
isinstance(5, int | str)        # True
issubclass(bool, int | float)   # True

# None과의 조합
isinstance(None, int | None)    # True
isinstance(42, None | int)      # True