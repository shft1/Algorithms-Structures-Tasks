import sys


def solution(schdl: list):
    schdl.sort(key=lambda x: (float(x[1]), float(x[0])))
    lessons = []
    for time in schdl:
        if not lessons:
            lessons.append(time)
        elif float(time[0]) >= float(lessons[-1][1]):
            lessons.append(time)
    return lessons


def main():
    n = int(sys.stdin.readline().rstrip())
    schedule = [tuple(sys.stdin.readline().rstrip().split()) for _ in range(n)]
    lessons = solution(schedule)
    count = len(lessons)
    sys.stdout.write(f"{count}\n")
    sys.stdout.write("\n".join(map(" ".join, lessons)))


if __name__ == "__main__":
    main()
