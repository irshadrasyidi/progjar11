import socket
import select
import queue
from threading import Thread
from time import sleep
from random import randint
import sys


class ProcessThread(Thread):
    def __init__(self):
        super(ProcessThread, self).__init__()
        self.running = True
        self.q = queue.Queue()

    def add(self, data):
        self.q.put(data)

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            try:
                # block for 1 second only:
                value = self.q.get(block=True, timeout=1)
                process(value)
            except:
                sys.stdout.write('.')
                sys.stdout.flush()
        #
        if not self.q.empty():
            print("Elements left in the queue:")
            while not self.q.empty():
                print(self.q.get())


t = ProcessThread()
t.start()


def process(value):
    """
    Implement this. Do something useful with the received data.
    """
    print(value)
    sleep(randint(1, 5))  # emulating processing time


def main():
    s = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    print(host)
    port = 50000  # Reserve a port for your service.
    s.bind((host, port))  # Bind to the port
    print("Listening on port {p}...".format(p=port))
    s.listen(5)  # Now wait for client connection.
    while True:
        try:
            client, addr = s.accept()
            ready = select.select([client], [], [], 2)
            if ready[0]:
                data = client.recv(4096)
                process_thread = ProcessThread()
                process_thread.start()
                process_thread.add(str(data))

        except KeyboardInterrupt:
            print("Stop.")
            break

        except socket.error as msg:
            print("Socket error! %s" % msg)
            break
    #
    cleanup()


def cleanup():
    t.stop()
    t.join()


#########################################################
if __name__ == "__main__":
    main()
