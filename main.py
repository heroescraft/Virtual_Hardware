def Or(ports):
	value = 0
	if ports[0] == 1 or ports[1] == 1:
		value = 1
	return value
	
def Not(port):
	return abs(port-1)

def Nor(ports):
	return Not(Or(ports))
	
def And(ports):
	return Not(Or([Not(ports[0]), Not(ports[1])]))

def Xor(ports):
	return abs(ports[0]-ports[1])

def Nand(ports):
	return Not(And(ports))
	
def HalfAdder(ports):
	#result = [value, carry]
	result = []
	result.append(Xor([ports[0], ports[1]]))
	result.append(And([ports[0], ports[1]]))
	return result

def FullAdder(ports):
	#ports = [a, b, carry]
	#result = [value, carry]
	Half = HalfAdder(ports[:2])
	Sum = Xor([Half[0], ports[2]])
	And1 = And([ports[2], Half[0]])
	And2 = And([ports[0],ports[1]])
	Carry = Or([And1, And2])
	return [Sum, Carry]


def BitAdder(bit, numbers):
	#numbers = ['1001', '0001']
	#result = []
	#result.reverse()
	#convert result into string
	#result = '1010'
	result = []
	Half = HalfAdder([int(numbers[1][-1]), int(numbers[0][-1])])
	result.append(Half[0])
	
	tmpresult = [0, Half[1]]
	for b in range(bit-1):
		tmpresult = FullAdder([int(numbers[1][(-b)+2]), int(numbers[0][(-b)+2]), tmpresult[1]])
		result.append(tmpresult[0])
	if tmpresult[1] == 1:
		result.append('1')
	
	result.reverse()
	output = ''
	for num in result:
		output+=str(num)
	return output

def BitReverser(bit, number):
	result = ''
	for b in range(bit):
		result+=str(Not(int(number[b])))
	return result

def BitSubtractor(bit, numbers):
	#numbers[0]-numbers[1]
	return BitReverser(4, BitAdder(4, [BitReverser(4, numbers[0]), numbers[1]]))

def IntToBin(num):
	#Currently, for some reason, only 4 bit adders work.
	if num > 16:
		result = 'Error: This is a 4 bit converter, it is currently not possible for 4> bit.'
	else:
		result = '0000'
		for i in range(num):
			result = BitAdder(4, ['0001', result])
	return result

def BinToInt(num):
	result = 0
	while num != '0000':
		num = BitSubtractor(4, [num, '0001'])
		result+=1
	return result
	

if __name__ == "__main__":
	try:
		Storage = open('script.bin', 'r').read().replace('\n', '').replace(' ', '')
	except:
		with open('script.bin', 'w') as f:
			f.write('0000')
		Storage = '0000'

	Bit = 4
	i = 0
	tmp = ''
	tmpStorage = []
	for value in Storage:
		i+=1
		tmp+=value
		if i == Bit:
			i=0
			tmpStorage.append(tmp)
			tmp=''
	Storage = tmpStorage


	Memory = {'1100':'0000', '1101':'0000', '1110':'0000', '1111':'0000'}

	#w:x:v:0001


	#a:1100
	#b:1101
	#c:1110
	#d:1111


	while True:

		button = input('') #This is used to simulate keyboard presses
		if button == 'e':
			line = 0
			tmpStorage = Storage[:]
			for value in tmpStorage:
				if value == '0000':
					break
				elif value == '0001':
					#write to x with the value v
					Memory[tmpStorage[line+1]] = tmpStorage[line+2]
					del tmpStorage[line+1]
					del tmpStorage[line+1]

				elif value == '0010':
					#insert a variable's value into any line of code after block
					ld = BinToInt(tmpStorage[line+1])
					tmpStorage[ld+line+2] = Memory[tmpStorage[line+2]]
					del tmpStorage[line+1]
					del tmpStorage[line+1]

				elif value == '0011':
					#add 2 varibles and put the result in another variable
					Memory[tmpStorage[line+3]] = BitAdder(Bit, [Memory[tmpStorage[line+1]], Memory[tmpStorage[line+2]]])
					for i in range(3):
						del tmpStorage[line+1]

				elif value == '0100':
					#subtract 2 varibles and put the result in another variable
					Memory[tmpStorage[line+3]] = BitSubtractor(Bit, [Memory[tmpStorage[line+1]], Memory[tmpStorage[line+2]]])
					for i in range(3):
						del tmpStorage[line+1]

				elif value == '0101':
					pass #*
				elif value == '0110':
					pass #/

				elif value == '0111':
					#print
					pv = Memory[tmpStorage[line+1]]
					print('>'+str(BinToInt(pv)))
					del tmpStorage[line+1]
				elif value == '1000':
					#input
					Memory[tmpStorage[line+1]] = IntToBin(int(input('<')))
					del tmpStorage[line+1]

				line+=1


		elif button == 'q':
			break
		elif button == 'm':
			print(Memory)
		elif button == 's':
			print(f'{Storage}\n{tmpStorage}')
		elif button == 'h':
			print(open('README.txt', 'r').read())


