import sys
import time
from typing import TypedDict

TEST_NUM = 1_000_000


class LinkEntry(TypedDict):
    prev: "LinkEntry"
    next: "LinkEntry"
    key: tuple[int, int] | None
    result: int | None


start = time.perf_counter()
keep = []
for _ in range(TEST_NUM):
    root_typedict = LinkEntry()
    root_typedict = LinkEntry(
        prev=root_typedict, next=root_typedict, key=None, result=None
    )
    keep.append(root_typedict)
end = time.perf_counter()

print(end - start)
print(sys.getsizeof(root_typedict))
time.sleep(30)

# RSS: 270160 kB
