class LCG:
    def __init__(self):
        self.oldseed=1000
        self.mask=(1<<64) -1
        self.multiplier=25214903917
        self.addend=11
        self.required_bits=32
        sum_bits=""
        zero_str="0"
        for i in range(5):
            result=self.next(self.required_bits)
            print(result)
            text_bits='{0:b}'.format(result)
            while(len(text_bits)< self.required_bits):
                text_bits=zero_str+text_bits
            sum_bits+=text_bits
        print(sum_bits)
    def next(self,bits):
        self.nextseed=(self.oldseed*self.multiplier + self.addend)% self.mask
        self.oldseed=self.nextseed
        return self.nextseed >> (64-bits)
LCG()
