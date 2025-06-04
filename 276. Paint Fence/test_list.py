import sys
import time

TEST_NUM = 1_000_000

start = time.perf_counter()
keep = []
for _ in range(TEST_NUM):
    root_list = []
    root_list[:] = [root_list, root_list, None, None]
    keep.append(root_list)
end = time.perf_counter()

print(end - start)
print(sys.getsizeof(root_list))
time.sleep(30)

# RSS: 149456 kB
