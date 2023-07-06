import threading
import time

def tentoone(id):
    print(f'Начало выполнения потока {id}...')
    for i in range(10,0,-1):
        print(f'Поток {id}: {i}')
        time.sleep(1)
    print(f'Поток {id} завершен...')

threads = []
for n in range(1,3):
    t = threading.Thread(target=tentoone, args=(n,))
    threads.append(t)
    t.start()



