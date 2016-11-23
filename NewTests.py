import math
import csv
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
import pickle  # or import cPickle as pickle

if __name__ == '__main__': 
    mapping=[0]*134
    data=[]
    label=[]
    
    
    with open("champions.tsv") as tsv:
        for line in csv.reader(tsv, dialect="excel-tab"): 
            temp=map(int,line[0:2])
            mapping[temp[0]]=temp[1]
    #print mapping
            
    tsv.close()
    
    data_file = open("sample.txt","r")
    
    for line in data_file:
        temp=line.split()
        
        if len(temp)==11:   
            team1=[0]*134
            team1_copy=[0]*134

            win=map(int,temp[1:6])
            for i in range(0,len(win)):
                win_index = mapping.index(win[i])
                team1[win_index]=1    
                team1_copy[win_index]=1

            team2=[0]*134
            team2_copy=[0]*134
            lose=map(int,temp[6:11])
            for i in range(0,len(lose)):
                lose_index = mapping.index(lose[i]) 
                team2[lose_index]=1 
                team2_copy[lose_index]=1
            
            team1.extend(team2_copy)
            team2.extend(team1_copy)

            data.append(team1)
            data.append(team2)
            
            label.append(1)
            label.append(0)    
    
    data_file.close()
    
    f_myfile = open('model.pickle', 'rb')
    logreg = pickle.load(f_myfile)  # variables come out in the order you put them in
    f_myfile.close()
        
    true_positive=0
    true_negative=0
    false_positive=0
    false_negative=0
    
    prediction=logreg.predict(data)
    for i in range(0,len(prediction)):
        if prediction[i]==label[i]:
            if prediction[i]==1:
                true_positive+=1
            else:
                true_negative+=1
        else:
            if prediction[i]==1:
                false_positive+=1
            else:
                false_negative+=1
                
                
    precision=1.0*true_positive/ (1.0*true_positive + false_positive)
    accuracy=(1.0*true_positive+true_negative)/(false_positive+false_negative+true_positive+true_negative)
    
    print [true_positive,true_negative],[false_positive,false_negative]
    print "precision = ",precision
    print "accuracy = ",accuracy