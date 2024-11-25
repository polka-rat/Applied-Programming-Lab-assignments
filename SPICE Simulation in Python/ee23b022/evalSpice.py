#Assignment 2 - SPICE simulation

#Date: 31.8.24
#Name: Deepak Charan S
#Roll No: EE23B022

#Description: To solve a circuit using Kirchoff's Laws. the circuit is provided to us in a file which contains voltage sources/current sources/resitors between two nodes and its value. We should also check against invalid files/ invalid parameters / unsolvable circuits and report the respective error

from collections import defaultdict
import numpy as np


def evalSpice(filename)->tuple([dict]): 
    cond_connections=defaultdict(dict)          # A dictionary to store the value of resistors between two nodes
    cur_sources=defaultdict(int)                # A dictionary to store current sources
    vol_sources=[]                              # A list to store voltage sources
    
    nodes=defaultdict(int)                                # A set to contain all the distinct nodes
                                      
    try:
        with open(filename) as f:
            file = [line.strip() for line in f.readlines()]         # A list to store all the lines without the newline character
    except FileNotFoundError:                                       # Invalid File
        raise FileNotFoundError('Please give the name of a valid SPICE file as input')      
    
    try:
        start=file.index(".circuit")+1              # Only the lines between '.circuit' and '.end' are relevant for us
        end=file.index(".end")
    except ValueError:                      # File is malformed
        raise ValueError('Malformed circuit file')
    
    GND_flag=0
    
    for i in range(start,end):
        val=None
        if len(file[i])==0: #if there is a space between lines
            continue
        if '#' in file[i]:  # Removing Comments
            file[i]=file[i][:file[i].index('#')]
            
        if file[i][0].upper() == 'V':       # A voltage source
            val=file[i].split()
            if len(val) !=5:
                raise ValueError("Malformed Circuit")
            for i in range(len(vol_sources)):
                if sorted(val[1:3])==sorted(vol_sources[i][1:3]):          
                    if val[-1]!=vol_sources[i][-1]:          # A Voltage source already exists between 2 nodes and of different value (circuit cant exist)
                        raise ValueError('Circuit error: no solution')
            vol_sources.append(val)     #storing it in our list
            
            if val[1]=='GND' or val[2]=='GND':
                GND_flag=1
                
            nodes[val[1]]+=1      
            nodes[val[2]]+=1
            nodes[val[0]]+=2
            
        elif file[i][0].upper() == 'I':         # A current source
            # file[i]=file[i][:file[i].index('dc')]+file[i][file[i].index('dc')+2:]  
            val=file[i].split()
            nodes[val[1]]+=1
            nodes[val[2]]+=1
            
            if val[1]=='GND' or val[2]=='GND':
                GND_flag=1
            
            cur_sources[val[1]]-=float(val[-1])      #Storing it in our Dictionary
            cur_sources[val[2]]+=float(val[-1])     # Current leaving a node is taken as postive by convention
            
        elif file[i][0].upper() == 'R':         # A resistor
            val=file[i].split()
            
            nodes[val[1]]+=1
            nodes[val[2]]+=1
            
            if val[1]=='GND' or val[2]=='GND':
                GND_flag=1
            
            try:        #checking if there was already a resistor connected between both the nodes
                cond_connections[val[1]][val[2]]+=1/(float(val[-1])) 
                cond_connections[val[2]][val[1]]+=1/(float(val[-1]))
            
            except KeyError:    # No previous resistor was found
                cond_connections[val[1]][val[2]]=1/(float(val[-1]))     # Storing the value of conductance (1/resistance) in between the 2 nodes
                cond_connections[val[2]][val[1]]=1/(float(val[-1]))

    
        else:       # Invalid element (in this assignment) was present
            raise ValueError('Only V, I, R elements are permitted')

        
    if GND_flag==0:
        raise ValueError("Circuit is Invalid, no ground....")
        
    float_node_check=dict(nodes)        # To check for floating nodes (where one node is left open)

    for i in cur_sources:
        if float_node_check[i]<2 or float_node_check[i]<2:
            raise ValueError("Floating node detected")
        
    nodes=list(nodes.keys())
    nodes.sort()
    count=0
    
    dnodes={}   # Since we have to assign a node a position in the matrix, I am using a dictionary to store their indices
    for i in range(len(nodes)):     # Giving each node an index
        if nodes[i]=='GND':         # We do not need to solve for Voltage at GND as it is already taken as 0 by convention
            pass
        elif nodes[i][0].upper()=='V':      
            pass
        else:
            dnodes[nodes[i]]=count

            count+=1
    for i in vol_sources:
        dnodes[i[0]]=count
        count+=1
            
    n=len(nodes)-1
    mat=np.zeros((n,)*2)            # the coefficient matrix
    bmat=np.zeros((n,)*1)           

    mat_count=0
    for i in dnodes:
        if i[0].upper()=='V':
            continue
        for j in dnodes:
            if i==j:
                mat[dnodes[i]][dnodes[i]]=sum(cond_connections[i].values())     # Diagonal elements = sum of conductances joined to the node
            else:

                try:                # Non Diagonal elements = -1*(conductance between nodes i and j)
                    mat[dnodes[i]][dnodes[j]]=-cond_connections[i][j]
                    mat[dnodes[j]][dnodes[i]]=-cond_connections[i][j]
                except KeyError:
                    pass
                         
        mat_count+=1        
    
    
    for i in vol_sources:           
        if i[2]=='GND':        # will have its own equation (Vi-0=V)
            mat[dnodes[i[1]]][dnodes[i[0]]]=1
            mat[mat_count][dnodes[i[1]]]=1
            bmat[mat_count]=float(i[-1])
            mat_count+=1
        elif i[1]=='GND':       #will have its own equation (0-Vj=V)
            mat[dnodes[i[2]]][dnodes[i[0]]]=-1
            mat[mat_count][dnodes[i[2]]]=-1
            bmat[mat_count]=float(i[-1])
            mat_count+=1
        else:      # supernode (Vi-Vj=V)
            mat[dnodes[i[1]]][dnodes[i[0]]]=1
            mat[dnodes[i[2]]][dnodes[i[0]]]=-1
            mat[mat_count][dnodes[i[1]]]=1
            mat[mat_count][dnodes[i[2]]]=-1
            bmat[mat_count]=i[-1]
            mat_count+=1
            
    for i in cur_sources:       #adding in the current source values in our matrix
        if i!='GND':           
            bmat[dnodes[i]]=cur_sources[i]
            
        
        mat_count+=1
    
    for i in mat:
        if i.any()==False:      # checking for 0 rows in our matrix (Occurs when we have an invalid circuit)
            raise ValueError('Circuit error: no solution')
    
    try:
        sol=np.linalg.solve(mat,bmat)  
    except np.linalg.LinAlgError:     #singular matrix (no solution)
        raise ValueError("Circuit has no solution")

    node_volt={'GND':0}
    curr_branch={}
    
    for i in dnodes:    # Filling in the solutions
        if i[0].upper()=='V':
            curr_branch[i]=sol[dnodes[i]]       
        else:
            node_volt[i]=sol[dnodes[i]]
      
    return (node_volt, curr_branch)



