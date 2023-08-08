from subprocess import Popen, STDOUT, PIPE
from threading import Thread


class ProcessOutputThread(Thread):
    def __init__(self, proc):
        Thread.__init__(self)
        self.proc = proc

    def run(self):
        while not self.proc.stdout.closed:
            print(self.proc.stdout.readline().decode().rstrip())


p = Popen(['bc', '-i'], stdout=PIPE, stderr=STDOUT, shell=True)
output = ProcessOutputThread(p)
output.start()

while not p.stdout.closed:
    query = input()
    if query == "quit" or query == "exit":
        p.communicate(query.encode(), timeout=1)
        if p.poll() is not None:
            break
    query = query + '\n'
    p.stdin.write(query.encode())
    p.stdin.flush()
