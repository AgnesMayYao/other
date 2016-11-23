import math
if __name__ == '__main__':
    data_file = open("small.txt","r")
    
    win=[]
    lose=[]
    win_team=[]
    lose_team=[]
    
    for line in data_file:
        temp=line.split()
        if len(temp)==11:   
            win.extend(map(int,temp[1:6]))
            lose.extend(map(int,temp[6:11]))
            #win_team.append(map(int,temp[1:6]))
            #lose_team.append(map(int,temp[6:11]))
    
    data_file.close()
    
    #sorted win/lose
    win.sort()
    lose.sort()
    
    #all hero numbers
    all_no=[]
    all_no.extend(list(set(win)))
    all_no.extend(list(set(lose)))
    all_no.sort()
    all_no=list(set(all_no))
    
    #all_no_win=[0]*len(all_no)
    p_x_w=[0]*len(all_no)
    p_x_l=[0]*len(all_no)
    
    #bayes
    #p_w=len(win)
    #p_l=len(lose)
    
    for i in range(0,len(all_no)):
        p_x_w[i]=win.count(all_no[i])
        p_x_l[i]=lose.count(all_no[i])   
        #all_no_win[i]=p_x_w[i]*1.0/(p_x_w[i]+p_x_l[i])
        
    #penalize
    mean_w=sum(p_x_w)*1.0/len(p_x_w)
    max_pen_w=(max(p_x_w)-mean_w)*1.0/100
    min_pen_w=(mean_w-min(p_x_w))*1.0/100
    
    mean_l=sum(p_x_l)*1.0/len(p_x_l)
    max_pen_l=(max(p_x_l)-mean_l)*1.0/100
    min_pen_l=(mean_l-min(p_x_l))*1.0/100
               
    #p_x_w=list(map(lambda x:max(x-max_pen_w,mean_w) if x>mean_w else min(x+min_pen_w,mean_w),p_x_w))
    #p_x_l=list(map(lambda x:max(x-max_pen_l,mean_l) if x>mean_l else min(x+min_pen_l,mean_l),p_x_l))
    
    p_x_w=list(map(lambda x:math.sqrt(x)+1,p_x_w))
    #p_x_w=list(map(lambda x:1 if x<=0,p_x_w))
    p_x_l=list(map(lambda x:math.sqrt(x)+1,p_x_l))
    #p_x_l=list(map(lambda x:1 if x<=0,p_x_l))
    
    #for those doesn't appear in the training set    
    p_x_w.append(sum(p_x_w)*1.0/len(p_x_w)/2)
    p_x_l.append(sum(p_x_l)*1.0*2/len(p_x_l))
        
    correct=0
    wrong=0
    #predict for one team
    new_data_file = open("small.txt","r")   
    for line in new_data_file:
        temp=line.split()
        if len(temp)==11:   
            win_team.append(map(int,temp[1:6]))
            lose_team.append(map(int,temp[6:11]))
            
    new_data_file.close()
            
    
    for j in range(0,len(win_team)): 
        #x1 = int(raw_input("x1: "))
        #x2 = int(raw_input("x2: "))
        #x3 = int(raw_input("x3: "))
        #x4 = int(raw_input("x4: "))
        #x5 = int(raw_input("x5: "))

        #[x1,x2,x3,x4,x5]=list(map(lambda x:all_no.index(x),[x1,x2,x3,x4,x5]))
        [x1,x2,x3,x4,x5]=list(map(lambda x:all_no.index(x) if x in all_no else len(p_x_w)-1,win_team[j]))
        P_team_w=p_x_w[x1]*p_x_w[x2]*p_x_w[x3]*p_x_w[x4]*p_x_w[x5]*1.0/(p_x_w[x1]*p_x_w[x2]*p_x_w[x3]*p_x_w[x4]*p_x_w[x5]+p_x_l[x1]*p_x_l[x2]*p_x_l[x3]*p_x_l[x4]*p_x_l[x5])
        [x1,x2,x3,x4,x5]=list(map(lambda x:all_no.index(x) if x in all_no else len(p_x_w)-1,lose_team[j]))
        P_team_l=p_x_w[x1]*p_x_w[x2]*p_x_w[x3]*p_x_w[x4]*p_x_w[x5]*1.0/(p_x_w[x1]*p_x_w[x2]*p_x_w[x3]*p_x_w[x4]*p_x_w[x5]+p_x_l[x1]*p_x_l[x2]*p_x_l[x3]*p_x_l[x4]*p_x_l[x5])
        if P_team_w>P_team_l:
            correct+=1
        else:
            wrong+=1
    
    
    
    
    print correct*1.0/(correct+wrong)
    