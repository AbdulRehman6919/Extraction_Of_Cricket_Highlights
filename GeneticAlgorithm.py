# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 20:59:35 2021

@author: Abdul Rehman
"""
class Genetic_Algo():
    
    #Orignal Code
    def Genetic_Algorithm(self,interest_val,Variety_val):
        #importing Libararies
        import glob
        import random as rd 
        import numpy  as np 
        import math as mt 
        
        #Giving Path of All Events To Count  the Total Events 
        Path_Four_files= glob.glob("./Runs/Fours"+"/*.mp4")
        Path_Six_files= glob.glob("./Runs/Sixes"+"/*.mp4")
        Path_Out_files= glob.glob("./Runs/Outs"+"/*.mp4")
        Path_Events_files= glob.glob("./Runs/Events"+"/*.mp4")
        
        #Assigning Tag to the Events & Giving Them Importance Level
        Events_Tag=[6,0,4,2]
        Imp_Level=[1.0,0.75,0.5,0.01]
        
        check =True #For Assigning the best chromosome for first Time 
        
        #Generating the Events List
        Events_list=[]
        for i in range(len(Path_Six_files)):
            Events_list.append(6)
        for i in range(len(Path_Four_files)):
            Events_list.append(4)
        for i in range(len(Path_Out_files)):
            Events_list.append(0)
        for i in range(len(Path_Events_files)):
            Events_list.append(2)
        print(Events_list)    
        Total_events=len(Events_list)
        print("Total Events in a list is: "+str(Total_events))
        
        Events_Count_List=[Events_list.count(6),Events_list.count(4),Events_list.count(0),Events_list.count(2)]
        
        
        #Specifying the Chromosome Length and Papulation
        chromsome_width=Total_events//2
        chromsome_Papulation=4
        
        Interest_value=interest_val
        Variety_value=Variety_val
        
        def Single_Chrmosome(self,chromsome_width):
            
            single_chromosome=[]
            for i in range(0,chromsome_width):
                single_chromosome.append(rd.choice(Events_list)) 
              
            return single_chromosome
        
        
        def Create_Full_Papulation(self,Papulation):
            
            for i in range(Papulation):
                Full_Papulation.append(Single_Chrmosome(self,chromsome_width))
        
        def Fitness_function(self,Full_Papulation):
            for i in Full_Papulation:
                temp=[i.count(6),i.count(0),i.count(4),i.count(2)]
                temp1=(((temp[0]*1.0)+(temp[1]*0.75)+(temp[2]*0.5)+(temp[3]*0.01))/len(i))
                Fitness=(Interest_value*temp1)+((1-(np.std(np.array([i.count(4),i.count(6),i.count(2),i.count(0)]))))*Variety_value)
                Fitness=round(Fitness,4)
                var=(i,Fitness,counter[0])
                Fitness_and_Papulation.append(var)
                counter[0]=counter[0]+1          
        
        def Make_Probability_List(self,Fitness_and_Papulation):   
            #Making Proabbalibibility List
            
            index=[1]
            Probabilty_list=[]
            #Selection on the basis of probability 
            for i in Fitness_and_Papulation:
                j=i[1] #Saving Cost in some varibale
                temp3=min(Fitness_and_Papulation, key=lambda x: x[1])
                
                for k in np.arange (0,j,temp3[1]):
                    Probabilty_list.append(index[0])
                index[0]=index[0]+1 
            print(Probabilty_list)
            print("Runs Safely")
            return Probabilty_list
        
        def Make_Random_Selection(self,Probabilty_list):
            for i in range(15):
                    safe=rd.choice(Probabilty_list)
                    for i in Fitness_and_Papulation:
                        if i[2]==safe:
                            Selection_List.append(i[0])
            
            return Selection_List
        def CrossOver_Criteria(self,Probabilty_list):
            import random as rd
            counter=[0]
            First=chromsome_width//2
            Second=chromsome_width - (chromsome_width//2)
            Selection_List=Make_Random_Selection(self,Probabilty_list)
            print("Length of Selection List is: "+str(len(Selection_List)))
            j=0
            value=chromsome_Papulation//2
            print("Value is: "+str(value))
            while j<value:
                
                    
                x,y=[],[]
                
                index_x=rd.randint(0, len(Selection_List)-1)
                index_y=rd.randint(0, len(Selection_List)-1)
                
                x= Selection_List[index_x]  #Picking First Chrmosome
                y= Selection_List[index_y]  #Picking Second Chrmosome
                      
                    
                list_1=[]  #Decaltion of temporary lists
                list_2=[]
                   
                for i in range(0,First):
                    list_1.append(x[i])
                    list_2.append(y[i])
                
                for i in range(First,chromsome_width):
                    list_1.append(y[i]) 
                    list_2.append(x[i])
                print("List 1 is: "+str(list_1))
                print("List 2 is: "+str(list_2))
                
                if ((list_1.count(6)<=Events_Count_List[0] and list_1.count(4)<=Events_Count_List[1] and list_1.count(0)<=Events_Count_List[2] and list_1.count(2)<=Events_Count_List[3]) and (list_2.count(6)<=Events_Count_List[0] and list_2.count(4)<=Events_Count_List[1]and list_2.count(0)<=Events_Count_List[2] and list_2.count(2)<=Events_Count_List[3])):
                    Cross_Over_List.append(list_1)
                    Cross_Over_List.append(list_2)
                else:
                    continue 
                    
                j=j+1         
                
                
                
        def Mutation_Probability(self):
            #We Assign Mutation proabability to 5%
            mutation_percent=2
            percent=(chromsome_width*chromsome_Papulation*mutation_percent)/100
            percent=mt.floor(percent)
            return percent
        def Doing_Mutation(self,Cross_Over_List):
            check=Mutation_Probability(self)
            #print("\nMutation Probablity is: ",check)
            for i in range(check):
                ran=rd.randrange(0,len(Cross_Over_List)) #Select a randomm list
                ch= Cross_Over_List[ran]
                for j in ch:
                    ran1=rd.randrange(0,chromsome_width) #Select random index of above list 
                    if ch[ran1]==6:
                        while(True):
                            temp=rd.choice(Events_list)
                            if temp!=6:
                                Events_list.append(ch[ran1])
                                name=temp
                                break
                            else:
                                continue
                              
                        ch[ran1]=name
                        
                    elif ch[ran1]==4:
                        while(True):
                            temp=rd.choice(Events_list)
                            if temp!=4:
                                Events_list.append(ch[ran1])
                                name=temp
                                break
                            else:
                                continue
        
                                        
                        ch[ran1]=name
                    elif ch[ran1]==2:
                        while(True):
                            temp=rd.choice(Events_list)
                            if temp!=2:
                                Events_list.append(ch[ran1])
                                name=temp
                                break
                            else:
                                continue
        
                                        
                        ch[ran1]=name    
                    else:
                        while(True):
                            temp=rd.choice(Events_list)
                            if temp!=0:
                                Events_list.append(ch[ran1])
                                name=temp
                                break
                            else:
                                continue
        
                                        
                        ch[ran1]=name
                    break
               
        for i in range(50):     
            Full_Papulation=[]  
            Fitness_and_Papulation=[]
            counter=[1]
            Probabilty_list=[] 
            Selection_List=[]      
            Cross_Over_List=[]
            
            Create_Full_Papulation(self,chromsome_Papulation) 
            Fitness_function(self,Full_Papulation)   
            print("Simple Pauplation With Fitness Function:")
            for i  in Fitness_and_Papulation:
                print("\t Chrome:",i[0],"\t Fitness:",i[1])
            
            Probabilty_list=Make_Probability_List(self,Fitness_and_Papulation)
            
            CrossOver_Criteria(self,Probabilty_list)
            Fitness_and_Papulation=[]
            Fitness_function(self,Cross_Over_List)
            print("After Crossover Results: ")
            for i  in Fitness_and_Papulation:
                 print("\tChrome:",i[0],"\t Fitness:",i[1])
            Fitness_and_Papulation=[]
            counter=[0]
            Doing_Mutation(self,Cross_Over_List)
            print("After Muattaion Results are :")
            Fitness_function(self,Cross_Over_List) #Fitness funcrion After Mutation 
            for i  in Fitness_and_Papulation:
                 print("\t Chrome:",i[0],"\t Fitness:",i[1])
               
                
            Best_Chormosome=list(max(Fitness_and_Papulation, key=lambda x: x[1])) 
            
            
            if check==True:
                Final_selected_Chormosome=Best_Chormosome
                check=False
            else:
                if Best_Chormosome[1]>Final_selected_Chormosome[1]:
                    Final_selected_Chormosome=Best_Chormosome
                
        print("Best Chromosome {} With Fitness Value is {} ".format(str(Final_selected_Chormosome[0]), str(Final_selected_Chormosome[1])))
    
        return Final_selected_Chormosome[0]




#%%
'''

bestone=[0, 0,4,4,2,2]
import glob 
import natsort as nt
import random as rd 
from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, afx, transfx, concatenate, CompositeVideoClip
 
Path_Four_files= glob.glob("D:/FYP Documents/Fyp coding Files/Video Croping/Runs/Fours"+"/*.mp4")
Path_Six_files= glob.glob("D:/FYP Documents/Fyp coding Files/Video Croping/Runs/Sixes"+"/*.mp4")
Path_Out_files= glob.glob("D:/FYP Documents/Fyp coding Files/Video Croping/Runs/Outs"+"/*.mp4")
Path_Events_files= glob.glob("D:/FYP Documents/Fyp coding Files/Video Croping/Runs/Events"+"/*.mp4")
  
new_list=[]  
for i in bestone:
    if i ==6:
        while True:
            temp=rd.choice(Path_Six_files)
            if temp not in new_list:
                new_list.append(temp)
                break
            else:
                continue
    elif i ==4:
        while True:
            temp=rd.choice(Path_Four_files)
            if temp not in new_list:
                new_list.append(temp)
                break
            else:
                continue
    if i ==0:
        while True:
            temp=rd.choice(Path_Out_files)
            if temp not in new_list:
                new_list.append(temp)
                break
            else:
                continue
    else:
        while True:
            temp=rd.choice(Path_Events_files)
            if temp not in new_list:
                new_list.append(temp)
                break
            else:
                continue
new_list1=[]            
for i in new_list:
    temp=i.split('\\')
    temp1=temp[1].split('_')
    new_list1.append([temp[0],int(temp1[0]),temp1[1]])

new_list1.sort(key = lambda new_list1: new_list1[1]) 

sample_list=[]
video_clip_list=[]
for i in new_list1:
    name=i[0]+str('\\')+str(i[1])+str('_')+str(i[2])
    sample_list.append(name)
    tempVideo=VideoFileClip(name)
    tempVideo.crossfadein(5.0) 
    video_clip_list.append(tempVideo)
print(sample_list)

slided_clips = [CompositeVideoClip([clip.fx( transfx.slide_out, 1, 'bottom')]) for clip in video_clip_list]
final_video= concatenate( slided_clips, padding=-1)
final_video.write_videofile("final_video.mp4")

'''


#%%
'''
import glob 
import natsort as nt

Path_Four_files= glob.glob("./Runs/Fours"+"/*.mp4")
Path_Six_files= glob.glob("./Runs/Sixes"+"/*.mp4")
Path_Out_files= glob.glob("./Runs/Outs"+"/*.mp4")
Path_Events_files= glob.glob("./Runs/Events"+"/*.mp4")

All_Filenames=[]

for i in Path_Four_files:
    All_Filenames.append(i)
for i in Path_Six_files:
    All_Filenames.append(i)
for i in Path_Out_files:
    All_Filenames.append(i)
for i in Path_Events_files:
    All_Filenames.append(i)

Delete_items=[]
for i in range(len(All_Filenames)):
    curr_file=All_Filenames[i].split('\\')
    curr_file=curr_file[1].split('_')
    curr_file=curr_file[0]
    for j in range(i+1,len(All_Filenames)):
        next_file=All_Filenames[j].split('\\')
        next_file=next_file[1].split('_')
        next_file=next_file[0]
        if int(curr_file)> int(next_file):
            #The above if else is used is curr_num is greater than next_num then it show be checked in that way
            if (int(curr_file)-int(next_file))<10 and All_Filenames[i] not in Delete_items:
                Delete_items.append(All_Filenames[i])
                Delete_items.append(All_Filenames[j])
                print('File i: ',All_Filenames[i],' File j: ',All_Filenames[j])
                
        else:
            
            if (int(next_file)-int(curr_file))<10 and All_Filenames[i] not in Delete_items:
                Delete_items.append(All_Filenames[i])
                Delete_items.append(All_Filenames[j])
                print('File i: ',All_Filenames[i],' File j: ',All_Filenames[j])
import os             
for (i,j) in zip(Delete_items,range(len(Delete_items))):
    if 'Events' in i:
        os.remove(i)
        Delete_items.pop(j)
        
print(Delete_items)
 
'''           
            
#%%
