import threading
import time

def sleep_sort(arr):
    result = []

    def add_number(num):
        time.sleep(num * 0.1)
        result.append(num)

    threads = []

    for num in arr:
        t = threading.Thread(target=add_number, args=(num,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return result

print(sleep_sort([4, 2, 1, 3]))