def main() -> None:
    try:
        with open("input.txt", "r", encoding="utf-8") as fin:
            data = fin.read().strip().splitlines()
    except OSError:
        return

    if len(data) < 2:
        return

    p = data[0].strip()
    t = data[1].strip()

    positions = []
    n, m = len(t), len(p)

    for i in range(0, n - m + 1):
        ok = True
        for j in range(m):
            if t[i + j] != p[j]:
                ok = False
                break
        if ok:
            positions.append(i + 1)  # 1-based

    try:
        with open("output.txt", "w", encoding="utf-8") as fout:
            fout.write(str(len(positions)) + "\n")
            if positions:
                fout.write(" ".join(map(str, positions)))
            fout.write("\n")
    except OSError:
        return


if __name__ == "__main__":
    main()

