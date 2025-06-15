import time

def task(name):
    print(f'{name} 시작')
    time.sleep(1)
    print(f'{name} 완료')

def main():
    start = time.time()

    task('작업 1')
    task('작업 2')
    task('작업 3')

    end = time.time()
    print(f'총 소요 시간: {end - start:.2f}초')

main()
