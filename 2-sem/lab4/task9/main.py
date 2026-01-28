from math import inf


def digits_count(x: int) -> int:
    cnt = 0
    while x > 0:
        cnt += 1
        x //= 10
    return max(cnt, 1)


def main() -> None:
    try:
        with open("input.txt", "r", encoding="utf-8") as fin:
            s = fin.read().strip()
    except OSError:
        return

    if not s:
        return

    n = len(s)
    dp = [inf] * (n + 1)
    prev_pos = [-1] * (n + 1)
    seg_start = [-1] * (n + 1)
    seg_len = [0] * (n + 1)
    seg_rep = [1] * (n + 1)

    dp[0] = 0

    # For each starting position j, compute prefix-function on suffix s[j:]
    for j in range(n):
        m = n - j
        pi = [0] * m
        for i in range(1, m):
            k = pi[i - 1]
            while k > 0 and s[j + i] != s[j + k]:
                k = pi[k - 1]
            if s[j + i] == s[j + k]:
                k += 1
            pi[i] = k

        for L in range(1, m + 1):
            total_len = L
            p = total_len - pi[total_len - 1]
            reps = 1
            if total_len % p == 0:
                reps = total_len // p
            else:
                p = total_len
                reps = 1

            if reps == 1:
                cost_segment = total_len
            else:
                cost_segment = p + 1 + digits_count(reps)  # pattern*reps

            i = j + L
            add_plus = 1 if j > 0 else 0
            cand = dp[j] + cost_segment + add_plus
            if cand < dp[i]:
                dp[i] = cand
                prev_pos[i] = j
                seg_start[i] = j
                seg_len[i] = p
                seg_rep[i] = reps

    # Reconstruct answer
    parts = []
    cur = n
    while cur > 0:
        j = prev_pos[cur]
        st = seg_start[cur]
        base_len = seg_len[cur]
        reps = seg_rep[cur]
        base = s[st : st + base_len]
        if reps == 1:
            piece = base
        else:
            piece = f"{base}*{reps}"
        parts.append(piece)
        cur = j

    parts.reverse()

    try:
        with open("output.txt", "w", encoding="utf-8") as fout:
            fout.write("+".join(parts) + "\n")
    except OSError:
        return


if __name__ == "__main__":
    main()

