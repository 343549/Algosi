import sys
import heapq


def main() -> None:
    """
    Распределяет задачи по потокам:
    - поддерживаем мин-кучу (готовность, индекс потока);
    - каждый раз берем поток, который освободится раньше всех;
    - печатаем поток и время старта, возвращаем его с обновленным временем.
    """
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])   # число потоков
    m = int(data[1])   # число задач
    times = list(map(int, data[2:2 + m]))

    # Куча по (время_готовности, индекс_потока)
    heap = [(0, i) for i in range(n)]
    heapq.heapify(heap)

    out_lines: list[str] = []
    for t in times:
        free_time, idx = heapq.heappop(heap)      # поток, который освободится раньше всех
        out_lines.append(f"{idx} {free_time}")    # выводим индекс потока и время старта
        heapq.heappush(heap, (free_time + t, idx))  # возвращаем поток с новым временем готовности

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    main()

