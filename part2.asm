	load R0,7
	load R5,0
	load R4,0
	load R1,10110111b
	load R2,1
rtr:	and R3,R1,R2
	addi R4,R4,R3
	ror R1,1
	addi R5,R5,R2
	jmpLE R5<=R0,rtr
	load R7,48
	addi RF,R4,R7
	
	HALT
	
	
