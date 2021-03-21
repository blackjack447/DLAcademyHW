# «Есть два писателя, которые по очереди в течении определенного времени (у каждого разное) пишут в одну книгу.
# Данная книга очень популярна, у неё есть как минимум 3 фаната (читателя), которые ждут не дождутся, чтобы прочитать
# новые записи из неё. Каждый читатель и писатель – отдельный поток. Одновременно книгу может читать несколько
# читателей, но писать единовременно может только один писатель.»

import time
from threading import Thread, Event

event = Event()
variable = ""


def writter_one():
   event.set()
   global variable
   variable += "cтроки первого писателя, "
   print("Первый писатель пишет что то в книгу")
   time.sleep(2)


def writter_two():
    event.set()
    global variable
    variable += "cтроки второго писателя"
    print("Второй писатель пишет что то в книгу")
    time.sleep(4)


def readers(thread_id):
   while True:
       event.wait()
       print(f'{thread_id} фанат прочитал {variable}')


if __name__ == '__main__':
    writter_one()
    writter_two()
    threads_1 = (Thread(target=writter_one))
    threads_2 = (Thread(target=writter_two))
    threads_3 = (Thread(target=readers, args=(thread_id,))
                 for thread_id in range(1, 4))

    for t in threads_3:
        t.start()
    event.clear()
