import asyncio

async def task(name):
    print(f'{name} 시작')
    await asyncio.sleep(1)
    print(f'{name} 완료')

async def main():
    start = asyncio.get_event_loop().time()

    await asyncio.gather(
        task('작업 1'),
        task('작업 2'),
        task('작업 3')
    )

    end = asyncio.get_event_loop().time()
    print(f'총 소요 시간: {end - start:.2f}초')

asyncio.run(main())