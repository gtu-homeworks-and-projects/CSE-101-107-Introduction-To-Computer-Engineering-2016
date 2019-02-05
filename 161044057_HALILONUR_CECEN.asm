	load R5,0
	load R8,0 
	load RB,1
	load RA,0
	load R6,48
	load R7,00000001b
	load R1,10101100b
	load R2,11101100b
newm:	xor R3,R1,R2
match:	and R4,R3,R7
	load R0,8
	jmpEQ R8=R0,FIN
	load R0,0
	jmpEQ R4=R0,COUNT
FIN:	addi RF,R9,R6
	load R0,0	
	load R9,0
	load R8,0
	jmpEQ R5=R0,newmatch
	jmpEq RA=R0,lastmatch
	HALT
	
	
	
	
COUNT:	addi R9,R9,R7
		ror R3,1
		addi R8,R8,RB
		jmp match

newmatch:		load R1,11100111b
		load R2,11111111b
		load R5,1
		addi R8,R8,RB
		jmp newm

lastmatch:		load R1,01010101b
		load R2,01000001b
		load RA,1
		addi R8,R8,RB
		jmp newm
