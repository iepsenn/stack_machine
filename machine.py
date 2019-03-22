class Machine:

    def __init__(self, file_input):
        self.input_file = file_input

    def run(self):
        with open(self.input_file) as f:
            code = f.read().splitlines()

        self.process(code)


    def process(self, code):
        self.stack = []
        for c in code:

            command = str(c).split(' ')
            #print(self.stack)

            if command[0] == "PRINT":
                if len(self.stack) > 0:
                    print(self.stack[-1])
                else:
                    print("erro de compilação\n")
                    return


            if len(command) == 2:
                command[1] = int(command[1])
            elif len(command) > 2:
                print("erro de compilação\ncomando inválido")


            if command[0] == 'MULT':
                if len(self.stack) >= 2:
                    a = self.stack[-2]
                    b = self.stack[-1]
                    c = a*b

                    del self.stack[-2:]
                    self.stack.append(c)
                else:
                    print("erro de compilação\n")
                    return

            elif command[0] == "ADD":
                if len(self.stack) >= 2:
                    a = self.stack[-2]
                    b = self.stack[-1]
                    c = a+b

                    del self.stack[-2:]
                    self.stack.append(c)
                else:
                    print("erro de compilação\n")
                    return

            elif command[0] == "SUB":
                if len(self.stack) >= 2:
                    a = self.stack[-2]
                    b = self.stack[-1]
                    c = a-b

                    del self.stack[-2:]
                    self.stack.append(c)
                else:
                    print("erro de compilação\n")
                    return

            elif command[0] == "DIV":
                if len(self.stack) >= 2:
                    a = self.stack[-2]
                    b = self.stack[-1]
                    c = a/b

                    del self.stack[-2:]
                    self.stack.append(c)
                else:
                    print("erro de compilação\n")
                    return

            elif command[0] == "PUSH":
                if len(command) == 2:
                    self.stack.append( command[1])
                else:
                    print("erro de compilação\n")
                    return
