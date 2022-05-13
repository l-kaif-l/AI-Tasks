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