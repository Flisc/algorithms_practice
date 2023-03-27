from typing import Final

data = {"key": True}
data2 = {'key2': ['value1', 'val2', ['val3', 'asd', 100, 'asd', 100, True, data]]}
print(data2)

match data:
    case {'key': float() as f}:
        print('first case')
    case _:
        print('default')
