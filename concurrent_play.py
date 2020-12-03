import concurrent.futures
import time

start=time.perf_counter()


def func(seconds):
    print(f'ZZzzzz Sleepy,for {seconds}s')
    time.sleep(seconds)
    #print(f'ran for {seconds}')
    return "Woke up"

with concurrent.futures.ThreadPoolExecutor() as executor:
    s=[5,4,3,2,1]
    results=executor.map(func,s)

    for r in results:
        print(r)
    ##lis=[executor.submit(func,sec) for sec in s]
    '''for f in concurrent.futures.as_completed(lis):
        print(f.result())'''


finish=time.perf_counter()

print(f'time taken: {round(finish-start,2)} seconds')
