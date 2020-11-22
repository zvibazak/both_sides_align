import random

def both_sides_align(txt,size,max_spaces=5):
    res = ""
    for line in txt.splitlines():
        line_text_left = line
        this_line = ""
            
        while line_text_left:
            #try to get next word to this_line 
            firstWord=""
            try:
                (firstWord, rest) = line_text_left.split(maxsplit=1)
            except:
                #this is the last word
                rest=''
                firstWord=''
                this_line = this_line+ " " + line_text_left
                line_text_left=''
            
            #the is place for more words...
            if len(this_line)+len(firstWord)<size and rest:
                this_line = this_line + " " + firstWord
                line_text_left = rest

            #no place - need to print this_line
            else:
                spaces_to_add=size-len(this_line)
                size_to_end_line = size-len(this_line)-2

                #one word with no space - need to split 
                if this_line=="":
                    res = res + (line_text_left[:(size-2)]+"-") + '\n'
                    line_text_left = line_text_left[(size-len(this_line)-2):]

                #another cases of split
                elif size_to_end_line>0 and (len(this_line.split(' '))==2 or (max_spaces and spaces_to_add>max_spaces and spaces_to_add<size) or len(this_line)>=size):
                    a=""
                    if len(line_text_left[:(size-len(this_line)-2)])>0:
                        a=(" " + line_text_left[:(size-len(this_line)-2)]+"-")
                        #line_text_left = line_text_left[(size-len(this_line)-2):]

                    res = res + (this_line[1:]+a) + '\n'
                    
                    line_text_left = line_text_left[(size-len(this_line)-2):]
                
                elif len(this_line.split(' '))-1>1:  
                    #time to add spaces
                    if line_text_left:
                        for _ in range(spaces_to_add):
                            ran_pos = random.randint(2,len(this_line.split(' '))-1)
                            parts = this_line.split(" ",maxsplit=ran_pos)
                            this_line = " ".join(parts[:-1]) + "  " +  " ".join(parts[-1:]) 
                    if len(this_line[1:])>size:
                        res = res + (this_line[1:size-1]+"-") + '\n'
                        this_line=this_line[size-1:]
                        
                    res = res + (this_line[1:]) + '\n'
                this_line = ""
    return res