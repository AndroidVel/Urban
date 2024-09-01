import datetime
import multiprocessing as mp
from PIL import Image
from queue import Empty


def resize_image(image_paths, pipe: mp.Pipe, stop_event):
    for image_path in image_paths:
        image = Image.open(image_path)
        image = image.resize((800, 600))
        image.save(image_path)
        pipe.send(image_path)
        print(image_path)
    stop_event.set()

def change_color(pipe: mp.Pipe, stop_event):
    while not stop_event.is_set():
        image_path = pipe.recv()
        image = Image.open(image_path)
        image = image.convert('L')
        image.save(image_path)


if __name__ == '__main__':
    data = []
    con1, con2 = mp.Pipe()
    stop_event = mp.Event()

    for image in range(1, 24):
        data.append(f'/home/user/Pictures/map/{image}.jpg')

    resize_process = mp.Process(target=resize_image, args=(data, con1, stop_event))
    change_process = mp.Process(target=change_color, args=(con2, stop_event))

    start = datetime.datetime.now()
    resize_process.start()
    change_process.start()

    resize_process.join()
    change_process.join()
    end = datetime.datetime.now()
    print()
    print(end - start)
