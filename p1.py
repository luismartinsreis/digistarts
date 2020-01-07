

def unique():
    with open("input1.txt", "r") as fin:
        y=set(fin.readlines()[1:])
        unique_set = sorted(set(map(int, y)))
        [print(k) for k in unique_set if -1000<= k <=10000]

        fin.seek(0)
        n=int(fin.readline())
        if 1 <= n <=1000:
            pass
        else:
            print('número {} fora da faixa permitida: 1 <= n <=1000'.format(n))
        fin.close()

if __name__ == "__main__":
    unique()