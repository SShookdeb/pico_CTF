#copyright@file

jumple_flag = "ocip{FTC0l_I4_t5m_ll0m_y_y3n58a025e3ÿº"

#break up upto 4 charecter
blocks = [] 
for i in range(0,len(jumple_flag),4):
	c = jumple_flag[i:]
	if len(c) > 4:
		c = c[0:4]
	blocks.append(''.join(c))

flag =''
for block in blocks:
	flag = flag + block[::-1]
print(flag) 
