# out_n = 0
# done = False
# with open("onelinefile.txt") as in_file:
#     while not done: #loop over output file names
#         with open(f"out{out_n}.txt", "w") as out_file: #generate an output file name
#             while not done: #loop over lines in inuput file and write to output file
#                 try:
#                     line = next(in_file).strip() #strip whitespace for consistency
#                 except StopIteration:
#                     done = True
#                     break
#                 if "SPLIT" in line: #more robust than 'if line == "SPLIT\n":'
#                     break
#                 else:
#                     out_file.write(line + '\n') #must add back in newline because we stripped it out earlier 
#             out_n += 1 #increment output file name integer

import csv

def ReadText( textfile ) :
    
    data = "" 
    with open( textfile,"r" ) as file :
        data = file.read()

    return data        


def ParseCSV( data ) :

    csvdata = [[]]      # empty 2d list
    

    # two pointers to traverse the string and slice it accordingly
    ptr1 = 0 ;      
    ptr2 = 0 ;
    row = []

    for ptr2 in range( len(data) ) :        # traversing the string

        dataptr1 = data[ptr1]
        dataptr2 = data[ptr2]

        # trying to change the pointer data's datatype 
        try :  dataptr1 = int(dataptr1) 
        except : pass

        try :  dataptr2 = int(dataptr2) 
        except : pass

        # check if both pointer datatype are not equal and that data is not "."
        if (type( dataptr1 ) != type( dataptr2 ) and dataptr2 != ".") or (ptr2 == len( data ) -1)  :
            
            if( ptr2 == len( data ) -1  ) : ptr2 += 1

            row.append( data[ ptr1 : ptr2 ] )
            ptr1 = ptr2 
            
            if ( len(row) == 4 ) :
                
                # CSV WRITING WITH writerow
                with open( "./demo.csv", "a", newline="" ) as csvfile :
                    write_obj = csv.writer( csvfile )
                    write_obj.writerow( row )

                row = []
            
# MAIN METHODS HERE
textdata = ReadText( "./onelinefile.txt" )
ParseCSV( textdata )