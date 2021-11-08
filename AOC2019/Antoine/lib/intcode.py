from collections import defaultdict, deque

class Machine:
  def __init__(self, m):
    self.__mreset = m
    self.__verbose = False
    
    self.boot()


  def input(self, v):
    self.run(v)


  def output(self, destructive: bool = True):

    if not destructive and self.__output_queue:
      return self.__output_queue[0]

    return self.__output_queue.popleft() if self.__output_queue else None


  def dump_output(self, clear: bool = False):

    o = list(self.__output_queue)

    if clear:
      self.__output_queue.clear()

    return o


  def toggle_verbose(self):
    self.__verbose = not self.__verbose


  def get_memory(self):
    return self.memory


  def boot(self):
    self.memory = self.__mreset + [0]*(8 * 1024*8)
    self.pointer = 0
    self.relative_base = 0
    self.len = len(self.__mreset)
    self.__output_queue = deque()
    self.__halt = False
    self.__waiting = False
    self.__initialized = False


  def halted(self):

    return self.__halt


  def waiting(self):
    return self.__waiting


  def has_output(self):
    return len(self.__output_queue) > 0


  def initialized(self):
    return self.__initialized


  def run(self, input = None):

    if input != None:  
        self.__initialized = True

    while self.pointer < self.len:
      n = self.memory[self.pointer]
      op, m = n % 100, [ n // 100 % 10, n // 1000 % 10, n // 10000 % 10 ]

      p, v = self.memory[self.pointer+1:self.pointer+4], [0]*3

      for i in range(3):
        if m[i] == 0 and p[i] < len(self.memory): 
          v[i] = self.memory[p[i]] 
        elif m[i] == 2 and p[i] < len(self.memory): 
          p[i] = self.relative_base + p[i]
          v[i] = self.memory[p[i]] 
        else: 
          v[i] = p[i]
          p[i] = self.pointer + i + 1

      ''' 
      For convenience: pn for positions, vn for values 
      '''
      p1, _, p3 = p
      v1, v2, _ = v


      # 99: end
      if op == 99:
        self.__halt = True
        if self.__verbose: print('END')
        break

      # 1: sum
      elif op == 1:
        r = v1 + v2
        self.memory[p3] = r 
        self.pointer += 4

        if self.__verbose: print('op 1: Sum', v1, v2, 'and save to', p3)

      # 2: multiply
      elif op == 2:
        r = v1 * v2
        self.memory[p3] = r        
        self.pointer += 4

        if self.__verbose: print('op 2: Multiply', v1, v2, 'and save to', p3)

      # 3: save to address
      elif op == 3: 
        if input == None:
          if self.__verbose: print('op 3: Waiting for input...')
          self.__waiting = True
          break # Wait for input...
        else:
          self.__waiting = False

        self.memory[p1] = input 
        if self.__verbose: print('READ:', self.memory[p1], 'Saved in', p1)

        input = None
        
        self.pointer += 2

      # 4: output
      elif op == 4:
        if self.__verbose: print('op 4: OUTPUT', v1)
        self.__output_queue.append(v1)

        self.pointer += 2

      # 5: jump-if-true
      elif op == 5: 
        if self.__verbose: print('op 5: TRUE, jump to', v2)

        if v1 != 0: 
          self.pointer = v2
        else: 
          self.pointer += 3

      # 6: jump-if-false
      elif op == 6: 
        if self.__verbose: print('op 6: FALSE, jump to', v2)

        if v1 == 0: 
          self.pointer = v2
        else: 
          self.pointer += 3

      # 7: less than
      elif op == 7: 
        r = 1 if v1 < v2 else 0
        
        self.memory[p3] = r
        self.pointer += 4

        if self.__verbose: print('op 7: If less than. Value ', r, 'saved in', p3)       

      # 8: equal
      elif op == 8: 
        r = 1 if v1 == v2 else 0
        
        self.memory[p3] = r 
        self.pointer += 4

        if self.__verbose: print('op 8: If equal. Value ', r, 'saved in', p3)

      # 9: set relative base
      elif op == 9: 
        if self.__verbose: print('op 9: Set relative base. Was', self.relative_base, 'now', self.relative_base + v1)

        self.relative_base += v1
        self.pointer += 2

      else: 
        raise ValueError(f'ERRRRR... p: {self.pointer}, op: {op}, v: {self.memory[self.pointer]}')
        # self.__halt = True
        # break