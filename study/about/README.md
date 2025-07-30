### pytest テストコード
```bash
# bash
$ pip install pytest
```
```python
from src.module_1 import add_numbers


def test_add_numbers():
    assert add_numbers(1, 2) == 3
```
assert で関数を呼び出し、実行ファイルと同じ階層でpytestを実行する
```bash
#bash
$ pytest
```