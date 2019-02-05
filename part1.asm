	load R0,57
	load R2,1
	load R1,48
Rpt:	store R1,[255]
	move RF,R1
	load R1,[255]
	addi R1,R1,R2
	jmpLE R1<=R0,Rpt
