```text
Description:
С сервером происходит что-то странное. У нас есть файл с логами, посмотрите его.
```
## Анализ

Каждая строка в файле URL-кодирована. После декодирования один из запросов выглядит примерно так:

```http
GET /wow/?id=1' AND ORD(MID((SELECT IFNULL(CAST(`flag` AS NCHAR),0x20)
FROM `security`.ws ORDER BY `flag` LIMIT 0,1),1,1))>64
AND 'Dbpi'='Dbpi' HTTP/1.1
```

Это boolean-based blind SQL injection. В запросе:

- `SELECT ... flag ... FROM security.ws` получает значение столбца `flag`;
- `MID(..., position, 1)` выбирает один символ на заданной позиции;
- `ORD(...)` переводит символ в ASCII-код;
- сравнение `> threshold` проверяет, больше ли код очередного порога.

Для каждого символа `sqlmap` меняет `threshold`, выполняя бинарный поиск. Например, для первой позиции встречается последовательность:

```text
64, 96, 112, 120, 116, 118, 119
```

Она сходится к ASCII-коду `119`, то есть к символу `w`. Для второй позиции поиск заканчивается на `115` (`s`), а для третьей — на `123` (`{`). Уже первые три символа подтверждают формат `ws{...}`.

## Автоматическое извлечение

Из каждой строки достаточно получить номер позиции и порог, а затем взять последний порог для каждой позиции. Последняя, 23-я позиция относится уже к проверке завершения строки, поэтому в результат берутся позиции 1–22.

```python
import re
from collections import defaultdict
from urllib.parse import unquote

values = defaultdict(list)

with open("logs.txt", encoding="ascii") as f:
    for line in f:
        decoded = unquote(line)
        match = re.search(
            r"MID\(\(SELECT.*?\),(\d+),1\)\)>\s*(\d+)",
            decoded,
        )
        if match:
            position, threshold = map(int, match.groups())
            values[position].append(threshold)

flag = "".join(chr(values[position][-1]) for position in range(1, 23))
print(flag)
```
## Flag

```text
ws{H0w_y0u_r3@d_th1s?}
```
