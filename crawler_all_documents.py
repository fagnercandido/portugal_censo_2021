import re
import requests
import asyncio

BASE_URL = 'https://tabulador.ine.pt/download'

async def download_file(url, destino):
    response = requests.get(url)
    if response.status_code == 200:
        with open(destino, 'wb') as file:
            file.write(response.content)

async def download_with_coroutine():
    tasks = []
    with open('links.html', 'r') as file:
        content = file.read()
    
    pattern = r'\b\w+PT\.XLSX\b'
    matches = re.findall(pattern, content)

    for indicadores in matches:
        tasks.append(asyncio.create_task(download_file(f'{BASE_URL}/{indicadores}', f'/sources/portugal_censo_2021/indicadores_pt/{indicadores}')))
        await asyncio.gather(*tasks)
        

def main():
    asyncio.run(download_with_coroutine())

if __name__ == '__main__':
    main()


