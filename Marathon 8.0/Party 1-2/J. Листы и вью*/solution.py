import sys


class Figon:
    lists: dict[str, tuple[int, list[int]]] = {}

    @classmethod
    def create_list(cls, variable: str, elements: list[int]) -> None:
        cls.lists[variable] = (0, elements)

    @classmethod
    def create_sublist(
        cls, var_parent: str, var_child: str, start: int
    ) -> None:
        shift: int = start - 1
        parent_shift, link = cls.lists[var_parent]
        cls.lists[var_child] = (parent_shift + shift, link)

    @classmethod
    def add(cls, var_class: str, x: int) -> None:
        cls.lists[var_class][1].append(x)

    @classmethod
    def get(cls, var_class: str, pos: int) -> str:
        src_shift, link = cls.lists[var_class]
        index: int = src_shift + pos - 1
        sys.stdout.write(f"{link[index]}\n")

    @classmethod
    def set(cls, var_class: str, pos: int, x: int) -> None:
        src_shift, link = cls.lists[var_class]
        index: int = src_shift + pos - 1
        link[index] = x


def solution(n):
    for _ in range(n):
        cmd: str = sys.stdin.readline().rstrip()
        if cmd.startswith("List"):
            left, right = cmd.split(" = ")
            variable = left[5:]
            if right.startswith("new "):
                elements: list[int] = list(map(int, right[9:-1].split(",")))
                Figon.create_list(variable, elements)
            else:
                var_parent, func = right.split(".")
                start, _ = map(int, func[8:-1].split(","))
                Figon.create_sublist(var_parent, variable, start)
        else:
            variable, right = cmd.split(".")
            if right.startswith("set"):
                pos, x = map(int, right[4:-1].split(","))
                Figon.set(variable, pos, x)
            elif right.startswith("add"):
                x: int = int(right[4:-1])
                Figon.add(variable, x)
            elif right.startswith("get"):
                pos: int = int(right[4:-1])
                Figon.get(variable, pos)


def main():
    n = int(sys.stdin.readline().rstrip())
    solution(n)


if __name__ == "__main__":
    main()
