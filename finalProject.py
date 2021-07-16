from __future__ import print_function
from collections import OrderedDict
import copy
#---------------------START OF STORAGE IN DATA STRUCTURES-----------------------
dict_list = []
file = open("data.txt", "r")
iC = 'A'
counter = 0
for line in file:
    counter = counter + 1
    myDict = OrderedDict()      #makes an ordered dictionary
    stp_line = line.strip()     #strip of newline
    line_list = stp_line.split() #separate lines by space
    for idx, ele in enumerate(line_list): #gets rid of colon for each key
        line_list[idx] = ele.replace(':', '')

    key = iC                #adding A to the first of every dictionary
    myDict[key] = counter   #adding the number which A is at
    for x,y in enumerate(line_list): #loop to add to dictionary
        if x % 2 == 0:   #i case (key)
            key = y
        else:            #i+1 case (val)
            myDict[key] = y
    dict_list.append(myDict)   #add dictionary to list
    #print('\n'.join(map(str, dict_list)))

lod_copy = []       #copy of list of dictionaries
for li in dict_list:    #deep copying each List
    d2 = copy.deepcopy(li)
    lod_copy.append(d2)
#print('\n'.join(map(str, lod_copy)))    #print statement for copied list of dict
#------------------END OF STORAGE IN DATA STRUCTURES---------------------------

#--------------BEGINNING OF FIND and SEARCH ALGORITHMS-------------------------
file2 = open("final.txt", 'r')  #opens testing file
query_num = 0                   #total queries ran
for l2 in file2:                #reading line by line through file
    l2_strp = l2.strip()        #stripping newline from the line
#-----------------------BEGINNING OF FIND ALGORITHM-----------------------------
    if l2_strp == "FIND":       #find values in dictionaries and output
        query_num = 1 + query_num   #increment query count
        print("//Query %d" %query_num)
        #print("FIND CASE HIT")  #the selected keys values from that dictionary
        lod_DB = []
        for ll in lod_copy:          #deep copying list of dictioary
            d3 = copy.deepcopy(ll)
            lod_DB.append(d3)
        #print('\n'.join(map(str, lod_DB)))
        #print("lod_DB was loaded")
    #----LOADING CONDITIONS/SELECTS TO SEARCH THROUGH DICTIONARY AND OUTPUT----
        fCon_list = []             #list to hold each line of the conditions
        for l2 in file2:
            if (l2.endswith(';\n')):  #if it is the final line to be read
                fCon_list.append(l2)
                break
            else:                    #each CONDITION to be stored
                fCon_list.append(l2)
#------------------------PARSING THROUGH EACH LINE AND STORING------------------
        selCnt = 0            #how many dictionaries were appended
        select_list = []      #what values to take out of each dictionary
        lod_remove = []       #database to be passed first conditions hits and check
        for ls in lod_DB:          #deep copying list of dictionary
            d4 = copy.deepcopy(ls)
            lod_remove.append(d4)
        #print('\n'.join(map(str, lod_remove)))
        for fConSearch in fCon_list:    #splitting and storing info to search with
            fsplit = fConSearch.split() #split the line to hold each string individually
            if (fConSearch.endswith(';\n')):    #storing projections
                #print("Endswith Case Hit")
                fNew = fConSearch.replace(';\n', '')
                for ln in fNew:            #adding all the select variables to a list
                    lns = ln.strip()       #stripping the spaces and making separate
                    select_list.append(lns) #adding them to the list of select variables
                #print(' '.join(map(str, select_list))) #print statement for select_list

            #WORKS PROPERLY if the length is only a key with space
            elif len(fConSearch) == 2:
                #print("SINGLE LETTER WITH NO CONDITION HIT")
                remCnt = 0          #removal count
                corCnt = 0          #match count
                ylod_hits = []         #reoccuring hit tracker for each condition
                cKey = fConSearch[0]
                cond_list = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y']
                cond_check = 0;       #make sure key exists

                #combines up each line for the projections to manipulate
                for dict in lod_remove:     #checking each dictionary in lod_remove
                        corCnt = corCnt + 1
                        ylod_hits.append(dict)   #append to hits

                if corCnt == 0: #if a condition never hits, there will be no output
                    break

                lod_remove = []             #clear out lod remove
                for lr in ylod_hits:          #deep copying of hit list of dictioaries
                    d5 = copy.deepcopy(lr)   #initialize the line as a deep copy
                    lod_remove.append(d5)    #append the line to lod_remove to be read again

            #if the key has a condition to it
            else:
                remCnt = 0          #removal count
                corCnt = 0          #match count
                lod_hits = []         #reoccuring hit tracker for each condition
                cond_list = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y']
                cond_check = 0;       #make sure key exists
                cKey = fsplit[0]      #key to look for
                cCond = fsplit[1]     #condition on the key's Value
                cVal = fsplit[2]      #store the value to be checked
                for i in cond_list:
                    if cKey == i:
                        cond_check = cond_check + 1

                if cond_check == 0:
                    print("ERROR, INVALID KEY")
                    break

                else:
                    if cCond == '=':            #equal to condition
                        for dict in lod_remove: #checking each dictionary in lod_remove
                            if cKey in dict:            #if key is in dictionary
                                if dict[cKey] != cVal:  #if key's val does not match
                                    remCnt = 1 + remCnt
                                else:                   #if key's val does matches
                                    corCnt = corCnt + 1
                                    lod_hits.append(dict)   #append to hits

                            else:
                                remCnt = 1 + remCnt       #if key is not in dictionary

                    elif cCond == '<':         #less than to condition
                        for dict in lod_remove: #checking each dictionary in lod_remove
                            if cKey in dict:    #if key is in dictionary
                                if dict[cKey] >= cVal:  #if key is greater than or equal to cVal
                                    remCnt = 1 + remCnt #remove counter
                                else:           #if key's value is less than cVal
                                    corCnt = corCnt + 1 #Correct
                                    lod_hits.append(dict)   #append to hits dictionary
                            else:           #if its not in the dictionary, removed
                                remCnt = 1 + remCnt

                    elif cCond == '>':         #greater than to condition
                        for dict in lod_remove: #checking each dictionary in lod_remove
                            if cKey in dict:      #if key is in DICTIONARY
                                if dict[cKey] <= cVal: #if key is less than or equal to values
                                    remCnt = 1 + remCnt #removed
                                else:                   #if val in dictionary is greater than cVal
                                    corCnt = corCnt + 1 #mark to correct
                                    lod_hits.append(dict) #append to hit dictionary
                            else:
                                remCnt = 1 + remCnt #if its not in the dictionary, remove
                    #print("Removed: %d, Correct Found: %d" %(remCnt,corCnt))

                    if corCnt == 0: #if a condition never hits, there will be no output
                        print(" ")
                        break
                    #1st Case: clear remove and store with hits from the condition
                    #2nd Case: this loop will read through remove each time,
                    #          trimming the amount of hits per condition
                    lod_remove = []             #clear out lod remove
                    for lr in lod_hits:          #deep copying of hit list of dictioaries
                        d5 = copy.deepcopy(lr)   #initialize the line as a deep copy
                        lod_remove.append(d5)    #append the line to lod_remove to be read again
            #print('\n'.join(map(str, lod_remove))) #put here to check per condition
        #print("IN CASE LIST:")
        #print('\n'.join(map(str, lod_remove))) #put here to check end of loop
        #print('\n')
        #NEEDS TO BE WITHIN THIS FOR LOOP
#-------------------------END OF DOING THE FINDING-----------------------------#

#----------------------START OF OUTPUT USING PROJECTIONS-----------------------#
        #select_list is the list that stores the projections
        perf_list = []      #list without the whitespaces
        lod_output = []     #list of dictionaries for output
        proj_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Z']
        for i in select_list:   #search through it
            if i != '':     #if its not a whitespace
                perf_list.append(i) #append to perf_list
        #print("Perfect Projections Printed")
        #print(' '.join(map(str, perf_list)))
        #print("Projection length: %d" %len(perf_list))
#------------------------#SECTION OF CODE ADJUSTED-----------------------------
        projCheck = 0 # projection counter
        loP_list = []   #correct projections to use  
        for proj in perf_list:
            if proj in proj_list:
                projCheck = projCheck + 1
                loP_list.append(proj)                
        #print("Projection Check: %d" %projCheck)
#---------------------SECTION OF ADJUSTED CODE---------------------------------
        #uses LOD_REMOVE
        if 'Z' in loP_list:         
            #print('\n'.join(map(str, lod_remove)))
            #print('\n')
            for dict in lod_remove:
                for key in dict:
                    print("%s: %s " %(key,dict[key]), end ='')
                print('')
            print('')
            #    lod_format.append(dl)
            #    print('\n'.join(map(str,lod_format)))

        #uses LOD_OUTPUT
        else:
            for dict in lod_remove:     #looking through the remaining dictionaries
                outDict = OrderedDict() #initialize a dictionary per dictionary
                for key in dict:        #looking through each key of the dictionary
                    for x in loP_list: 
                        if x == key:        #if the projection matches the key
                            outDict[x] = dict[key]   #the keys value is passed to the output dictionary
                if len(outDict) > 0:   #if dictionary is not empty after checking for projections
                    lod_output.append(outDict) #append to output
            #print("OUTPUT LIST")
            #print('\n'.join(map(str, lod_output)))
            #print('\n')
            for dict in lod_output:
                for key in dict:
                    print("%s: %s " %(key,dict[key]), end ='')
                print('')
            print('')
#--------------END OF FIND ALGORITHM----------------

#--------------START OF SORT ALGORITHM--------------
    elif l2_strp == "SORT":
        lod_sDB = []
        query_num = 1 + query_num
        print("//Query %d" %query_num)
        sCond_list = []
        for ll in lod_copy:          #deep copying list of dictioary
            d3 = copy.deepcopy(ll)
            lod_sDB.append(d3)
        for l2 in file2:
            if (l2.endswith(';\n')):  #if it is the final line to be read
                l2.rstrip('\n')
                sCond_list.append(l2)
                break;               #breaks out of the loop to prevent the wrong lines from being read
            else:                    #not the final line in query
                l2.rstrip('\n')
                sCond_list.append(l2)

        cond_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'Y']
        project_list = []
        sCond_check = 0
        for sConSearch in sCond_list:    #splitting and storing info to search with
            ssplit = sConSearch.split()  #split the line to hold each string individually
            if (sConSearch.endswith(';\n')):    #storing projections
                sNew = sConSearch.replace(';\n', '')
                for ls in sNew:            #adding all the select variables to a list
                    lss = ls.strip()       #stripping the spaces and making separate
                    project_list.append(lss) #adding them to the list of projections
                
                sKey = ssplit[0]
                sOrder = ssplit[2]
                for i in cond_list:     #check the condition to see if anything is to be returned
                    if sKey == i:       #if key matches on of the conditions
                        sCond_check = sCond_check + 1

                if sCond_check == 0: #if it doesnt match any
                    print('')   #print nothing
                    break;      #break the loop

                if sOrder == '1':       #SORT IN ASCENDING ORDER
                    lod_sort = [];      #list of dictionaries with the key
                    for dict in lod_sDB: #go through each dictionary
                        if sKey in dict: #if the key is in the dictionary
                            lod_sort.append(dict) #append the dictionary

                    listVal = []          #list to store keys
                    for dict in lod_sort:   #open each dictionary in sort
                        if sKey in dict:    #if sKey is in dictionary
                            listVal.append(dict[sKey]) #append value
                    #print("Pre-Sort:")
                    #print(', '.join(map(str, listVal)))

                    #bubble SORT
                    n = len(listVal)
                    for i in range(n):
                        for j in range(0, n-i-1):
                            if listVal[j] > listVal[j+1]:
                                listVal[j], listVal[j+1] = listVal[j+1], listVal[j]

                    #to order the list of dictionaries
                    sort_output = []
                    for i in listVal:
                        for dict in lod_sort:
                            if i == dict[sKey]:
                                sort_output.append(dict)
                        break;
                    
                    #USES SORT_OUTPUT
                    for dict in sort_output:
                        for key in dict:
                            print("%s: %s " %(key,dict[key]), end ='')
                        print('')
                    print('')

                elif sOrder == "-1":    #SORT IN DESCENDING ORDER
                    lod_sort = [];      #list of dictionaries with the key
                    for dict in lod_sDB: #go through each dictionary
                        if sKey in dict: #if the key is in the dictionary
                            lod_sort.append(dict) #append the dictionary

                    listVal = []          #list to store keys
                    for dict in lod_sort:   #open each dictionary in sort
                        if sKey in dict:    #if sKey is in dictionary
                            listVal.append(dict[sKey]) #append value
                    
                    #bubble SORT
                    n = len(listVal)
                    for i in range(n):
                        for j in range(0, n-i-1):
                            if listVal[j] < listVal[j+1]:
                                listVal[j], listVal[j+1] = listVal[j+1], listVal[j]
                    #print("Post-Sort:")
                    #print(', '.join(map(str, listVal)))

                    sort_output = []
                    for i in listVal:
                        for dict in lod_sort:
                            if i == dict[sKey]:
                                sort_output.append(dict)
                        #break;
                    #USES SORT_OUTPUT
                    for dict in sort_output:
                        for key in dict:
                            print("%s: %s " %(key,dict[key]), end ='')
                        print('')
                    print('')

                else:
                    print("ERROR")
                    break

    else:
        query_num = 1 + query_num
        print("//Query %d" %query_num)
        eCon_list = []             #list to hold each line of the conditions
        for l2 in file2:
            if (l2.endswith(';\n')):  #if it is the final line to be read
                eCon_list.append(l2)
                break
            else:                    #each CONDITION to be stored
                eCon_list.append(l2)

        if "FIND" or "SORT" not in eCon_list:
            print("ERROR\n")
#--------------END OF SORT ALGORITHM-----------------
