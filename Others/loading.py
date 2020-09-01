import time
if __name__ == '__main__':

    seq = ['-', '|', '/', '\\']
    c = 0
    for n in range(100):
        print(f"[{(' '*100).replace(' ', '*', n+1)}]{seq[c]}", end="\r")
        time.sleep(0.05)
        c += -4 if c >= 3 else 1
    print("\n")


    for key, val in enumerate(seq):
        print(f"({key})", end= "\n" if key == len(seq)-1 else "\r")
        time.sleep(1)
        # print(f"{val}")

    for key, val in enumerate(seq):
        print(f"({key})", end= "\r")
        time.sleep(1)

    












