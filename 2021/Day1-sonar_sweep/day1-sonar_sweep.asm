.data
filename: .asciiz  "/home/fredrik/Documents/AdventOfCode/2021/Day1-sonar_sweep/day1data.txt"
buffer: .space 10012

.text
	la $a0, filename
	li $a1, 0       # readonly
	li $a2, 0
	li $v0, 13
	syscall         # open file
	move $a0, $v0    
	la $a1, buffer
	li $a2, 10012
    
read_file:
	li $v0, 14
	syscall
	beqz $v0, read_done
	addu $a1, $a1, $v0   # adjust buffer pointer
	subu $a2, $a2, $v0
	bnez $a2, read_file   # If buffer not full and not EOF, continue reading

read_done:
	# File copied to buffer
	# Read from buffer and convert each string to an int
	la $t0, buffer
	addi $t0, $t0, 10010	# starting from the end minus null byte and new line	
	addi $t1, $zero, 10				# ascii for new line
	addi $t3, $zero, 1
	addi $t5, $zero, 10012
	add $s2, $zero, $zero
	add $s0, $zero, $zero

first_number:			# get the first number (starting from behind)
	subi $t5, $t5, 1
	lb $a0, ($t0)
	subi $t0, $t0, 1
	sub $t2, $a0, $t1
	beqz $t2, next_number
	
	subi $a0, $a0, 48
	mul $t4, $t3, $a0
	add $s2, $s2, $t4
	mul $t3, $t3, 10
	j first_number
	
next_number:
	addi $t3, $zero, 1
	add $s1, $zero, $zero
	
next_char:
	subi $t5, $t5, 1
	beqz $t5, done
	lb $a0, ($t0)
	subi $t0, $t0, 1
	sub $t2, $a0, $t1
	beqz $t2, number_done
	
	subi $a0, $a0, 48
	mul $t4, $t3, $a0
	add $s1, $s1, $t4
	mul $t3, $t3, 10
	j next_char
	
number_done:	
	ble $s2, $s1, no_increase
	move $s2, $s1
	addi $s0, $s0, 1
	j next_number

no_increase:
	move $s2, $s1
	j next_number
	
done:
	ble $s2, $s1, no_increase_last
	move $s2, $s1
	addi $s0, $s0, 1
no_increase_last:
	move $a0, $s0
	li $v0, 1
	syscall 
