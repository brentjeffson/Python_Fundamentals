import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} Second(s)...")
    time.sleep(seconds)
    return f"({seconds})Done Sleeping..."


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [1, 5, 4, 3, 2, 1]
    results = [executor.submit(do_something, sec) for sec in secs]  # this is called list comprehension

    # if an exception occurs inside the function, it will only be
    # raised when it's value is retrieved from the results iterator.
    # https://youtu.be/IEEhzQoKtQU

    # returns result as they finish
    for f in concurrent.futures.as_completed(results):
        print(f.result())

    # returns result as in the order that they were started
    results = executor.map(do_something, secs)
    for r in results:
        print(r)

    # f1 = executor.submit(do_something, 2)
    # f2 = executor.submit(do_something, 2)
    # print(f1.result())  # wait until function completes
    # print(f2.result())  # wait until function completes
    # print("Done.")  # will not get executed until the above code is done waiting

end = time.perf_counter()
print(f"Finished in {round(end-start, 2)} seconds")