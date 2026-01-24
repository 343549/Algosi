import sys


class MinHeap:
    """
    Мин-куча с поддержкой decrease-key через таблицу позиций.
    Элемент хранится как [value, id], где id — номер операции A.
    """

    def __init__(self) -> None:
        self.h: list[list[int]] = []
        self.pos: dict[int, int] = {}  # id -> индекс в куче

    def _swap(self, i: int, j: int) -> None:
        self.h[i], self.h[j] = self.h[j], self.h[i]
        self.pos[self.h[i][1]] = i
        self.pos[self.h[j][1]] = j

    def _less(self, i: int, j: int) -> bool:
        # сравниваем по значению, затем по id
        if self.h[i][0] != self.h[j][0]:
            return self.h[i][0] < self.h[j][0]
        return self.h[i][1] < self.h[j][1]

    def _sift_up(self, i: int) -> None:
        # подъем вверх при уменьшении ключа
        while i > 0:
            p = (i - 1) // 2
            if self._less(i, p):
                self._swap(i, p)
                i = p
            else:
                break

    def _sift_down(self, i: int) -> None:
        # опускание вниз при извлечении минимума
        n = len(self.h)
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            smallest = i

            if l < n and self._less(l, smallest):
                smallest = l
            if r < n and self._less(r, smallest):
                smallest = r

            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    def push(self, value: int, item_id: int) -> None:
        # вставка нового элемента
        self.h.append([value, item_id])
        i = len(self.h) - 1
        self.pos[item_id] = i
        self._sift_up(i)

    def extract_min(self) -> int | None:
        # извлечение минимального; None если пусто
        if not self.h:
            return None
        res_val, res_id = self.h[0]
        last = self.h.pop()
        self.pos.pop(res_id, None)
        if self.h:
            self.h[0] = last
            self.pos[self.h[0][1]] = 0
            self._sift_down(0)
        return res_val

    def decrease_key(self, item_id: int, new_value: int) -> None:
        # уменьшить значение элемента по его id
        i = self.pos[item_id]
        self.h[i][0] = new_value
        self._sift_up(i)


def main() -> None:
    """
    Обрабатывает команды очереди с приоритетами:
    A x — добавить x
    X   — вывести минимум или * если пусто
    D i y — уменьшить элемент, добавленный в строке i+1 входа, до y
    """
    inp = sys.stdin.buffer
    out_lines: list[str] = []

    first = inp.readline()
    if not first:
        return
    q = int(first)

    heap = MinHeap()
    # add_id_by_op_line[k] — id элемента, добавленного операцией A на строке k (1-based для операций)
    add_id_by_op_line: list[int | None] = [None] * (q + 1)
    next_add_id = 1

    for op_line_no in range(1, q + 1):
        line = inp.readline()
        if not line:
            break
        parts = line.split()
        if not parts:
            continue

        op = parts[0].decode()
        if op == "A":
            x = int(parts[1])
            item_id = next_add_id
            next_add_id += 1
            add_id_by_op_line[op_line_no] = item_id
            heap.push(x, item_id)
        elif op == "X":
            v = heap.extract_min()
            out_lines.append("*" if v is None else str(v))
        elif op == "D":
            x = int(parts[1])  # номер строки операции A во входе минус 1 (первая строка — q)
            y = int(parts[2])
            a_op_line = x
            item_id = add_id_by_op_line[a_op_line]
            heap.decrease_key(int(item_id), y)
        else:
            # неизвестная команда — игнорируем
            pass

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()

