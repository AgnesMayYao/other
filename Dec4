import math
import csv
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import pickle  # or import cPickle as pickle
import numpy as np

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
    
    data_file = open("2016-11-29.txt","r")
    
    for line in data_file:
        temp=line.split()
        
        if len(temp)>2:   
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
            data.append(team1)
            label.append(int(temp[21]))
            """  
            rn=np.random.rand()
            if rn>0.5:
                team1.extend(team2_copy)
                data.append(team1)
                label.append(1)
            else:              
                team2.extend(team1_copy)
                data.append(team2)
                label.append(0)
            """
            
            #label.append(int(temp[21]))
            
            #label.append(0)    
    
    data_file.close()
        
    
    X_train,X_test,Y_train,Y_test=train_test_split(data,label,test_size=0.2,random_state=1)
    
 
    logreg = linear_model.LogisticRegression()
    
    logreg.fit(data, label)
    
    true_positive=0
    true_negative=0
    false_positive=0
    false_negative=0
    
    
    prediction=logreg.predict(X_test)
    for i in range(0,len(prediction)):
        if prediction[i]==Y_test[i]:
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
    
    
    #result_file_name+=".csv"
    #result_file = open(result_file_name,'wb')
    #wr = csv.writer(result_file, dialect='excel')
    #wr.writerows(results)
    #result_file.close()
    
    
    # Write to file
    _myfile = open('model.pickle', 'wb')
    pickle.dump(logreg, _myfile)
    _myfile.close()
