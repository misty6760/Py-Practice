# 함수 호출 시 언패킹
def add(i,j,k):
    return i + j + k

args=[1,2,3]
print(f"function_call_unpacking_1: {add(*args)}")       # 출력 6

kwargs = {'i':4,'j':5,'k':6}
print(f"function_call_unpacking_2: {add(**kwargs)}")    # 출력 15