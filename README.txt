WELCOME:
	Welcome to Virtual Hardware! This is a Python program that 
	attempts to model an actual computer. This documentation covers
	how to use the "fake computer" part and the logic gates.

LOGIC GATES:
	This code also does come with
	several logic gates including OR, NOR, XOR, NOT, AND, and NAND. 
	(All of these functions return values)
	The syntax for these is as follows:
		Or([a, b])
		Nor([a, b])
		Xor([a, b])
		Not(a)
		And([a, b])
		Nand([a, b])
	(NOTE: a or b have to be either 1 or 0 as integers.)

BUILDING FURTHER:

	The other functions include:
		HalfAdder([a, b])
		FullAdder([a, b, carry])
		
		BitAdder(bit, ['', '']) (The only supported value for "bit" is 4,
	each number being added will be in the format '1001' or '0011'.)
	
		BitReverser(bit, a) (Number format is also a string    ^^
	The BitReverser takes a value and flips its 1s and 0s around
	using NOT gates. Example: '0001' would need the bit of 4 and
	would output: '1110'. This is useful for subtraction because we could
	take the number '0110' and say we wanted to subtract '0011'.
	We'd first reverse '0110' which would be '1001', then we add
	'0011' to the reversed value. '1100' is the sum, then we reverse again
	to get the difference: '0011'. Proving that 0110-0011=0011.)
	
		BitSubtractor(bit, ['', '']) Same syntax as BitAdder()
		
		BinToInt('') takes a string format 4 bit binary number and
	converts it to a integer.
	
		IntToBin(num) takes an integer and converts it to a string
	4 bit binary number

	IF YOU HAVE ANY IDEAS ON HOW TO FIX ANY BUGS PLEASE LET ME KNOW!


TO USE THESE FUNCTIONS:
	
	It would be helpful to change main.py's name to like vhw.py or something
	then:
	from vhw import *

DEFAULT COMPUTER SYSTEM:

	Welcome to the default "computer"! This can be runned by just 
	running the main.py file. Then you are sent to a loop of input() 
	functions. This is used to emulate keyboard presses. So you would
	press the desired key, and press ENTER.
	
	KEYS:
		e executes the script in the "script.bin" file, if there isn't
	a script.bin file it creates one with an empty program.
	
		q quits "computer"
		
		m prints data in "computer's" memory. Dictionary style: 
	{'1100':'0000', '1101':'0010',...}
	   ^      ^        ^      ^
	address value   address2 value2
	
		s prints "computer's" storage, basically script.bin, but
	also an extra. When a program executes, it may modify a temporary
	Storage file, the output of that would be printed below the actual
	Storage file. The temporary one can be used for debugging.
		
		h reads this file (h for help)
	
	HOW TO CODE THIS COMPUTER?
		
		This next section is how to code this "computer". You have to code
		in binary so it is a little pain, but it still works out fine. 
		Just a note: each "block" (series of four 1s and 0s) of code is
		read individually. So the program will read: 00010000 as [0001, 0000]
		To prevent hard reading, you may insert new lines or whitespaces however
		you choose. (0001 0000 is the same as
		0001
		0000
		and even 00010000)
		(You have to write your code into script.bin)
		
		Here some guide lines that I use for this function by function
		description, syntax, and examples:

			1. All caps 4 letter words means it a value that is variable. 
			2. () means that this is other text that should be added in,
			but can't because it has to follow the 4 letter rule. "LINE(s)"
			doesn't mean 1 or more lines, it litterally means "lines". 
			Or () just explain further what you are reading. NEVER ADD
			ANY OTHER CHARACTERS BESIDES 1 AND 0, AND EACH BLOCK CONSISTS
			OF ONLY 4 CHARACTERS. 
			3. "Example:\n" (\n = newline) means it's a multiline example,
			example ends at whitespace.

			0001 assign to variable
				Syntax:0001 VARI VALU
				Example: 0001 1100 0001

			0010 replace lines(vari) after with VARI
				Syntax: 0010 LINE(s) VARI
				Example: 
				0010 0001 1100
				VALU (Whatever 1100 memory address equals)

			0011 adds 2 variables
				Syntax: 0011 VAR1 VAR2 VAR3 (variable 3 is the output variable)
				Example: 0011 1100 1101 1110 (Adds memory address 1100's value
				with memory address 1101's value. It writes the sum in memory
				address 1110)

			0100 subtracts 2 variables
				Syntax: 0100 VAR1 VAR2 VAR3 (variable 3 is the output variable)
				Example: 0011 1100 1101 1110 (Subtracts memory address 1100's value
				with memory address 1101's value. It writes the difference in memory
				address 1110)

			0101 Does nothing

			0110 Does nothing

			0111 displays (or prints) a memory address's value in integer format
				Syntax: 0111 VARI
				Example: 0111 1100 (prints memory address 1100's value in integer format)

			1000 asks for input in the form of an integer and writes that integer  to memory
				Syntax: 0111 VARI
				Example: 0111 1100 (prints memory address 1100's value in integer format)



			CODE EXAMPLES:
			adder (not indented for easy copy/paste):
1000 1100
1000 1101
0011 1100 1101 1110
0111 1110

			subtractor:
1000 1100
1000 1101
0100 1100 1101 1110
0111 1110
