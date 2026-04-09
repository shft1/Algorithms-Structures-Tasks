import sys


def main():
    n_line = sys.stdin.readline().rstrip()
    while n_line == "":
        n_line = sys.stdin.readline().rstrip()
    n = int(n_line)

    correct_answers = sys.stdin.readline().rstrip()
    while correct_answers == "":
        correct_answers = sys.stdin.readline().rstrip()

    m_line = sys.stdin.readline().rstrip()
    while m_line == "":
        m_line = sys.stdin.readline().rstrip()
    m = int(m_line)

    works = []
    for _ in range(m):
        work = sys.stdin.readline().rstrip()
        while work == "":
            work = sys.stdin.readline().rstrip()
        works.append(work)

    correct_counts = []
    wrong_counts = []

    for work in works:
        correct = sum(work[i] == correct_answers[i] for i in range(n))
        correct_counts.append(correct)
        wrong_counts.append(n - correct)

    similar_pairs = []

    for i in range(m):
        for j in range(i + 1, m):
            same_correct = 0
            same_wrong = 0

            for k in range(n):
                if works[i][k] != works[j][k]:
                    continue

                if works[i][k] == correct_answers[k]:
                    same_correct += 1
                else:
                    same_wrong += 1

            if (
                2 * same_correct > correct_counts[i]
                and 2 * same_correct > correct_counts[j]
                and 2 * same_wrong > wrong_counts[i]
                and 2 * same_wrong > wrong_counts[j]
            ):
                similar_pairs.append((i + 1, j + 1))

    print(len(similar_pairs))
    for first, second in similar_pairs:
        print(first, second)


if __name__ == "__main__":
    main()
