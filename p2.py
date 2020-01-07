
allowed_operators = {'+','-','/','%'}

def binary_operations():
     with open("input2.txt", "r") as fin:
        x=fin.readlines()
        operator = x[0].strip('\n')
        a=int(x[1].strip('\n'),2)
        b=int(x[2].strip('\n'),2)
        if operator not in allowed_operators:
            print('operacao invalida')
        elif a>=256 or b>=256 or 0>a or 0>b:
              print('valores invalidos')
        else:
            op = eval(str(a)+operator+str(b))
            print(bin(op)[2:].zfill(8))
        fin.close()
if __name__ == "__main__":
    binary_operations()