class IntcodeComputer:
    def __init__(self, array, name='IntCode'):
        array.extend([0] * 65000) #comment for d7 memory error
        self.array = array.copy()
        self.trace = False
        self.name = name
        self._input = None
        self.relative = 0
        self.pointer = 0
        self._output = None
        self.instructions = {
            1: self.add,
            2: self.multiply,
            3: self.input,
            4: self.output,
            5: self.jumpTrue,
            6: self.jumpFalse,
            7: self.lessThan,
            8: self.equal,
            9: self.addRel
        }

        self.generator = self.start()
        next(self.generator)

    def send(self, value):
        try:
            self.generator.send(value)
        except StopIteration:
            if self.trace:
                print(f"{self.name}: 'send' hit StopIteration")

    def receive(self):
        try:
            for output in self.generator:
                if output is not None:
                    next(self.generator)
                    return output
        except StopIteration:
            if self.trace:
                print(f"{self.name}: 'send' hit StopIteration")
            return output

    def decoder(self, instruct):
        a = str(instruct)
        b = [int(a[-2:])]
        for d in a[-3::-1]:
            b.append(int(d))
        b.extend([0, 0, 0])
        return b

    def _find_position(self, parm, mode):
        if mode == 0:
            return self.array[self.array[parm]]
        elif mode == 1:
            return self.array[parm]
        elif mode == 2:
            return self.array[self.array[parm] + self.relative]
        else:
            print("Unknown mode, halting.")
            quit()

    def _find_literal_position(self, parm, mode):
        if mode == 0:
            return self.array[parm]
        elif mode == 2:
            return self.array[parm] + self.relative
        else:
            print(f"Wrong input mode: {mode}. Halting.")
            quit()

    def add(self, modes):
        n1 = self._find_position(self.pointer + 1, modes[0])
        n2 = self._find_position(self.pointer + 2, modes[1])
        n3 = self._find_literal_position(self.pointer + 3, modes[2])

        self.array[n3] = n1 + n2
        self.pointer += 4

    def multiply(self, modes):
        n1 = self._find_position(self.pointer + 1, modes[0])
        n2 = self._find_position(self.pointer + 2, modes[1])
        n3 = self._find_literal_position(self.pointer + 3, modes[2])

        self.array[n3] = n1 * n2
        self.pointer += 4

    def input(self, modes):
        position = self._find_literal_position(self.pointer + 1, modes[0])
        self.array[position] = self._input
        self._input = None
        self.pointer += 2

    def output(self, modes=None):
        self._output = self._find_position(self.pointer + 1, modes[0])
        self.pointer += 2

    def jumpTrue(self, modes):
        n1 = self._find_position(self.pointer + 1, modes[0])
        n2 = self._find_position(self.pointer + 2, modes[1])
        if n1 != 0:
            self.pointer = n2
        else:
            self.pointer += 3

    def jumpFalse(self, modes):
        n1 = self._find_position(self.pointer + 1, modes[0])
        n2 = self._find_position(self.pointer + 2, modes[1])
        if n1 == 0:
            self.pointer = n2
        else:
            self.pointer += 3

    def lessThan(self, modes):
        n1 = self._find_position(self.pointer + 1, modes[0])
        n2 = self._find_position(self.pointer + 2, modes[1])
        n3 = self._find_literal_position(self.pointer + 3, modes[2])
        self.array[n3] = 1 if n1 < n2 else 0
        self.pointer += 4

    def equal(self, modes):
        n1 = self._find_position(self.pointer + 1, modes[0])
        n2 = self._find_position(self.pointer + 2, modes[1])
        n3 = self._find_literal_position(self.pointer + 3, modes[2])
        self.array[n3] = 1 if n1 == n2 else 0
        self.pointer += 4

    def addRel(self, modes):
        self.relative += self._find_position(self.pointer + 1, modes[0])
        self.pointer += 2

    def start(self):
        while self.array[self.pointer] != 99:

            if self.trace:
                print(f"{self.name}: processing instruction {self.pointer}")

            input = yield
            if input is not None:
                if self.trace:
                    print(f"{self.name}: received {input}")
                self._input = input

            modes = self.decoder(self.array[self.pointer])
            opcode = modes[0]
            modes = modes[1:]

            if opcode in self.instructions:
                if self.trace:
                    print(f"{self.name}: opcode: {opcode}, input: {self._input}")

                if opcode == 3 and self._input is None:
                    if self.trace:
                        print("Waiting for input")
                    continue

                self.instructions[opcode](modes)

            if self._output is not None:
                if self.trace:
                    print(f"{self.name}: sent {self._output}")
                yield self._output
                self._output = None


