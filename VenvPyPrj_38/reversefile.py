# Задание 3.4.7
# Выполните реверсирование строк файла (перестановка строк файла в обратном порядке)
import io, os

class ReverseFile(io.IOBase):
    def __init__ (self, filename, headers=1):
        self.fp = open(filename, 'r', encoding='utf8')
        self.headers = headers
        self.reverse = self.reversed_lines()
        self.end_position = -1
        self.current_position = -1

    def readline(self, size=-1):
        if self.headers > 0:
            self.headers -= 1
            raw = self.fp.readline(size)
            self.end_position = self.fp.tell()
            return raw

        raw = next(self.reverse)
        if self.current_position > self.end_position:
            return raw

        raise StopIteration

    def reversed_lines(self):
        # Generate the lines of file in reverse order.
        part = ''
        for block in self.reversed_blocks():
            block = block + part
            block = block.split('\n')
            block.reverse()
            part = block.pop()
            if block[0] == '':
                block.pop(0)

            for line in block:
                yield line + '\n'

        if part:
            yield part

    def reversed_blocks(self, blocksize=0xFFFF):
        # "Generate blocks of file's contents in reverse order."
        file = self.fp
        file.seek(0, os.SEEK_END)
        here = file.tell()
        while 0 < here:
            delta = min(blocksize, here)
            here -= delta
            file.seek(here, os.SEEK_SET)
            self.current_position = file.tell()
            yield file.read(delta)

rev = ReverseFile("..\\input.txt")
print(rev.reversed_lines)
for line in rev.reversed_lines():
    print(f'{line.strip()}')