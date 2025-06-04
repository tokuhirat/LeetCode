import sys
import time
from dataclasses import dataclass

TEST_NUM = 1_000_000


@dataclass
class LinkEntryDataclass:
    prev: "LinkEntryDataclass"
    next: "LinkEntryDataclass"
    key: tuple[int, int] | None
    result: int | None


start = time.perf_counter()
keep = []
for _ in range(TEST_NUM):
    root_dataclass = LinkEntryDataclass(None, None, None, None)
    root_dataclass = LinkEntryDataclass(
        prev=root_dataclass, next=root_dataclass, key=None, result=None
    )
    keep.append(root_dataclass)
end = time.perf_counter()

print(end - start)
print(sys.getsizeof(root_dataclass))
time.sleep(30)

# 239408 kB
