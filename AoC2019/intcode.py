
class intcode:
    def __init__(self, progIn):
        self.program = self.parse_program(progIn)
        memoryPad = [0] * 999999
        self.program += memoryPad
        self.curIdx = 0 # initialize at 0, pointer to current instruction
                        # I'm hoping this will allow the program to start backup
                        # after it pauses waiting for input
        self.stateFlag = 0
        #
        # stateFlag     = 0: Normal operating mode
        #               = 1: Waiting on input.  update self.curInput and run prog_continue()
        #               = 99: Program complete.  HALTED
        self.curInput = [] # Placeholder for current input
        self.curRecall = [] # Placeholder for current recall value
        self.curBase = 0 # current relevant base
        self.debug = False #Debug Mode Flag
        self.step = 0 # Current step
        
    def execute(self, input1=False, input2=False, debug = False):
        self.debug = debug
        if input1:
            self.program[1] = input1
        if input2:
            self.program[2] = input2
        while True:
            _,_,_,curOpcode = self.parse_opcode(self.program[self.curIdx])
            if curOpcode == 99:
                self.stateFlag = 99
                break
            elif curOpcode == 1:
                newIdx = self.op_add(self.curIdx)
            elif curOpcode == 2:
                newIdx = self.op_mult(self.curIdx)
            elif curOpcode == 3:
                # Save mode. First query value
                if self.curInput == []: #input empty, wait for input
                    self.pause_for_input()
                    break
                else:
                    newIdx = self.op_save(self.curIdx)
                    self.stateFlag = 0
                    self.curInput = []
            elif curOpcode == 4:
                newIdx = self.op_recall(self.curIdx)
            elif curOpcode == 5:
                newIdx = self.op_jump_if_true(self.curIdx)
            elif curOpcode == 6:
                newIdx = self.op_jump_if_false(self.curIdx)
            elif curOpcode == 7:
                newIdx = self.op_less_than(self.curIdx)
            elif curOpcode == 8:
                newIdx = self.op_equal(self.curIdx)
            elif curOpcode == 9:
                newIdx = self.op_adjust_base(self.curIdx)
            else:
                print("you broke something, dumbass. Not a valid mode"+str(curOpcode))
            if self.debug:
                print("Completed Step # "+str(self.step))
                print("Instructions: "+str(self.program[self.curIdx:self.curIdx+4]))
            self.curIdx = newIdx
            self.step += 1
            if self.debug:
                break
 
    
    def parse_program(self, progIn):
        """ Converts string input of program to a list of numbers
        """
        b = [int(i) for i in progIn.split(',')]
        return b
        
        
    def parse_opcode(self, incode):
        A,B,C,D,E = [int(x) for x in str("{:05d}".format(incode))]
        DE = (D*10) + E
        return [A,B,C,DE]

    def op_add(self,idx):
        modeD,modeC,modeB,opcode = self.parse_opcode(self.program[idx])
        valueB = self.get_value(modeB,idx+1)
        valueC = self.get_value(modeC,idx+2)
        if modeD == 0:
            modeD = 1
        valueD = self.get_value(modeD,idx+3)
        self.program[valueD] = valueB + valueC
        jumpsToNext = 4 # This opcode uses four positions in program
        if self.debug:
            print("Program: "+str(self.program[idx:idx+4])+" at index: "+str(self.curIdx))
            print("ModeB: "+str(modeB)+" ModeC: "+str(modeC) + " ModeD: "+str(modeD))
            print("valueB: "+str(valueB)+" valueC: "+str(valueC)+ " valueD: "+str(valueD))
            print("Sum: "+str(valueB + valueC)+" should be: "+str(self.program[valueD]))
        return idx + jumpsToNext
        
    def op_mult(self,idx):
        modeD,modeC,modeB,opcode = self.parse_opcode(self.program[idx])
        valueB = self.get_value(modeB,idx+1)
        valueC = self.get_value(modeC,idx+2)

        if modeD == 0:
            modeD = 1
        valueD = self.get_value(modeD,idx+3)

        # Store product in the location indiciated by program[D]
        self.program[self.program[idx+3]] = valueB * valueC
        
        jumpsToNext = 4 # This opcode uses four positions in program
        if self.debug:
            print("Program: "+str(self.program[idx:idx+4])+" at index: "+str(self.curIdx))
            print("ModeB: "+str(modeB)+" ModeC: "+str(modeC) + " ModeD: "+str(modeD))
            print("valueB: "+str(valueB)+" valueC: "+str(valueC)+ " valueD: "+str(valueD))
            print("Product: "+str(valueB * valueC)+" should be: "+str(self.program[valueD]))
        return idx + jumpsToNext

   
    def op_save(self, idx):
        in_value = self.curInput        
        _,_,modeB,opcode = self.parse_opcode(self.program[idx])
        if modeB == 0:
            address = self.program[idx+1]
        elif modeB == 2:
            a = self.program[idx+1]
            address = self.curBase + a
        self.program[address] = in_value
        jumpsToNext = 2 # This opcode uses two positions in program
        return idx + jumpsToNext

    def pause_for_input(self):
        # Flags code as waiting for input
        # when input entered, will call op_save
        self.stateFlag = 1 # Waiting on input
        

    def op_recall(self, idx):        
        _,_,modeB,opcode = self.parse_opcode(self.program[idx])
        valB = self.get_value(modeB,idx+1)
        if modeB == 2:
            self.curRecall = self.program[valB]
        else:
            self.curRecall = valB
        print("Recall Value: "+str(self.curRecall))
        jumpsToNext = 2 #uses two positions in program
        return idx + jumpsToNext

    def op_jump_if_true(self,idx):
        _,modeC,modeB,opcode = self.parse_opcode(self.program[idx])

        valB = self.get_value(modeB,idx+1)
        valC = self.get_value(modeC,idx+2)
        if valB != 0:
            return valC 
        else:
            return idx+3 

    def op_jump_if_false(self,idx):
        _,modeC,modeB,opcode = self.parse_opcode(self.program[idx])
        valB = self.get_value(modeB, idx+1)
        valC = self.get_value(modeC, idx+2)
        if valB == 0:
            return valC 
        else:
            return idx+3 

    def op_less_than(self,idx):
        _,modeC,modeB,opcode = self.parse_opcode(self.program[idx])        
        valB = self.get_value(modeB, idx+1)
        valC = self.get_value(modeC, idx+2)
        valD = self.program[idx+3] 
        if self.debug:
            print("Program: "+str(self.program[idx:idx+4])+" at index: "+str(self.curIdx))
            print("ModeB: "+str(modeB)+" ModeC: "+str(modeC))
            print("valueB: "+str(valB)+" valueC: "+str(valC))
        if valB < valC:
            self.program[valD] = 1
        else:
            self.program[valD] = 0
        
        return idx + 4

    def op_equal(self,idx):

        _,modeC,modeB,opcode = self.parse_opcode(self.program[idx])
        valB = self.get_value(modeB, idx+1)
        valC = self.get_value(modeC, idx+2)            
        valD = self.program[idx+3] 
        if valB == valC:
            self.program[valD] = 1
        else:
            self.program[valD] = 0 
        
        return idx + 4
    
    def op_adjust_base(self,idx):
        _,_,modeB,opcode = self.parse_opcode(self.program[idx])
        valB = self.get_value(modeB, idx+1)
        if modeB == 2:
            a = self.program[idx+1]
            self.curBase += self.program[self.curBase + a]
        if self.debug:
            print("Program: "+str(self.program[idx:idx+2])+" at index: "+str(self.curIdx))
            print("ModeB: "+str(modeB))
            print("Current Base: "+str(self.curBase))
            print("Program at target: "+str(self.program[self.program[idx+1]]))
            print("valB: "+str(modeB))
        self.curBase += valB
        if self.debug:
            print("new base: "+str(self.curBase))  
            print("\n")
              
        return idx+2
    
    def get_value(self,mode,idx):
        if mode == 0:
            value = self.program[self.program[idx]]
        elif mode == 1:
            value = self.program[idx]
        elif mode == 2:
            a = self.program[idx]
            value = self.curBase + a
        return value
  
