def main() -> None:
    try:
        with open("input.txt", "r", encoding="utf-8") as fin:
            s = fin.read().strip()
    except OSError:
        return

    if not s:
        return

    n = len(s)
    z = [0] * n
    l = r = 0

    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1

    try:
        with open("output.txt", "w", encoding="utf-8") as fout:
            if n > 1:
                fout.write(" ".join(str(z[i]) for i in range(1, n)))
            fout.write("\n")
    except OSError:
        return


if __name__ == "__main__":
    main()

