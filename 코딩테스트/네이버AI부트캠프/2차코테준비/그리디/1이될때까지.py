if __name__ == '__main__':
    N , K = map(int,input().split()); cnt =0 

    while True:
        if N == 1:
            break # 종료

        if N % K == 0:
            N = N // K
            cnt +=1
        else:
            N = N - 1
            cnt +=1

    print(cnt)
        