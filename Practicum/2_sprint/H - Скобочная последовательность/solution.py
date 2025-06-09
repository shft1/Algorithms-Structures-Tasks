import sys


def solution():
    br_seq = sys.stdin.readline().rstrip()
    if not br_seq:
        return "True"

    br_op_stack = []
    br_cl = {"]": "[", "}": "{", ")": "("}

    for br in br_seq:
        if br in br_cl:
            if not br_op_stack or br_op_stack[-1] != br_cl[br]:
                return "False"
            br_op_stack.pop()
        else:
            br_op_stack.append(br)

    return "False" if br_op_stack else "True"


if __name__ == "__main__":
    sys.stdout.write(solution() + "\n")
