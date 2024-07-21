# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:05:20 2024

@author: gbulb
"""
class Creating_a_Character_Table_from_Genetic_Strings:
     def find_character_tables(list_of_strings):
        STRING_0,STRING_1,STRING_2,STRING_3,STRING_4,STRING_5,STRING_6,STRING_7='','','','','','','',''
        for i,string in enumerate(list_of_strings):
            for j in range(len(string1)):
                if j==0 and string[j]=='A':
                    STRING_0+='1'
                elif j==0 and string[j]=='C':
                    STRING_0+='0'
                if j==1 and string[j]=='T':
                     STRING_1+='1'
                elif j==1 and string[j]=='G':
                     STRING_1+='0'
                if j==2 and string[j]=='T':
                     STRING_2+='1'
                elif j==2 and string[j]=='G':
                     STRING_2+='0'
                if j==3 and string[j]=='T':
                     STRING_3+='1'
                elif j==3 and string[j]=='C':
                     STRING_3+='0'
                if j==4 and string[j]=='T':
                     STRING_4+='1'
                elif j==4 and string[j]=='G':
                     STRING_4+='0'
                if j==5 and string[j]=='A':
                     STRING_5+='1'
                elif j==5 and string[j]=='C':
                     STRING_5+='0'
                if j==6 and string[j]=='T':
                      STRING_6+='1'
                elif j==6 and string[j]=='C':
                      STRING_6+='0'
                if j==7 and string[j]=='C':
                      STRING_7+='1'
                elif j==7 and string[j]=='A':
                      STRING_7+='0'
        #print(STRING_0,STRING_1,STRING_2,STRING_3,STRING_4,STRING_5,STRING_6,STRING_7)
        print(STRING_0)
        print(STRING_1)
            
if __name__=="__main__":          
    string1,string2,string3,string4,string5='ATGCTACC','CGTTTACC','ATTCGACC','AGTCTCCC','CGTCTATC'
    list_of_strings=[string1,string2,string3,string4,string5]
    Creating_a_Character_Table_from_Genetic_Strings.find_character_tables(list_of_strings)
    
    