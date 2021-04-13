import sys,time,os
import numpy as np
import pandas as pd
import webbrowser
import matplotlib.pyplot as plt
from csv import writer
from datetime import date,timedelta


global dff,dfm,dft,nop,dffg,dfmg,dftg,nop,graph_option,title_option
dff=pd.read_csv('finaldata.csv')
dfm=pd.read_csv('miscdata.csv')
dft=pd.read_csv('top10.csv')


#these are used for resetting the column names to default
dff_columns=list(dff.columns)
dft_columns=list(dft.columns)
dfm_columns=list(dfm.columns)


dff=dff.fillna(0)#replacing Nan values with zero
dff['total_cases']=dff['total_cases'].astype(int)#converting float(decimal) values to int
dff['total_deaths']=dff['total_deaths'].astype(int)#converting float(decimal) values to int
dft=dft.fillna(0)#replacing Nan values with zero
dft['new_cases']=dft['new_cases'].astype(int)#converting float(decimal) values to int
dft['new_deaths']=dft['new_deaths'].astype(int)#converting float(decimal) values to int
dfm=dfm.fillna(0)#float values are kept here

#following data is for graphs
dffg=dff.copy()
dfmg=dfm.copy()
dftg=dft.copy()

#used in visualisation loop for asking the user if he wants to save the graphs
nop=0

#for activation of project title animation
title_option=True

#for save fig of graphs
graph_option=None

dffg['total_cases'] = dffg['total_cases'].abs()
dffg['total_deaths'] = dffg['total_deaths'].abs()
dftg['new_cases'] = dftg['new_cases'].abs()#converting negative values into positive if any
dftg['new_deaths'] = dftg['new_deaths'].abs()#converting negative values into positive if any

for_top10=dffg.copy()
#converting date column values to dtype = datetime
dftg['date'] = pd.to_datetime(dftg['date'])
dftg.drop(dftg[dftg['date']<'3/11/2020'].index,inplace=True)#dropping some rows to match all the country data




#module for changing the title
def title():
    global qqq
    if title_op=='y' or title_op=='Y':#since this if is executed the elif statements wouldnt be executed
        qqq=input('Enter the title you want to give:')
    else:
        qqq=('Python Project')
    spaces()#new module has been created for better organiszation

#module for aligining the title of the project to the middle
def spaces():
    global i
    if len(qqq)>0 and len(qqq)<=2:
        i=('\t\t\t\t\t  一一一'+qqq+'一一一 ')
    elif len(qqq)>2 and len(qqq)<=4:
        i=('\t\t\t\t\t 一一一'+qqq+'一一一 ')
    elif len(qqq)>4 and len(qqq)<=6:
        i=('\t\t\t\t\t一一一'+qqq+'一一一 ')    
    elif len(qqq)>6 and len(qqq)<=8:
        i=('\t\t\t\t       一一一'+qqq+'一一一 ')
    elif len(qqq)>8 and len(qqq)<=10:
        i=('\t\t\t\t      一一一'+qqq+'一一一 ')
    elif len(qqq)>10 and len(qqq)<=12:
        i=('\t\t\t\t     一一一'+qqq+'一一一 ')
    elif len(qqq)>12 and len(qqq)<=14:
        i=('\t\t\t\t    一一一'+qqq+'一一一 ')
    elif len(qqq)>14 and len(qqq)<=16:
        i=('\t\t\t\t   一一一'+qqq+'一一一 ')
    elif len(qqq)>16 and len(qqq)<=18:
        i=('\t\t\t\t  一一一'+qqq+'一一一 ')
    elif len(qqq)>18 and len(qqq)<=20:
        i=('\t\t\t\t 一一一'+qqq+'一一一 ')
    elif len(qqq)>20 and len(qqq)<=22:
        i=('\t\t\t\t一一一'+qqq+'一一一 ')
    elif len(qqq)>22 and len(qqq)<=24:
        i=('\t\t\t       一一一'+qqq+'一一一 ')
    elif len(qqq)>24 and len(qqq)<=26:
        i=('\t\t\t      一一一'+qqq+'一一一 ')
    elif len(qqq)>26 and len(qqq)<=28:
        i=('\t\t\t     一一一'+qqq+'一一一 ')
    elif len(qqq)>28 and len(qqq)<=30:
        i=('\t\t\t    一一一'+qqq+'一一一 ')
    elif len(qqq)>30 and len(qqq)<=32:
        i=('\t\t\t   一一一'+qqq+'一一一 ')
    elif len(qqq)>32 and len(qqq)<=34:
        i=('\t\t\t  一一一'+qqq+'一一一 ')
    elif len(qqq)>34 and len(qqq)<=36:
        i=('\t\t\t 一一一'+qqq+'一一一 ')
    elif len(qqq)>36 and len(qqq)<=38:
        i=('\t\t\t一一一'+qqq+'一一一 ')
    elif len(qqq)>38 and len(qqq)<=40:
        i=('\t\t       一一一'+qqq+'一一一 ')
    elif len(qqq)>40 and len(qqq)<=42:
        i=('\t\t      一一一'+qqq+'一一一 ')
    elif len(qqq)>42 and len(qqq)<=44:
        i=('\t\t     一一一'+qqq+'一一一 ')
    elif len(qqq)>44 and len(qqq)<=46:
        i=('\t\t    一一一'+qqq+'一一一 ')
    elif len(qqq)>46 and len(qqq)<=48:
        i=('\t\t   一一一'+qqq+'一一一 ')
    elif len(qqq)>48 and len(qqq)<=50:
        i=('\t\t  一一一'+qqq+'一一一 ')
    elif len(qqq)>50 and len(qqq)<=52:
        i=('\t\t 一一一'+qqq+'一一一 ')
    elif len(qqq)>52 and len(qqq)<=54:
        i=('\t\t一一一'+qqq+'一一一 ')
    elif len(qqq)>54 and len(qqq)<=56:
        i=('\t       一一一'+qqq+'一一一 ')
    elif len(qqq)>56 and len(qqq)<=58:
        i=('\t      一一一'+qqq+'一一一 ')
    elif len(qqq)>58 and len(qqq)<=60:
        i=('\t     一一一'+qqq+'一一一 ')
    elif len(qqq)>60 and len(qqq)<=62:
        i=('\t    一一一'+qqq+'一一一 ')
    elif len(qqq)>62 and len(qqq)<=64:
        i=('\t   一一一'+qqq+'一一一 ')
    elif len(qqq)>64 and len(qqq)<=66:
        i=('\t  一一一'+qqq+'一一一 ')
    elif len(qqq)>66 and len(qqq)<=68:
        i=('\t 一一一'+qqq+'一一一 ')
    elif len(qqq)>68 and len(qqq)<=70:
        i=('\t一一一'+qqq+'一一一 ')
    elif len(qqq)>70 and len(qqq)<=72:
        i=('       一一一'+qqq+'一一一 ')
    elif len(qqq)>72 and len(qqq)<=74:
        i=('      一一一'+qqq+'一一一 ')
    elif len(qqq)>74 and len(qqq)<=76:
        i=('     一一一'+qqq+'一一一 ')
    elif len(qqq)>76 and len(qqq)<=78:
        i=('    一一一'+qqq+'一一一 ')
    elif len(qqq)>78 and len(qqq)<=80:
        i=('   一一一'+qqq+'一一一 ')
    elif len(qqq)>80 and len(qqq)<=82:
        i=('  一一一'+qqq+'一一一 ')
    elif len(qqq)>82 and len(qqq)<=84:
        i=(' 一一一'+qqq+'一一一 ')
    else:
        i=('一一一'+qqq+'一一一 ')

#asking user if he wants to give a title
title_op=input('Do you want to give a title? If no then default will be taken..y/n:')
title()


#Module for title animation
def typewriter(i):
    for char in i:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
os.system('cls')





##########Visualisation modules###########
def total_deaths_pie():
    #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
    plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
    
    for_top10 = dffg.copy()
    for_top10.sort_values('total_deaths',ascending=False,inplace=True)
    for_top10.reset_index(inplace=True)#reseting the index after deleting rows
    for_top10.drop('index',axis=1,inplace=True)#deleting the index column that was created after reseting the index
    
    qop=len(for_top10)#this has the total nunber of countries
    l=[]
    for qqq in range(qop-10):#the loop repeats 10 times less so it keeps the top 10 countries
        l.append(qqq+10)#this begins insert index from 11th country 
    
    
    for_top10.drop(l,inplace=True)#dropping the countries which are not in the top 10
    
    location=for_top10['location']
    deaths=for_top10['total_deaths']
    
    ll=for_top10['location']#assigning only the country names to ll
    lll=[]
    for q in range(10):
        lll.append(ll[q])
    
    explode=(0.15,0,0,0,0,0,0,0,0,0)
    #color=['#7cb0eb','#e4d354','#f15c80','#a87fba','#2bca74','#325cac','#b1bdd1','#418b64','#e7d19d','#4c4c54']#EASTER EGG
    color=['#000080','#0000f1','#004dff','#00b1ff','#29ffce','#7dff7a','#ceff29','#ffc400','#ff6800','#f10800']
    wp={'edgecolor':'#1b1e23','linewidth': 1,'linestyle': 'dashed', 'antialiased': True}#wedge properties
    plt.pie(deaths,explode=explode,labels=lll,shadow=True,colors=color,wedgeprops=wp)
    
    plt.title('Top 10 countries with Highest Deaths')

    print()
    we=input('The legend might overlap the pie chart. Do you want to show the legend? y/n:')
    if we=='y' or we=='Y':
        plt.legend()
    
    name='Top 10 countries with Highest Deaths'
    if saa=='a' or saa=='A':
        plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    elif saa=='b' or saa=='B':
        plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)

    plt.show()


def total_cases_pie():
    #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
    plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
    
    for_top10 = dffg.copy()
    for_top10.sort_values('total_cases',ascending=False,inplace=True)
    for_top10.reset_index(inplace=True)#reseting the index after deleting rows
    for_top10.drop('index',axis=1,inplace=True)#deleting the index column that was created after reseting the index
    
    qop=len(for_top10)#this has the total nunber of countries
    l=[]
    for qqq in range(qop-10):#the loop repeats 10 times less so it keeps the top 10 countries
        l.append(qqq+10)#this begins insert index from 11th country 
    
    
    for_top10.drop(l,inplace=True)#dropping the countries which are not in the top 10
    
    qqqq=for_top10['location']#assigning only the country names to qqqq
    location=for_top10['location']
    cases=for_top10['total_cases']
    
    ll=for_top10['location']#assigning only the country names to ll
    lll=[]
    for q in range(10):
        lll.append(ll[q])
    explode=(0.15,0,0,0,0,0,0,0,0,0)
    
    #color=['#7cb0eb','#e4d354','#f15c80','#a87fba','#2bca74','#325cac','#b1bdd1','#418b64','#e7d19d','#4c4c54']EASTER EGG
    color=['#000080','#0000f1','#004dff','#00b1ff','#29ffce','#7dff7a','#ceff29','#ffc400','#ff6800','#f10800']
    wp={'edgecolor':'#1b1e23','linewidth': 1,'linestyle': 'dashed', 'antialiased': True}#wedge properties
    plt.pie(cases,explode=explode,labels=lll,shadow=True,colors=color,wedgeprops=wp)
    
    plt.title('Top 10 countries with Highest Cases')
    
    print()
    we=input('The legend might overlap the pie chart. Do you want to show the legend? y/n:')
    if we=='y' or we=='Y':
        plt.legend()
    
    name='Top 10 countries with Highest Cases'
    if saa=='a' or saa=='A':
        plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    elif saa=='b' or saa=='B':
        plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)

    plt.show()






def dfmg_bar():
    #the following two lines are given to stop a warning which shows up right before displaying the graph
    import warnings
    warnings.filterwarnings("ignore")
    
    #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
    plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
    
    while True:
        print('a.Select and compare multiple columns')
        print('b.Compare Male and Female smokers')
        print('c.Compare Population')
        print('d.Compare Median age')
        print('e.Compare GDP')
        print('f.Compare Cardiovasc Death Rate')
        print('g.Compare Diabetes prevalence')
        print('h.Compare Handwashing Facilities')
        print('i.Compare Hospital beds per thousand')
        print('j.Compare Life Expectancy')
        print('k.Compare Human Development Index')
        print('l.Compare Male smokers')
        print('m.Compare Female smokers')
        print('n.Exit')
       
        w=input('Enter your selection here:')
        print()
        if w=='a' or w=='A':
            cn=int(input('Enter the number of column you want to compare [max 3]:'))
            print()
            #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
            plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
            plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)

            continent=dfmg['continent']
            location=dfmg['location']
            stringency_index=dfmg['stringency_index']
            population=dfmg['population']
            median_age=dfmg['median_age']
            gdp_per_capita=dfmg['gdp_per_capita']
            cardiovasc_death_rate=dfmg['cardiovasc_death_rate']
            diabetes_prevalence=dfmg['diabetes_prevalence']
            female_smokers=dfmg['female_smokers']
            life_expectancy=dfmg['life_expectancy']
            male_smokers=dfmg['male_smokers']
            handwashing_facilities=dfmg['handwashing_facilities']
            hospital_beds_per_thousand=dfmg['hospital_beds_per_thousand']
            life_expectancy=dfmg['life_expectancy']
            human_development_index=dfmg['human_development_index']

            #dividing the dataframe into 4 equal parts
            l= len(location.index)
            ll=l//4
            
            aq=['location']
            beth=dfmg.columns
            lll=[]#here we basically remove the column names to be kept from all the column names
            for ab in beth:
                if ab in aq:
                    continue
                else:
                    lll.append(ab)
            print('Columns:')
            print(lll)
            print()
            
            if cn==1:
                co1=input('Enter name of the column to be compared:')
                coll1=dfmg[co1]
                name=co1+' in different countries'
                l= len(location.index)
                ll=l//2
                
                location1=location.loc[:ll]
                location2=location.loc[ll:]
                
                d= len(location.index)
                dd=d//2
                col1=coll1.loc[:dd]
                col2=coll1.loc[dd:]

                plot1=plt.figure(1)
                
                #following three lines are given to prevent the printing of scientific values like '3.41e+06'
                plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
                plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
                plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
                
                plt.bar(location1,col1,label=co1,color='#8da0cb',edgecolor='k')
                plt.grid(color='grey',ls='-.',lw = 0.25)
                plt.legend()
                q=(co1+'\n[Country wise]')
                plt.title(q)
                plt.xlabel('Countries')
                plt.ylabel('Number of '+co1)
                plt.xticks(location1,rotation=90)
                if saa=='a' or saa=='A':
                    plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
                elif saa=='b' or saa=='B':
                    plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)

                
                plot2=plt.figure(2)
                
                #following three lines are given to prevent the printing of scientific values like '3.41e+06'
                plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
                plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
                plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
                
                plt.bar(location2,col2,label=co1,color='#8da0cb',edgecolor='k')
                plt.grid(color='grey',ls='-.',lw = 0.25)
                plt.legend()
                q=(co1+'\n[Country wise]')
                plt.title(q)
                plt.xlabel('Countries')
                plt.ylabel('Number of '+co1)
                plt.xticks(location2,rotation=90)
                if saa=='a' or saa=='A':
                    plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
                elif saa=='b' or saa=='B':
                    plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
                plt.show()


            if cn==2:
                co1=input('Enter name of the 1st column to be compared:')
                co2=input('Enter name of the 2nd column to be compared:')
                
                name=co1+''+co2+' in different countries'

                print()
                print('From the selected columns use data of:')
                print('a.First quarter')
                print('b.Second quarter')
                print('c.Third quarter')
                print('d.Fourth quarter')
                print('e.Manually enter start stop value')
                print('f.Select specific indices')
                op=input('Enter your selection:')
                print()
                col1=dfmg[co1]
                col2=dfmg[co2]
                if op=='a' or op=='A':
                    location=location.loc[:ll]
                    col1=col1.loc[:ll]
                    col2=col2.loc[:ll]
                    
                elif op=='b' or op=='B':
                    location=location.loc[ll:ll*2]
                    col1=col1.loc[ll:ll*2]
                    col2=col2.loc[ll:ll*2]
                    
                elif op=='c' or op=='C':
                    location=location.loc[ll*2:ll*3]
                    col1=col1.loc[ll*2:ll*3]
                    col2=col2.loc[ll*2:ll*3]
                    
                elif op=='d' or op=='D':
                    location=location.loc[ll*3:ll*4]
                    col1=col1.loc[ll*3:ll*4]
                    col2=col2.loc[ll*3:ll*4]
                    
                elif op=='e' or op=='E':
                    w=input('Would you like to print the country names & indices bfore selection?')
                    if w=='y' or w=='Y':
                        print(dfmg['location'])
                    print()
                    
                    start=int(input('Enter start value:'))
                    stop=int(input('Enter stop value:'))
                    
                    location=location.loc[start:stop]
                    col1=col1.loc[start:stop]
                    col2=col2.loc[start:stop]
                    
                elif op=='f' or op=='F':
                    w=input('Would you like to print the country names & indices bfore selection?')
                    if w=='y' or w=='Y':
                        print(dfmg['location'])
                    print()
                    ww=int(input('Enter the number of rows you want to select:'))
                    if ww==1:
                        ll=int(input('Enter index:'))
                    elif ww>1:
                        for qq in range(ww):
                            if qq+1==1:
                                qqq='st'
                            elif qq+1==2:
                                qqq='nd'
                            elif qq+1==3:
                                qqq='rd'
                            elif qq+1<=4:
                                qqq='th'
                            print('Enter the index of',str(qq+1)+qqq+' row to be used:')
                            n=int(input(''))
                            
                            if qq==0:
                                entry=location.loc[n:n]
                                locationf=entry#we do not concat since the df for concat isnt formed yet, therefore we insted assign it
                                entry=col1.loc[n:n]
                                col1f=entry
                                entry=col2.loc[n:n]
                                col2f=entry
                            else:
                                entry=location.loc[n:n]
                                locationf=pd.concat([locationf,entry],ignore_index=True)
                                entry=col1.loc[n:n]#since the df for concat is formed we can now start concatinating
                                col1f=pd.concat([col1f,entry],ignore_index=True)
                                entry=deaths.loc[n:n]
                                col2f=pd.concat([col2f,entry],ignore_index=True)
                    location=locationf
                    col1=col1f
                    col2s=col2f
                w=0.4
                
                bar1=np.arange(len(location))
                bar2=[x+w for x in bar1]
                
                plt.bar(bar1,col1,width=w,label=co1,color='#8da0cb',edgecolor='k')
                plt.bar(bar2,col2,width=w,label=co2,color='#fc8d62',edgecolor='k')
                
                plt.xlabel('Countries')
                plt.ylabel('Number of'+co1+' and '+co2)
                q=(co1+' and '+co2+'\n[Country wise]')
                plt.title(q)
                
                #plt.yticks(cases)
                if op=='f' or op=='F':
                    plt.xticks(bar1+w/2,location)
                else:
                    plt.xticks(bar1+w/2,location,rotation=90)

                
                plt.grid(color='grey',ls='-.',lw=0.25)
                plt.legend()
                if saa=='a' or saa=='A':
                    plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
                elif saa=='b' or saa=='B':
                    plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
                plt.show()
            
            elif cn==3:
                co1=input('Enter name of the 1st column to be compared:')
                co2=input('Enter name of the 2nd column to be compared:')
                co3=input('Enter name of the 3rd column to be compared:')
                
                name=co1+''+co2+''+co3+' in different countries'

                print()
                print('From the selected columns use data of:')
                print('a.First quarter')
                print('b.Second quarter')
                print('c.Third quarter')
                print('d.Fourth quarter')
                print('e.Manually enter start stop value')
                print('f.Select specific indices')
                op=input('Enter your selection:')
                print()
                col1=dfmg[co1]
                col2=dfmg[co2]
                col3=dfmg[co3]
                if op=='a' or op=='A':
                    location=location.loc[:ll]
                    col1=col1.loc[:ll]
                    col2=col2.loc[:ll]
                    col3=col3.loc[:ll]
                    
                elif op=='b' or op=='B':
                    location=location.loc[ll:ll*2]
                    col1=col1.loc[ll:ll*2]
                    col2=col2.loc[ll:ll*2]
                    col3=col3.loc[ll:ll*2]
                    
                elif op=='c' or op=='C':
                    location=location.loc[ll*2:ll*3]
                    col1=col1.loc[ll*2:ll*3]
                    col2=col2.loc[ll*2:ll*3]
                    col3=col3.loc[ll*2:ll*3]
                    
                elif op=='d' or op=='D':
                    location=location.loc[ll*3:ll*4]
                    col1=col1.loc[ll*3:ll*4]
                    col2=col2.loc[ll*3:ll*4]
                    col3=col3.loc[ll*3:ll*4]
                    
                elif op=='e' or op=='E':
                    w=input('Would you like to print the country names & indices bfore selection?')
                    if w=='y' or w=='Y':
                        print(dfmg['location'])
                    print()
                    
                    start=int(input('Enter start value:'))
                    stop=int(input('Enter stop value:'))
                    
                    location=location.loc[start:stop]
                    col1=col1.loc[start:stop]
                    col2=col2.loc[start:stop]
                    col3=col3.loc[start:stop]
                    
                elif op=='f' or op=='F':
                    w=input('Would you like to print the country names & indices bfore selection?')
                    if w=='y' or w=='Y':
                        print(dfmg['location'])
                    print()
                    ww=int(input('Enter the number of rows you want to select:'))
                    if ww==1:
                        ll=int(input('Enter index:'))
                    elif ww>1:
                        for qq in range(ww):
                            if qq+1==1:
                                qqq='st'
                            elif qq+1==2:
                                qqq='nd'
                            elif qq+1==3:
                                qqq='rd'
                            elif qq+1<=4:
                                qqq='th'
                            print('Enter the index of',str(qq+1)+qqq+' row to be used:')
                            n=int(input(''))
                            
                            if qq==0:
                                entry=location.loc[n:n]
                                locationf=entry#we do not concat since the df for concat isnt formed yet, therefore we insted assign it
                                entry=col1.loc[n:n]
                                col1f=entry
                                entry=col2.loc[n:n]
                                col2f=entry
                                entry=col3.loc[n:n]
                                col3f=entry
                            else:
                                entry=location.loc[n:n]
                                locationf=pd.concat([locationf,entry],ignore_index=True)
                                entry=col1.loc[n:n]#since the df for concat is formed we can now start concatinating
                                col1f=pd.concat([col1f,entry],ignore_index=True)
                                entry=col2.loc[n:n]
                                col2f=pd.concat([col2f,entry],ignore_index=True)
                                entry=col3.loc[n:n]
                                col3f=pd.concat([col3f,entry],ignore_index=True)
                    location=locationf
                    col1=col1f
                    col2=col2f
                    col3=col3f
                w=0.2
                
                bar1=np.arange(len(location))
                bar2=[x+w for x in bar1]
                bar3=[x+w for x in bar2]
                
                plt.bar(bar1,col1,width=w,label=co1,color='#8da0cb',edgecolor='k')
                plt.bar(bar2,col2,width=w,label=co2,color='#fc8d62',edgecolor='k')
                plt.bar(bar3,col3,width=w,label=co3,color='#66c2a5',edgecolor='k')
                
                plt.xlabel('Countries')
                plt.ylabel('Number of'+co1+' and '+co2)
                q=(co1+' & '+co2+' & '+co3+'\n[Country wise]')
                plt.title(q)
                
                #plt.yticks(cases)
                if op=='f' or op=='F':
                    plt.xticks(bar1+w,location)
                else:
                    plt.xticks(bar1+w,location,rotation=90)

                
                plt.grid(color='grey',ls='-.',lw=0.25)
                plt.legend()
                if saa=='a' or saa=='A':
                    plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
                elif saa=='b' or saa=='B':
                    plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
                plt.show()

        if w=='b' or w=='B':
            co1='male_smokers'
            co2='female_smokers'
            location=dfmg['location']
            name=co1+''+co2+' in different countries'
            
            #dividing the dataframe into 4 equal parts
            l= len(location.index)
            ll=l//4
            
            print()
            print('From the selected columns use data of:')
            print('a.First quarter')
            print('b.Second quarter')
            print('c.Third quarter')
            print('d.Fourth quarter')
            print('e.Manually enter start stop value')
            print('f.Select specific indices')
            op=input('Enter your selection:')
            print()
            col1=dfmg[co1]
            col2=dfmg[co2]
            if op=='a' or op=='A':
                location=location.loc[:ll]
                col1=col1.loc[:ll]
                col2=col2.loc[:ll]
                
            elif op=='b' or op=='B':
                location=location.loc[ll:ll*2]
                col1=col1.loc[ll:ll*2]
                col2=col2.loc[ll:ll*2]
                
            elif op=='c' or op=='C':
                location=location.loc[ll*2:ll*3]
                col1=col1.loc[ll*2:ll*3]
                col2=col2.loc[ll*2:ll*3]
                
            elif op=='d' or op=='D':
                location=location.loc[ll*3:ll*4]
                col1=col1.loc[ll*3:ll*4]
                col2=col2.loc[ll*3:ll*4]
                
            elif op=='e' or op=='E':
                w=input('Would you like to print the country names & indices bfore selection?')
                if w=='y' or w=='Y':
                    print(dfmg['location'])
                print()
                
                start=int(input('Enter start value:'))
                stop=int(input('Enter stop value:'))
                
                location=location.loc[start:stop]
                col1=col1.loc[start:stop]
                col2=col2.loc[start:stop]
                
            elif op=='f' or op=='F':
                w=input('Would you like to print the country names & indices bfore selection?')
                if w=='y' or w=='Y':
                    print(dfmg['location'])
                print()
                ww=int(input('Enter the number of rows you want to select:'))
                if ww==1:
                    ll=int(input('Enter index:'))
                elif ww>1:
                    for qq in range(ww):
                        if qq+1==1:
                            qqq='st'
                        elif qq+1==2:
                            qqq='nd'
                        elif qq+1==3:
                            qqq='rd'
                        elif qq+1<=4:
                            qqq='th'
                        print('Enter the index of',str(qq+1)+qqq+' row to be used:')
                        n=int(input(''))
                        
                        if qq==0:
                            entry=location.loc[n:n]
                            locationf=entry#we do not concat since the df for concat isnt formed yet, therefore we insted assign it
                            entry=col1.loc[n:n]
                            col1f=entry
                            entry=col2.loc[n:n]
                            col2f=entry
                        else:
                            entry=location.loc[n:n]
                            locationf=pd.concat([locationf,entry],ignore_index=True)
                            entry=col1.loc[n:n]#since the df for concat is formed we can now start concatinating
                            col1f=pd.concat([col1f,entry],ignore_index=True)
                            entry=deaths.loc[n:n]
                            col2f=pd.concat([col2f,entry],ignore_index=True)
                location=locationf
                col1=col1f
                col2s=col2f
            w=0.4
            
            bar1=np.arange(len(location))
            bar2=[x+w for x in bar1]
            
            plt.bar(bar1,col1,width=w,label=co1,color='#8da0cb',edgecolor='k')
            plt.bar(bar2,col2,width=w,label=co2,color='#fc8d62',edgecolor='k')
            
            plt.xlabel('Countries')
            plt.ylabel('Number of'+co1+' and '+co2)
            q=(co1+' and '+co2+'\n[Country wise]')
            plt.title(q)
            
            #plt.yticks(cases)
            if op=='f' or op=='F':
                plt.xticks(bar1+w/2,location)
            else:
                plt.xticks(bar1+w/2,location,rotation=90)
            
            
            plt.grid(color='grey',ls='-.',lw=0.25)
            plt.legend()
            if saa=='a' or saa=='A':
                plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
            elif saa=='b' or saa=='B':
                plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
            plt.show()

        if w=='c' or w=='C' or w=='d' or w=='D' or w=='e' or w=='E' or w=='f' or w=='F' or w=='g' or w=='G' or w=='h'\
            or w=='H' or w=='i' or w=='I' or w=='j' or w=='J' or w=='k' or w=='K' or w=='l' or w=='L' or w=='m' or w=='M':
            if w=='c' or w=='C':
                co1='population'
            elif w=='d' or w=='D':
                co1='median_age'
            elif w=='e' or w=='E':
                co1='gdp_per_capita'
            elif w=='f' or w=='F':
                co1='cardiovasc_death_rate'
            elif w=='g' or w=='G':
                co1='diabetes_prevalence'
            elif w=='h' or w=='H':
                co1='handwashing_facilities'
            elif w=='i' or w=='I':
                co1='hospital_beds_per_thousand'
            elif w=='j' or w=='J':
                co1='life_expectancy'
            elif w=='k' or w=='K':
                co1='human_development_index'
            elif w=='l' or w=='L':
                co1='male_smokers'
            elif w=='m' or w=='M':
                co1='female_smokers'
            
            location=dfmg['location']
            
            coll1=dfmg[co1]
            name=co1+' in different countries'
            l= len(location.index)
            ll=l//2
            
            location1=location.loc[:ll]
            location2=location.loc[ll:]
            
            d= len(location.index)
            dd=d//2
            col1=coll1.loc[:dd]
            col2=coll1.loc[dd:]
            
            plot1=plt.figure(1)
            #following three lines are given to prevent the printing of scientific values like '3.41e+06'
            plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
            plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
            plt.bar(location1,col1,label=co1,color='#8da0cb',edgecolor='k')
            plt.grid(color='grey',ls='-.',lw = 0.25)
            plt.legend()
            q=(co1+'\n[Country wise]')
            plt.title(q)
            plt.xlabel('Countries')
            plt.ylabel('Number of '+co1)
            plt.xticks(location1,rotation=90)
            if saa=='a' or saa=='A':
                plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
            elif saa=='b' or saa=='B':
                plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
            
            plot2=plt.figure(2)
            #following three lines are given to prevent the printing of scientific values like '3.41e+06'
            plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
            plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
            plt.bar(location2,col2,label=co1,color='#8da0cb',edgecolor='k')
            plt.grid(color='grey',ls='-.',lw = 0.25)
            plt.legend()
            q=(co1+'\n[Country wise]')
            plt.title(q)
            plt.xlabel('Countries')
            plt.ylabel('Number of '+co1)
            plt.xticks(location2,rotation=90)
            if saa=='a' or saa=='A':
                plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
            elif saa=='b' or saa=='B':
                plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
            plt.show()
        if w=='n' or w=='N':
            visualisation()





def trends_deaths_countries():
    for_top10 = dffg.copy()
    for_top10.sort_values('total_cases',ascending=False,inplace=True)
    for_top10.reset_index(inplace=True)#reseting the index after deleting rows
    for_top10.drop('index',axis=1,inplace=True)#deleting the index column that was created after reseting the index
    
    #extracting names of top 10 countries automatically
    ll=for_top10['location']#assigning only the country names to ll
    c1=ll[0] #first country
    c2=ll[1] #second country
    c3=ll[2] #third country
    c4=ll[3] #forth country
    c5=ll[4] #fifth country
    c6=ll[5] #sixth country
    c7=ll[6] #seventh country
    c8=ll[7] #eigth country
    c9=ll[8] #ninth country
    c10=ll[9] #tenth country
    
    #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
    plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
        
    #deaths data of various countries for y axis
    cc1=dftg.loc[dftg['location']==c1,['new_deaths']]
    cc2=dftg.loc[dftg['location']==c2,['new_deaths']]
    cc3=dftg.loc[dftg['location']==c3,['new_deaths']]
    cc4=dftg.loc[dftg['location']==c4,['new_deaths']]
    cc5=dftg.loc[dftg['location']==c5,['new_deaths']]
    cc6=dftg.loc[dftg['location']==c6,['new_deaths']]
    cc7=dftg.loc[dftg['location']==c7,['new_deaths']]
    cc8=dftg.loc[dftg['location']==c8,['new_deaths']]
    cc9=dftg.loc[dftg['location']==c9,['new_deaths']]
    cc10=dftg.loc[dftg['location']==c10,['new_deaths']]
    
    #date data for x axis
    dd1=dftg.loc[dftg['location']==c1,['date']]
    
    print('a.Select specific countries')
    print('b.All top 10 countries')
    w=input('Enter your option:')
    print()
    if w=='a' or w=='A':
        print('Top 10 countries:')
        print('',c1,'\n',c2,'\n',c3,'\n',c4,'\n',c5,'\n',c6,'\n',c7,'\n',c8,'\n',c9,'\n',c10)
        print()
        try:
            ww=int(input('Enter the number of countries you want to select:'))
        except:
            print()
            print('Invalid input')
            sys.exit()
        if ww>=1:#give just for 1 ccountry to be asked as enter name of the country instead of first country
            if ww==1:
                www=input('Enter name of the country:')
                name='Death trends in '+www
                plt.xlabel('Country')
            else:
                www=input('Enter name of the first country:')
                plt.xlabel('Countries')
                name='Death trends in top '+str(ww)+' countries'
            cc1=dftg.loc[dftg['location']==www,['new_deaths']]
            plt.plot(dd1,cc1,label=www)
            if ww>=2:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                www=input('Enter name of the second country:')
                cc1=dftg.loc[dftg['location']==www,['new_deaths']]
                plt.plot(dd1,cc1,label=www)
                if ww>=3:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                    www=input('Enter name of the third country:')
                    cc1=dftg.loc[dftg['location']==www,['new_deaths']]
                    plt.plot(dd1,cc1,label=www,linestyle='-.')
                    if ww>=4:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                        www=input('Enter name of the forth country:')
                        cc1=dftg.loc[dftg['location']==www,['new_deaths']]
                        plt.plot(dd1,cc1,label=www)
                        if ww>=5:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                            www=input('Enter name of the fifth country:')
                            cc1=dftg.loc[dftg['location']==www,['new_deaths']]
                            plt.plot(dd1,cc1,label=www)
                            if ww>=6:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                                www=input('Enter name of the sixth country:')
                                cc1=dftg.loc[dftg['location']==www,['new_deaths']]
                                plt.plot(dd1,cc1,label=www)
                                if ww>=7:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                                    www=input('Enter name of the seventh country:')
                                    cc1=dftg.loc[dftg['location']==www,['new_deaths']]
                                    plt.plot(dd1,cc1,label=www)
                                    if ww>=8:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                                        www=input('Enter name of the eigth country:')
                                        cc1=dftg.loc[dftg['location']==www,['new_deaths']]
                                        plt.plot(dd1,cc1,label=www)
                                        if ww>=9:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                                            www=input('Enter name of the ninth country:')
                                            cc1=dftg.loc[dftg['location']==www,['new_deaths']]
                                            plt.plot(dd1,cc1,label=www)
                                            if ww>=10:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                                                www=input('Enter name of the tenth country:')
                                                cc1=dftg.loc[dftg['location']==www,['new_deaths']]
                                                plt.plot(dd1,cc1,label=www)
    elif w=='b' or w=='B':
        name='Death trends in Top10 countries'
        ll=for_top10['location']#assigning only the country names to ll
        c1=ll[0] #first country
        c2=ll[1] #second country
        c3=ll[2] #third country
        c4=ll[3] #forth country
        c5=ll[4] #fifth country
        c6=ll[5] #sixth country
        c7=ll[6] #seventh country
        c8=ll[7] #eigth country
        c9=ll[8] #ninth country
        c10=ll[9] #tenth country
        
        #deaths data of various countries for y axis
        cc1=dftg.loc[dftg['location']==c1,['new_deaths']]
        cc2=dftg.loc[dftg['location']==c2,['new_deaths']]
        cc3=dftg.loc[dftg['location']==c3,['new_deaths']]
        cc4=dftg.loc[dftg['location']==c4,['new_deaths']]
        cc5=dftg.loc[dftg['location']==c5,['new_deaths']]
        cc6=dftg.loc[dftg['location']==c6,['new_deaths']]
        cc7=dftg.loc[dftg['location']==c7,['new_deaths']]
        cc8=dftg.loc[dftg['location']==c8,['new_deaths']]
        cc9=dftg.loc[dftg['location']==c9,['new_deaths']]
        cc10=dftg.loc[dftg['location']==c10,['new_deaths']]
        
        #date data for x axis
        dd1=dftg.loc[dftg['location']==c1,['date']]
        dd2=dftg.loc[dftg['location']==c2,['date']]
        dd3=dftg.loc[dftg['location']==c3,['date']]
        dd4=dftg.loc[dftg['location']==c4,['date']]
        dd5=dftg.loc[dftg['location']==c5,['date']]
        dd6=dftg.loc[dftg['location']==c6,['date']]
        dd7=dftg.loc[dftg['location']==c7,['date']]
        dd8=dftg.loc[dftg['location']==c8,['date']]
        dd9=dftg.loc[dftg['location']==c9,['date']]
        dd10=dftg.loc[dftg['location']==c10,['date']]
        
        
        plt.plot(dd1,cc1,label=c1)
        plt.plot(dd2,cc2,label=c2)
        plt.plot(dd3,cc3,label=c3)
        plt.plot(dd4,cc4,label=c4)
        plt.plot(dd5,cc5,label=c5)
        plt.plot(dd6,cc6,label=c6)
        plt.plot(dd7,cc7,label=c7)
        plt.plot(dd8,cc8,label=c8)
        plt.plot(dd9,cc9,label=c9)
        plt.plot(dd10,cc10,label=c10)
        
        plt.xlabel('Countries')
    
    
    plt.grid(color='grey',ls='-.',lw=0.25)
    plt.ylabel('Number of deaths')
    plt.title('Trend of deaths due to Covid-19')
    plt.legend()
    
    if saa=='a' or saa=='A':
        plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    elif saa=='b' or saa=='B':
        plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    
    plt.show()





def trends_cases_countries():
    for_top10 = dffg.copy()
    for_top10.sort_values('total_cases',ascending=False,inplace=True)
    for_top10.reset_index(inplace=True)#reseting the index after deleting rows
    for_top10.drop('index',axis=1,inplace=True)#deleting the index column that was created after reseting the index
        
    #extracting names of top 10 countries automatically
    ll=for_top10['location']#assigning only the country names to ll
    c1=ll[0] #first country
    c2=ll[1] #second country
    c3=ll[2] #third country
    c4=ll[3] #forth country
    c5=ll[4] #fifth country
    c6=ll[5] #sixth country
    c7=ll[6] #seventh country
    c8=ll[7] #eigth country
    c9=ll[8] #ninth country
    c10=ll[9] #tenth country
    
    #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
    plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
    
    #cases data of various countries for y axis
    cc1=dftg.loc[dftg['location']==c1,['new_cases']]
    cc2=dftg.loc[dftg['location']==c2,['new_cases']]
    cc3=dftg.loc[dftg['location']==c3,['new_cases']]
    cc4=dftg.loc[dftg['location']==c4,['new_cases']]
    cc5=dftg.loc[dftg['location']==c5,['new_cases']]
    cc6=dftg.loc[dftg['location']==c6,['new_cases']]
    cc7=dftg.loc[dftg['location']==c7,['new_cases']]
    cc8=dftg.loc[dftg['location']==c8,['new_cases']]
    cc9=dftg.loc[dftg['location']==c9,['new_cases']]
    cc10=dftg.loc[dftg['location']==c10,['new_cases']]
    
    #date data for x axis
    dd1=dftg.loc[dftg['location']==c1,['date']]
    
    print('a.Select specific countries')
    print('b.All top 10 countries')
    w=input('Enter your option:')
    print()
    if w=='a' or w=='A':
        print('Top 10 countries:')
        print('',c1,'\n',c2,'\n',c3,'\n',c4,'\n',c5,'\n',c6,'\n',c7,'\n',c8,'\n',c9,'\n',c10)
        print()
        try:
            ww=int(input('Enter the number of countries you want to select:'))
        except:
            print()
            print('Invalid input')
            sys.exit()
        if ww>=1:#give just for 1 ccountry to be asked as enter name of the country instead of first country
            name='Case trends in specific countries'
            if ww==1:
                www=input('Enter name of the country:')
                plt.xlabel('Country')
            else:
                www=input('Enter name of the first country:')
                plt.xlabel('Countries')
            cc1=dftg.loc[dftg['location']==www,['new_cases']]
            plt.plot(dd1,cc1,label=www)
            if ww>=2:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                www=input('Enter name of the second country:')
                cc1=dftg.loc[dftg['location']==www,['new_cases']]
                plt.plot(dd1,cc1,label=www)
                if ww>=3:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                    www=input('Enter name of the third country:')
                    cc1=dftg.loc[dftg['location']==www,['new_cases']]
                    plt.plot(dd1,cc1,label=www,linestyle='-.')
                    if ww>=4:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                        www=input('Enter name of the forth country:')
                        cc1=dftg.loc[dftg['location']==www,['new_cases']]
                        plt.plot(dd1,cc1,label=www)
                        if ww>=5:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                            www=input('Enter name of the fifth country:')
                            cc1=dftg.loc[dftg['location']==www,['new_cases']]
                            plt.plot(dd1,cc1,label=www)
                            if ww>=6:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                                www=input('Enter name of the sixth country:')
                                cc1=dftg.loc[dftg['location']==www,['new_cases']]
                                plt.plot(dd1,cc1,label=www)
                                if ww>=7:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                                    www=input('Enter name of the seventh country:')
                                    cc1=dftg.loc[dftg['location']==www,['new_cases']]
                                    plt.plot(dd1,cc1,label=www)
                                    if ww>=8:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                                        www=input('Enter name of the eigth country:')
                                        cc1=dftg.loc[dftg['location']==www,['new_cases']]
                                        plt.plot(dd1,cc1,label=www)
                                        if ww>=9:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                                            www=input('Enter name of the ninth country:')
                                            cc1=dftg.loc[dftg['location']==www,['new_cases']]
                                            plt.plot(dd1,cc1,label=www)
                                            if ww>=10:#give just for 1 ccountry to be asked as enter name of the country instead of first country
                                                www=input('Enter name of the tenth country:')
                                                cc1=dftg.loc[dftg['location']==www,['new_cases']]
                                                plt.plot(dd1,cc1,label=www)
    elif w=='b' or w=='B':
        name='Case trends in Top10 countries'
        ll=for_top10['location']#assigning only the country names to ll
        c1=ll[0] #first country
        c2=ll[1] #second country
        c3=ll[2] #third country
        c4=ll[3] #forth country
        c5=ll[4] #fifth country
        c6=ll[5] #sixth country
        c7=ll[6] #seventh country
        c8=ll[7] #eigth country
        c9=ll[8] #ninth country
        c10=ll[9] #tenth country
        
        #cases data of various countries for y axis
        cc1=dftg.loc[dftg['location']==c1,['new_cases']]
        cc2=dftg.loc[dftg['location']==c2,['new_cases']]
        cc3=dftg.loc[dftg['location']==c3,['new_cases']]
        cc4=dftg.loc[dftg['location']==c4,['new_cases']]
        cc5=dftg.loc[dftg['location']==c5,['new_cases']]
        cc6=dftg.loc[dftg['location']==c6,['new_cases']]
        cc7=dftg.loc[dftg['location']==c7,['new_cases']]
        cc8=dftg.loc[dftg['location']==c8,['new_cases']]
        cc9=dftg.loc[dftg['location']==c9,['new_cases']]
        cc10=dftg.loc[dftg['location']==c10,['new_cases']]
        
        #date data for x axis
        dd1=dftg.loc[dftg['location']==c1,['date']]
        dd2=dftg.loc[dftg['location']==c2,['date']]
        dd3=dftg.loc[dftg['location']==c3,['date']]
        dd4=dftg.loc[dftg['location']==c4,['date']]
        dd5=dftg.loc[dftg['location']==c5,['date']]
        dd6=dftg.loc[dftg['location']==c6,['date']]
        dd7=dftg.loc[dftg['location']==c7,['date']]
        dd8=dftg.loc[dftg['location']==c8,['date']]
        dd9=dftg.loc[dftg['location']==c9,['date']]
        dd10=dftg.loc[dftg['location']==c10,['date']]
        
        plt.plot(dd1,cc1,label=c1)
        plt.plot(dd2,cc2,label=c2)
        plt.plot(dd3,cc3,label=c3)
        plt.plot(dd4,cc4,label=c4)
        plt.plot(dd5,cc5,label=c5)
        plt.plot(dd6,cc6,label=c6)
        plt.plot(dd7,cc7,label=c7)
        plt.plot(dd8,cc8,label=c8)
        plt.plot(dd9,cc9,label=c9)
        plt.plot(dd10,cc10,label=c10)
        
    
    
    plt.grid(color='grey',ls='-.',lw=0.25)
    plt.ylabel('Number of Cases')
    plt.title('Trend of Cases due to Covid-19')
    plt.legend()
    
    if saa=='a' or saa=='A':
        plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    elif saa=='b' or saa=='B':
        plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    
    plt.show()




def cases_vs_deaths_country_bar():
    #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
    plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
    
    name='Deaths and Cases Country wise'
    
    location=dffg['location']
    deaths=dffg['total_deaths']
    cases=dffg['total_cases']
    
    #dividing the dataframe into 4 equal parts
    l= len(location.index)
    ll=l//4
    
    print('Select on which rows do you want the graph to be shown.')
    print('a.First quarter')
    print('b.Second quarter')
    print('c.Third quarter')
    print('d.Fourth quarter')
    print('e.Manually enter start stop value')
    print('f.Select specific indices')
    op=input('Enter your selection:')
    print()
    
    if op=='a' or op=='A':
        location=location.loc[:ll]
        cases=cases.loc[:ll]
        deaths=deaths.loc[:ll]
        
    elif op=='b' or op=='B':
        location=location.loc[ll:ll*2]
        deaths=deaths.loc[ll:ll*2]
        cases=cases.loc[ll:ll*2]
        
    elif op=='c' or op=='C':
        location=location.loc[ll*2:ll*3]
        deaths=deaths.loc[ll*2:ll*3]
        cases=cases.loc[ll*2:ll*3]
        
    elif op=='d' or op=='D':
        location=location.loc[ll*3:ll*4]
        deaths=deaths.loc[ll*3:ll*4]
        cases=cases.loc[ll*3:ll*4]
        
    elif op=='e' or op=='E':
        start=int(input('Enter start value:'))
        stop=int(input('Enter stop value:'))
        location=location.loc[start:stop]
        deaths=deaths.loc[start:stop]
        cases=cases.loc[start:stop]
        
    elif op=='f' or op=='F':
        rot=999
        w=input('Would you like to print the country names & indices bfore selection?')
        if w=='y' or w=='Y':
            print(dffg['location'])
        print()
        ww=int(input('Enter the number of rows you want to select:'))
        if ww==1:
            ll=int(input('Enter index:'))
        elif ww>1:
            for qq in range(ww):
                if qq+1==1:
                    qqq='st'
                elif qq+1==2:
                    qqq='nd'
                elif qq+1==3:
                    qqq='rd'
                elif qq+1<=4:
                    qqq='th'
                print('Enter the index of',str(qq+1)+qqq+' row to be used:')
                n=int(input(''))
                
                if qq==0:
                    entry=location.loc[n:n]
                    locationf=entry#we do not concat since the df for concat isnt formed yet, therefore we insted assign it
                    entry=cases.loc[n:n]
                    casesf=entry
                    entry=deaths.loc[n:n]
                    deathsf=entry
                else:
                    entry=location.loc[n:n]
                    locationf=pd.concat([locationf,entry],ignore_index=True)
                    entry=cases.loc[n:n]#since the df for concat is formed we can now start concatinating
                    casesf=pd.concat([casesf,entry],ignore_index=True)
                    entry=deaths.loc[n:n]
                    deathsf=pd.concat([deathsf,entry],ignore_index=True)
        location=locationf
        cases=casesf
        deaths=deathsf
        
    w=0.4
    
    bar1=np.arange(len(location))
    bar2=[x+w for x in bar1]
    
    plt.bar(bar1,cases,width=w,label='Cases',color='#8da0cb',edgecolor='k')
    plt.bar(bar2,deaths,width=w,label='Deaths',color='#fc8d62',edgecolor='k')
    
    plt.xlabel('Countries')
    plt.ylabel('Number of Cases & deaths')
    plt.title('Cases and Deaths\n[Country wise]')
    
    #plt.yticks(cases)
    if op=='f' or op=='F':
        plt.xticks(bar1+w/2,location)
    else:
        plt.xticks(bar1+w/2,location,rotation=90)
    
    
    plt.grid(color='grey',ls='-.',lw=0.25)
    plt.legend()
    
    if saa=='a' or saa=='A':
        plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    elif saa=='b' or saa=='B':
        plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    
    plt.show()






def cases_vs_deaths_continent_bar():
    w=0.4
    name='Cases and Deaths Continent wise'
    continent=dffg['continent']
    cases=dffg['total_cases']
    deaths=dffg['total_deaths']
    
    continent=['Asia','Europe','Africa','North America','South America','Oceania']
    bar1=np.arange(len(continent))
    bar2=[x+w for x in bar1]
    
    #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
    plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
        
    asia=dffg.loc[dffg['continent']=='Asia','total_cases'].sum()
    europe=dffg.loc[dffg['continent']=='Europe','total_cases'].sum()
    africa=dffg.loc[dffg['continent']=='Africa','total_cases'].sum()
    north_america=dffg.loc[dffg['continent']=='North America','total_cases'].sum()
    south_america=dffg.loc[dffg['continent']=='South America','total_cases'].sum()
    oceania=dffg.loc[dffg['continent']=='Oceania','total_cases'].sum()
    cases=[asia,europe,africa,north_america,south_america,oceania]
    
    asia=dffg.loc[dffg['continent']=='Asia','total_deaths'].sum()
    europe=dffg.loc[dffg['continent']=='Europe','total_deaths'].sum()
    africa=dffg.loc[dffg['continent']=='Africa','total_deaths'].sum()
    north_america=dffg.loc[dffg['continent']=='North America','total_deaths'].sum()
    south_america=dffg.loc[dffg['continent']=='South America','total_deaths'].sum()
    oceania=dffg.loc[dffg['continent']=='Oceania','total_deaths'].sum()
    deaths=[asia,europe,africa,north_america,south_america,oceania]
    
    plt.bar(bar1,cases,width=w,label='Cases',color='#8da0cb',edgecolor='k')
    plt.bar(bar2,deaths,width=w,label='Deaths',color='#fc8d62',edgecolor='k')

    plt.xlabel('Continents')
    plt.ylabel('Number of Cases & deaths')
    plt.title('Cases and Deaths\n[Continent wise]')
    plt.yticks(cases)
    plt.xticks(bar1+w/2,continent)
    plt.grid(color='grey',ls='-.',lw = 0.25)
    plt.legend()
    
    if saa=='a' or saa=='A':
        plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    elif saa=='b' or saa=='B':
        plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    
    plt.show()






def total_cases_continent_bar():
    name='Total Cases Continent wise'
    continent=dffg['continent']
    cases=dffg['total_cases']
    
    #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
    plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
        
    asia=dffg.loc[dffg['continent']=='Asia','total_cases'].sum()
    europe=dffg.loc[dffg['continent']=='Europe','total_cases'].sum()
    africa=dffg.loc[dffg['continent']=='Africa','total_cases'].sum()
    north_america=dffg.loc[dffg['continent']=='North America','total_cases'].sum()
    south_america=dffg.loc[dffg['continent']=='South America','total_cases'].sum()
    oceania=dffg.loc[dffg['continent']=='Oceania','total_cases'].sum()
    
    continent=['Asia','Europe','Africa','North America','South America','Oceania']
    cases=[asia,europe,africa,north_america,south_america,oceania]
    
    #bmap = brewer2mpl.get_map('Set2','qualitative',3,reverse=True)
    #color = bmap.mpl_colors
    plt.grid(color='grey',ls='-.',lw = 0.25)
    plt.bar(continent,cases,label='Cases',color=['#8da0cb','#fc8d62','#66c2a5','#8da0cb','#fc8d62','#66c2a5'],edgecolor='k')
    
    #yticks shows the exact number of cases
    plt.yticks(cases)#disable this to show even values
    
    plt.title('Cases\n[Continent wise]')
    plt.xlabel('Continents')
    plt.ylabel('Number of Cases\n[Continent wise]')
    
    if saa=='a' or saa=='A':
        plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    elif saa=='b' or saa=='B':
        plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    
    plt.show()






def total_deaths_continent_bar():
    name='Total Deaths Continent wise'
    #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
    plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
    
    continent=dffg['continent']
    deaths=dffg['total_deaths']
    
    asia=dffg.loc[dffg['continent']=='Asia','total_deaths'].sum()
    europe=dffg.loc[dffg['continent']=='Europe','total_deaths'].sum()
    africa=dffg.loc[dffg['continent']=='Africa','total_deaths'].sum()
    north_america=dffg.loc[dffg['continent']=='North America','total_deaths'].sum()
    south_america=dffg.loc[dffg['continent']=='South America','total_deaths'].sum()
    oceania=dffg.loc[dffg['continent']=='Oceania','total_deaths'].sum()
    
    continent=['Asia','Europe','Africa','North America','South America','Oceania']
    deaths=[asia,europe,africa,north_america,south_america,oceania]
    
    plt.bar(continent,deaths,label='Deaths',color=['#8da0cb','#fc8d62','#66c2a5','#8da0cb','#fc8d62','#66c2a5'],edgecolor='k')

    #yticks shows the exact number of cases
    #plt.yticks(continent)#disable this to show even values

    #plt.legend()
    plt.grid(color='grey',ls='-.',lw = 0.25)
    plt.title('Deaths\n[Continent wise]')
    plt.xlabel('Continents')
    plt.ylabel('Number of deaths')

    if saa=='a' or saa=='A':
        plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    elif saa=='b' or saa=='B':
        plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)

    plt.show()






def total_deaths_country_bar():
    #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
    plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
    
    name='Total Deaths Country wise'
    
    location=dffg['location']
    deaths=dffg['total_deaths']
    
    l= len(location.index)
    ll=l//2
    location1=location.loc[:ll]
    location2=location.loc[ll:]
    
    d= len(location.index)
    dd=d//2
    deaths1=deaths.loc[:dd]
    deaths2=deaths.loc[dd:]
    
    plot1=plt.figure(1)
    plt.bar(location1,deaths1,label='Deaths',color='lightcoral',edgecolor='darkred')
    plt.grid(color='grey',ls='-.',lw = 0.25)
    plt.legend()
    plt.title('Deaths\n[Country wise]')
    plt.xlabel('Countries')
    plt.ylabel('Number of deaths')
    plt.xticks(location1,rotation=90)
    #plt.yticks(deaths)
    
    plot2=plt.figure(2)
    plt.bar(location2,deaths2,label='Deaths',color='lightcoral',edgecolor='darkred')
    plt.grid(color='grey',ls='-.',lw = 0.25)
    plt.legend()
    plt.title('Deaths\n[Country wise]')
    plt.xlabel('Countries')
    plt.ylabel('Number of deaths')
    plt.xticks(location2,rotation=90)
    #plt.yticks(deaths)
    
    if saa=='a' or saa=='A':
        plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    elif saa=='b' or saa=='B':
        plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    
    plt.show()






def total_cases_country_bar():
    name='Total Cases Country wise'
    location=dffg['location']
    cases=dffg['total_cases']
    l= len(location.index)
    ll=l//2

    location1=location.loc[:ll]
    location2=location.loc[ll:]
    y=dffg['total_cases']
    q=max(y)
    yy=[]
    for yn in range(0,q+1,1000000):
        yy.append(yn)
    c= len(location.index)
    cc=c//2
    
    cases1=cases.loc[:cc]
    cases2=cases.loc[cc:]
    
    plot1 = plt.figure(1)
    
    #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
    plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
    
    plt.bar(location1,cases1,label='Cases',color='paleturquoise',width=0.85,edgecolor='darkcyan')
    plt.grid(color='grey',ls='-.',lw = 0.25)
    plt.legend()
    plt.title('Cases\n[Country wise]')
    plt.xlabel('Countries')
    plt.ylabel('Number of cases')
    plt.xticks(location1,rotation=90)
    plt.yticks(yy)
    
    if saa=='a' or saa=='A':
        plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    elif saa=='b' or saa=='B':
        plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    
    
    plot2 = plt.figure(2)
    #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
    plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
    plt.bar(location2,cases2,label='Cases',color='paleturquoise',width=0.85,edgecolor='darkcyan')
    plt.grid(color='grey',ls='-.',lw = 0.25)
    plt.legend()
    plt.title('Cases\n[Country wise]')
    plt.xlabel('Countries')
    plt.ylabel('Number of cases')
    plt.xticks(location2,rotation=90)
    plt.yticks(yy)
    if saa=='a' or saa=='A':
        plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    elif saa=='b' or saa=='B':
        plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    
    plt.show()



def countries_under_cases_hist():
    location=dffg['location']
    cases=dffg['total_cases']
    print()
    print('a.Pass custom bins')
    print('b.Take default bins [cases below 50000]')
    bi=input('Enter your selection:')
    if bi=='a' or bi=='A':
        print()
        n=int(input('Enter the number of bins you want to pass:'))
        print()
        l=[]
        for qq in range(n):
            if qq+1==1:
                qqq='st'
            elif qq+1==2:
                qqq='nd'
            elif qq+1==3:
                qqq='rd'
            elif qq+1<=4:
                qqq='th'
            print('Enter the',str(qq+1)+qqq+' bin below:')
            qq=int(input(''))
            l.append(qq)
            bins=l
    else:
        bins=[]
        a=50000
        s=a//20
        for q in range(0,a+1,s):
            bins.append(q)
    try:
        ls=(len(cases)//2)
        cases=cases[:ls]
        
        #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
        plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
        plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
        plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
        
        plt.hist(cases,bins=bins,color=['#66c2a5'],edgecolor='k')
        plt.xticks(bins)
        plt.title('Number of Countries under specific number of Cases')
        plt.xlabel('Number of Cases')
        plt.ylabel('Number of Countries')
        plt.grid(color='grey',ls='-.',lw=0.35)
        name='Number of Countries under specific number of Cases'
        if saa=='a' or saa=='A':
            plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
        elif saa=='b' or saa=='B':
            plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
        
        plt.show()
        
    except:
        print()
        print('ERROR.')
        print('Bins passed should be constant e.g.40 60 80 100...')


def countries_under_deaths_hist():
    location=dffg['location']
    deaths=dffg['total_deaths']
    print()
    print('a.Pass custom bins')
    print('b.Take default bins [deaths below 25000]')
    bi=input('Enter your selection:')
    if bi=='a' or bi=='A':
        print()
        n=int(input('Enter the number of bins you want to pass:'))
        print()
        l=[]
        for qq in range(n):
            if qq+1==1:
                qqq='st'
            elif qq+1==2:
                qqq='nd'
            elif qq+1==3:
                qqq='rd'
            elif qq+1<=4:
                qqq='th'
            print('Enter the',str(qq+1)+qqq+' bin below:')
            qq=int(input(''))
            l.append(qq)
            bins=l
    else:
        bins=[]
        a=25000
        s=a//20
        for q in range(0,a+1,s):
            bins.append(q)
    try:
        ls=(len(deaths)//2)
        deaths=deaths[:ls]
        
        #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
        plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
        plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
        plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
        
        plt.hist(deaths,bins=bins,color=['#66c2a5'],edgecolor='k')
        plt.xticks(bins)
        plt.title('Number of Countries under specific number of Deaths')
        plt.xlabel('Number of Deaths')
        plt.ylabel('Number of Countries')
        plt.grid(color='grey',ls='-.',lw=0.35)
        name='Number of Countries under specific number of Deaths'
        if saa=='a' or saa=='A':
            plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
        elif saa=='b' or saa=='B':
            plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
        
        plt.show()
        
    except:
        print()
        print('ERROR.')
        print('Bins passed should be constant e.g.40 60 80 100...')



def countries_in_continent_hist():
    name='Number of Countries in each Continent'
    #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
    plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
    
    continent=dffg['continent']
    bins=['Asia','Europe','Africa','North America','South America','Oceania']
    plt.hist(continent,bins=bins,color='#495769',edgecolor='white')
    
    plt.title('Number of Countries per Continent')
    plt.xlabel('Continents')
    plt.ylabel('Number of Countries')
    plt.xticks(bins,rotation=10)
    plt.grid(color='grey',ls='-.',lw = 0.35)

    if saa=='a' or saa=='A':
        plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    elif saa=='b' or saa=='B':
        plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)

    plt.show()
    

def total_case_barh():
    #the following two lines are given to stop a warning which shows up right before displaying the graph
    import warnings
    warnings.filterwarnings("ignore")
    
    #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
    plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)
    
    for_top10 = dffg.copy()
    for_top10.sort_values('total_deaths',ascending=False,inplace=True)
    for_top10.reset_index(inplace=True)#reseting the index after deleting rows
    for_top10.drop('index',axis=1,inplace=True)#deleting the index column that was created after reseting the index
    
    qop=len(for_top10)#this has the total nunber of countries
    l=[]
    for qqq in range(qop-10):#the loop repeats 10 times less so it keeps the top 10 countries
        l.append(qqq+10)#this begins insert index from 11th country 
    
    for_top10.drop(l,inplace=True)#dropping the countries which are not in the top 10
    
    for_top10.sort_values(by=['total_cases'],inplace=True)
    for_top10.reset_index(inplace=True,drop=True)
    #for_top10.drop(~[0,1,2,3,4,5,6,7,8,9],inplace=True)
    
    location=for_top10['location']
    cases=for_top10['total_cases']
    ypos=np.arange(len(cases))
    name='Horizontal Bar graph showing Top 10 Countries having highest cases'
    
    ax1=plt.subplot(111)#done so that the value of each bar can be displayed against each bar
    
    plt.barh(location,cases[ypos],color='steelblue',edgecolor='k')
    
    ax1.set_facecolor('lightgrey')
    
    ax1.xaxis.grid(color='grey',ls='-.',lw=0.25)#showing only xaxis grid
    
    name='Top 10 Countries with higest Cases'
    plt.title('Top 10 most Infected Countries')
    plt.xlabel('Number of Cases')
    #plt.ylabel('Countries')
    
    for py,px in enumerate(cases):#showing the value of each bar against it
        ax1.annotate('{:,}'.format(px),xy=(px+10,py),va='center',fontstyle='italic')
    ax1.set_xlim(0,cases.max()*1.18)
    
    if saa=='a' or saa=='A':
        plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    elif saa=='b' or saa=='B':
        plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)

    plt.show()






def total_death_barh():
    #the following two lines are given to stop a warning which shows up right before displaying the graph
    import warnings
    warnings.filterwarnings("ignore")
    
    #following three lines are given to prevent the printing of scientific values like '3.41e+06'    
    plt.ticklabel_format(axis='both', style='', scilimits=None, useOffset=None, useLocale=None, useMathText=None)
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.gcf().axes[0].xaxis.get_major_formatter().set_scientific(False)

    for_top10 = dffg.copy()
    for_top10.sort_values('total_deaths',ascending=False,inplace=True)
    for_top10.reset_index(inplace=True)#reseting the index after deleting rows
    for_top10.drop('index',axis=1,inplace=True)#deleting the index column that was created after reseting the index
    
    qop=len(for_top10)#this has the total nunber of countries
    l=[]
    for qqq in range(qop-10):#the loop repeats 10 times less so it keeps the top 10 countries
        l.append(qqq+10)#this begins insert index from 11th country 

    for_top10.drop(l,inplace=True)#dropping the countries which are not in the top 10

    for_top10.sort_values(by=['total_deaths'],inplace=True)
    for_top10.reset_index(inplace=True,drop=True)
    #for_top10.drop(~[0,1,2,3,4,5,6,7,8,9],inplace=True)
    
    location=for_top10['location']
    deaths=for_top10['total_deaths']
    ypos=np.arange(len(deaths))
    name='Horizontal bar graph showing Top 10 having highest deaths'
    
    ax1=plt.subplot(111)#done so that the value of each bar can be displayed against each bar
    
    plt.barh(location,deaths[ypos],color='salmon',edgecolor='darkred')
    
    ax1.xaxis.grid(color='grey',ls='-.',lw=0.25)#showing only xaxis grid
    
    ax1.set_facecolor('lightgrey')
    
    name='Top 10 Countries with higest Deaths'
    plt.title('Top 10 Countries with highest Deaths')
    plt.xlabel('Number of Deaths')
    #plt.ylabel('Countries')
    
    for py,px in enumerate(deaths):#showing the value of each bar against it
        ax1.annotate('{:,}'.format(px),xy=(px+10,py),va='center',fontstyle='italic')
    ax1.set_xlim(0,deaths.max()*1.18)
    
    if saa=='a' or saa=='A':
        plt.savefig(path+'\\'+name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)
    elif saa=='b' or saa=='B':
        plt.savefig(name+'.'+fmt,dpi=600,bbox_inches='tight',pad_inches=0.9)

    plt.show()







def visualisation():
    global dff,dfm,dft,dffg,dfmg,dftg,for_top10,saa,fmt,sa,nop,path,graph_option,fmt
    graph_option=False
    if nop==0:
        print()
        sa=input('Would you like to save the graphs you select or create?y/n:')
        print()
        if sa=='y' or sa=='Y':
            nop=1#to stop save fig option loop
            print('a.Specify a folder for saving the graphs')
            print('b.Autosave to folder containing the python project file')
            saa=input('Enter your selection:')
            print()
            if saa=='a' or saa=='A':
                path=input('Enter path of the folder you want to save the graphs to:')
                path.encode('unicode_escape')
                print()
                print('Would you like to specify the format in which the graph is to be saved?')
                saaa=input('If no then the default format is JPEG.?y/n:')
                if saaa=='y' or saaa=='Y':
                    print('a.PNG')
                    print('b.PDF')
                    print('c.SVG')
                    print('d.RAW')
                    print('e.JPG')
                    print('f.JPEG')
                    f=input('Enter your selection:')
                    if f=='a' or f=='A':
                        fmt='png'
                    elif f=='b' or f=='B':
                        fmt='pdf'
                    elif f=='c' or f=='C':
                        fmt='svg'
                    elif f=='d' or f=='D':
                        fmt='raw'
                    elif f=='e' or f=='E':
                        fmt='jpg'
                    elif f=='f' or f=='F':
                        fmt='jpeg'
                    graph_option=True
                elif saaa!='y' or saaa!='Y':
                    fmt='jpg' #since this is the format widley seen
                    graph_option=True
            elif saa=='b' or saa=='B':
                fmt='jpg'
                graph_option=True
        else:
            saa=False
        nop=1
        
        
    while True:
        print()
        print('\n一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一')
        print('                                         VISUALISATION')
        print('一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一')
        print('a.Total Cases & Deaths')
        print('b.Comparison b/w Cases and Deaths')
        print('c.Trends over time i.e.Cases,Deaths')
        print('d.Top 10 Countries')
        print('e.Misc. data related to covid-19')
        print('f.Number of Countries in Each continent')
        print('g.Go back to main menu')
        op=input('Enter your selection:')
        print()
        if op=='a' or op=='A':
            print('a.Total Cases')
            print('b.Total Deaths')
            m=input('Enter your option:')
            print()
            if m=='a' or m=='A':
                print('a.Total cases Country wise')
                print('b.Total cases Continent wise')
                print('c.Number of countries in specific range of Total Cases')
                mm=input('Enter your selection:')
                print()
                if mm=='a' or mm=='A':
                    total_cases_country_bar()
                elif mm=='b' or mm=='B':
                    total_cases_continent_bar()
                elif mm=='c' or mm=='C':
                    countries_under_cases_hist()
            elif m=='b' or m=='B':
                print('a.Total deaths Country wise')
                print('b.Total deaths Continent wise')
                print('c.Number of countries in specific range of Total Deaths')
                mm=input('Enter your selection:')
                print()
                if mm=='a' or mm=='A':
                    total_deaths_country_bar()
                elif mm=='b' or mm=='B':
                    total_deaths_continent_bar()
                elif mm=='c' or mm=='C':
                    countries_under_deaths_hist()
        elif op=='b' or op=='B':
            print('a.Country wise')
            print('b.Continent wise')
            mm=input('Enter your selection:')
            print()
            if mm=='a' or mm=='A':
                cases_vs_deaths_country_bar()
            if mm=='b' or mm=='B':
                cases_vs_deaths_continent_bar()
        elif op=='c' or op=='C':
            print('a.Trend of cases')
            print('b.Trend of deaths')
            mm=input('Enter your selection:')
            print()
            if mm=='a' or mm=='A':
                trends_cases_countries()
            if mm=='b' or mm=='B':
                trends_deaths_countries()
        elif op=='d' or op=='D':
            print('a.Top 10 Countries with highest Cases[Pie]')
            print('b.Top 10 Countries with highest Deaths[Pie]')
            print('c.Top 10 Countries with highest Cases[Horizontal bar]')
            print('d.Top 10 Countries with highest Deaths[Horizontal bar]')
            mm=input('Enter your selection:')
            if mm=='a' or mm=='A':
                total_cases_pie()
            if mm=='b' or mm=='B':
                total_deaths_pie()
            if mm=='c' or mm=='C':
                total_case_barh()
            if mm=='d' or mm=='D':
                total_death_barh()
        elif op=='e' or op=='E':
            print()
            dfmg_bar()
        elif op=='f' or op=='F':
            countries_in_continent_hist()
        elif op=='g' or op=='G':
            menu()
    







#Analysis module
def analysis():
    global dff,dfm,dft
    while True:
        print()
        print('\n一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一')
        print('                                            ANALYSIS')
        print('一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一')
        print('a.Print full data')
        print('b.Print top x rows')
        print('c.Print bottom x rows')
        print('d.Print particular columns')
        print('e.Print particular rows')
        print('f.Print column labels')
        print('g.Print after sorting')
        print('h.Print by giving condition')
        print('i.Data aggregation [max,count,mean,etc.]')
        print('j.Print country with highest numbers i.e.Deaths,Cases')
        print('k.Print complete statistics')
        print('l.Go back to main menu')
        op=input('Enter your selection:')
        print()
        if op=='a' or op=='A':#printing full data
            print('Main file containing data about all the countries[dff]:')
            print(dff)
            print()
            print('File containing trends of covid in Top 10 countries[dft]:')
            print(dft)
            print()
            print('File containing misc. infomation like age,population etc. of different countries[dfm]:')
            print(dfm)
        elif op=='b' or op=='B':#printing top rows
            print('a. Main file containing data about all the countries')
            print('b. File containing trends of covid in Top 10 countries')
            print('c. File containing misc. infomation like age,population etc. of different countries')
            opp=input('Select the csv file you want to use:')
            if opp=='a' or opp=='A':
                qwe=dff
            elif opp=='b' or opp=='B':
                qwe=dft
            elif opp=='c' or opp=='C':
                qwe=dfm
            try:
                print()
                no = int(input('Enter the number of rows you want to print from the top:'))
                print()
                print(qwe.head(no))
            except:
                print(qwe.head())
        
        elif op=='c' or op=='C':#printing top rows
            print('a. Main file containing data about all the countries')
            print('b. File containing trends of covid in Top 10 countries')
            print('c. File containing misc. infomation like age,population etc. of different countries')
            opp=input('Select the csv file you want to use:')
            if opp=='a' or opp=='A':
                qwe=dff
            elif opp=='b' or opp=='B':
                qwe=dft
            elif opp=='c' or opp=='C':
                qwe=dfm
            try:
                print()
                no = int(input('Enter the number of rows you want to print from the top:'))
                print()
                print(qwe.tail(no))
            except:
                print(qwe.tail())
                
        elif op=='d' or op=='D':#printing particular columns
            print('a. Main file containing data about all the countries')
            print('b. File containing trends of covid in Top 10 countries')
            print('c. File containing misc. infomation like age,population etc. of different countries')
            opp=input('Select the csv file you want to use:')
            print()
            if opp=='a' or opp=='A':
                qwe=dff
            elif opp=='b' or opp=='B':
                qwe=dft
            elif opp=='c' or opp=='C':
                qwe=dfm
            q=input('Do you want to print the column names before selection?y/n:')
            if q=='y' or q=='Y':
                print(qwe.columns)
            print()
            l=[]
            print('a.Select using default column index')
            print('b.Select using column name')
            w=input('Enter your selection here:')
            print()
            if w=='a' or w=='A':
                ww=int(input('Enter the no of columns you want to print:'))
                print()
                if ww==1:
                    qq=int(input('Enter the index of the column:'))
                    l=qq
                elif ww>1:
                    for qq in range(ww):
                        if qq+1==1:
                            qqq='st'
                        elif qq+1==2:
                            qqq='nd'
                        elif qq+1==3:
                            qqq='rd'
                        elif qq+1<=4:
                            qqq='th'
                        print('Enter the index of',str(qq+1)+qqq+' column you want to be printed below:-')
                        qq=int(input(''))
                        if qq<=len(qwe.columns):
                            l.append(qq)
                print()
                print(qwe.iloc[:,l])
            elif w=='b' or w=='B':
                ww=input('Enter the no of columns you want to print:')
                if int(ww)==1:
                    qq=input('Enter name of the column:')
                    l.append(qq)
                elif int(ww)>1:
                    for qq in range(int(ww)):
                        if qq+1==1:
                            qqq='st'
                        elif qq+1==2:
                            qqq='nd'
                        elif qq+1==3:
                            qqq='rd'
                        elif qq+1<=4:
                            qqq='th'
                        print('Enter the name of',str(qq+1)+qqq+' column you want to be printed below:')#str(f+1)+ for prining st with the
                        qq=input('')
                        l.append(qq)
                print()
                print(qwe[l])#what can we posibally write about this function lol
                    
        elif op=='e' or op=='E':#printing particular rows
            print('a. Main file containing data about all the countries')
            print('b. File containing trends of covid in Top 10 countries')
            print('c. File containing misc. infomation like age,population etc. of different countries')
            opp=input('Select the csv file you want to use:')
            print()
            if opp=='a' or opp=='A':
                qwe=dff
            elif opp=='b' or opp=='B':
                qwe=dft
            elif opp=='c' or opp=='C':
                qwe=dfm
            l=[]
            print('a)Print using Country Name')
            print('b)Print using Row index')
            print('c)Print all rows after a specific index')
            print('d)Print all rows before a specific index')
            www=input('Enter you selection a/b:')
            print()
            if www=='a' or www=='A':
                ww=int(input('Enter the no of countries/rows you want to print:'))
                print()
                wwww=input('Do you want to print the country names?y/n:')
                if wwww=='y' or wwww=='Y':
                    print(qwe.loc[:,['location']])
                print()
                if ww==1:#normal loc function is used for pritning one country
                    nam=input('Enter the name of the country:')
                    print(qwe.loc[qwe['location']==(nam)])
                elif ww>1:#since loc cannot print two country names at the same time, so we use append loop
                    for qq in range(ww):
                        if qq+1==1:
                            qqq='st'
                        elif qq+1==2:
                            qqq='nd'
                        elif qq+1==3:
                            qqq='rd'
                        elif qq+1<=4:
                            qqq='th'
                        print('Enter the name of',str(qq+1)+qqq+' country you want to be printed below:-')
                        contr=input('')
                        a=qwe.loc[qwe['location']==(contr)]
                        if qq==0:
                            b=qwe.loc[qwe['location']==(contr)]
                        else:
                            b=pd.concat([b,a])#to print pultiple countries together, they are concatinated
                    print()
                    print(b)
            elif www=='b' or www=='B':
                ww=int(input('Enter the no of countries/rows you want to print:'))
                print()
                if ww==1:
                    qq=int(input('Enter the index of the column:'))
                    l=qq
                elif ww>1:
                    for qq in range(ww):
                        if qq+1==1:
                            qqq='st'
                        elif qq+1==2:
                            qqq='nd'
                        elif qq+1==3:
                            qqq='rd'
                        elif qq+1<=4:
                            qqq='th'
                        print('Enter index of the',str(qq+1)+qqq+' row you want to be printed below:-')
                        qqqqq=input('')
                        try:#incase the user resets an index to string this will take string as well as int
                            if type(int(qqqqq))==int:
                                qqqqqq=int(qqqqq)
                        except:
                            qqqqqq=qqqqq
                        l.append(qqqqqq)
                print()
                print(qwe.loc[l])
            elif www=='c' or www=='C':
                print(qwe.index)
                try:
                    q=int(input('Print rows after the index:'))
                    print()
                    print(qwe.iloc[q:])
                except:
                    print('Only integer values allowed.')
            elif www=='d' or www=='D':
                print(qwe.index)
                try:
                    q=int(input('Print rows before the index:'))
                    print()
                    print(qwe.iloc[:q])
                except:
                    print('Only integer values allowed.')
            
        elif op=='f' or op=='F':#printing particular columns
            print('a. Main file containing data about all the countries')
            print('b. File containing trends of covid in Top 10 countries')
            print('c. File containing misc. infomation like age,population etc. of different countries')
            print('d. All three files')
            ww=input('Select the CSV file to be used:')
            print()
            if ww=='a' or ww=='A':
                print(dff.columns)
            elif ww=='b' or ww=='B':
                print(dft.columns)
            elif ww=='c' or ww=='C':
                print(dfm.columns)
            elif ww=='d' or ww=='D':                
                print('Main file containing data about all the countries[dff]:')
                print(dff.columns)
                print()
                print('File containing trends of covid in Top 10 countries[dft]:')
                print(dft.columns)
                print()
                print('File containing misc. infomation like age,population etc. of different countries[dfm]:')
                print(dfm.columns)
            
        elif op=='g' or op=='G':#print after sorting
            print('a. Main file containing data about all the countries')
            print('b. File containing trends of covid in Top 10 countries')
            print('c. File containing misc. infomation like age,population etc. of different countries')
            opp=input('Select the csv file you want to use:')
            if opp=='a' or opp=='A':
                qwe=dff
            elif opp=='b' or opp=='B':
                qwe=dft
            elif opp=='c' or opp=='C':
                qwe=dfm
            print()
            q=input('Do you want to print column names before selection?y/n:')
            if q=='y' or q=='Y':
                print(qwe.columns)
            print()
            wwww=input('Enter the column name to be used for sorting:')
            print()
            inp=input('Do you want to inplace the sort?y/n:')
            print()
            print('a.Ascending order')
            print('b.Descending order')
            order=input('Select order to be sorted in:')
            print()
            if inp=='y' or inp=='Y':
                if order=='b':
                    print(qwe.sort_values(by=[wwww],ascending=False))
                    qwe.sort_values(by=[wwww],inplace=True,ascending=False)
                else:
                    print(qwe.sort_values(by=[wwww]))
                    qwe.sort_values(by=[wwww],inplace=True)
            else:
                if order=='b':
                    print(qwe.sort_values(by=[wwww],ascending=False))
                else:
                    print(qwe.sort_values(by=[wwww]))
            
        elif op=='h' or op=='H':#printing by giving condition
            print('a. Main file containing data about all the countries')
            print('b. File containing trends of covid in Top 10 countries')
            print('c. File containing misc. infomation like age,population etc. of different countries')
            opp=input('Select the csv file you want to use:')
            if opp=='a' or opp=='A':
                qwe=dff
            elif opp=='b' or opp=='B':
                qwe=dft
            elif opp=='c' or opp=='C':
                qwe=dfm
            print()
            q=input('Do you want to print the column names before selection?y/n:')
            if q=='y' or q=='Y':
                print(qwe.columns)
            print()
            ww=input('Enter name of the column you want to give condition on:')
            print()
            www=input('Do you want to select the columns to be printed?y/n:')                    
            if www=='y' or www=='Y':
                ln=int(input('Enter the number of columns you want to print:'))
                print()
                if ln==1:
                    wwww=input('Enter name of the column you want to print:')
                    l=list(wwww)
                elif ln>1:
                    l=[]
                    for qq in range(ln):
                        if qq+1==1:
                            qqq='st'
                        elif qq+1==2:
                            qqq='nd'
                        elif qq+1==3:
                            qqq='rd'
                        elif qq+1<=4:
                            qqq='th'
                        print('Enter name of the',str(qq+1)+qqq+' column you want to be printed below:-')
                        qq=input('')
                        l.append(qq)
            print()
            print('Conditions:')
            print('a.Greater than')#greater than or equals to is used because it makes more sense
            print('b.Less than')#less than or equals to is used because it makes more sense
            print('c.Equal to')
            print('d.Not Equal to')
            wwwww=input('Enter you selection:')
            print()
            if (qwe[ww].dtype)=='object':#####################################
                if wwwww=='a' or wwwww=='A':
                    wwwwww=input('Enter value here: Greater than ')
                    print()
                    if www=='y' or www=='Y':
                        print(qwe.loc[qwe[ww]>wwwwww,l])
                    else:
                        print(qwe.loc[qwe[ww]>wwwwww])
                elif wwwww=='b' or wwwww=='B':
                    wwwwww=input('Enter value here: Less than ')
                    print()
                    if www=='y' or www=='Y':
                        print(qwe.loc[qwe[ww]<wwwwww,l])
                    else:
                        print(qwe.loc[qwe[ww]<wwwwww])
                elif wwwww=='c' or wwwww=='C':
                    wwwwww=input('Enter value here: Equal to ')
                    print()
                    if www=='y' or www=='Y':
                        print(qwe.loc[qwe[ww]==wwwwww,l])
                    else:
                        print(qwe.loc[qwe[ww]==wwwwww])
                elif wwwww=='d' or wwwww=='D':
                    wwwwww=input('Enter value here: Not equal to ')
                    print()
                    if www=='y' or www=='Y':
                        print(qwe.loc[qwe[ww]!=wwwwww,l])
                    else:
                        print(qwe.loc[qwe[ww]!=wwwwww])
            elif (qwe[ww].dtype)=='int64' or (qwe[ww].dtype)=='float' or (qwe[ww].dtype)=='int32':
                if wwwww=='a' or wwwww=='A':
                    wwwwww=int(input('Enter value here: Greater than '))
                    print()
                    if www=='y' or www=='Y':
                        print(qwe.loc[qwe[ww]>=wwwwww,l])
                    else:
                        print(qwe.loc[qwe[ww]>=wwwwww])
                elif wwwww=='b' or wwwww=='B':
                    wwwwww=int(input('Enter value here: Less than '))
                    print()
                    if www=='y' or www=='Y':
                        print(qwe.loc[qwe[ww]<=wwwwww,l])
                    else:
                        print(qwe.loc[qwe[ww]<=wwwwww])
                elif wwwww=='c' or wwwww=='C':
                    wwwwww=int(input('Enter value here: Equal to '))
                    print()
                    if www=='y' or www=='Y':
                        print(qwe.loc[qwe[ww]==wwwwww,l])
                    else:
                        print(qwe.loc[qwe[ww]==wwwwww])
                elif wwwww=='d' or wwwww=='D':
                    wwwwww=int(input('Enter value here: Not equal to '))
                    print()
                    if www=='y' or www=='Y':
                        print(qwe.loc[qwe[ww]!=wwwwww,l])
                    else:
                        print(qwe.loc[qwe[ww]!=wwwwww])
                        
        elif op=='i' or op=='I':#aggregate functions
            while True:
                print('a.max()')
                print('b.min()')
                print('c.sum()')
                print('d.count()')
                print('e.mean()/avg()')
                print('f.Exit')
                ww=input('Enter your selection:')
                print()
                if ww=='a' or ww=='A':
                    print('a.Main file containing data about all the countries')
                    print('b.File containing trends of covid in Top 10 countries')
                    print('c.File containing misc. infomation like age,population etc. of different countries')
                    opp=input('Select the csv file you want to use:')
                    if opp=='a' or opp=='A':
                        qwe=dff
                    elif opp=='b' or opp=='B':
                        qwe=dft
                    elif opp=='c' or opp=='C':
                        qwe=dfm
                    print()
                    print('a.Max from particular coulum')
                    print('b.Max from all the coulums/rows')
                    www=input('Enter you selection:')
                    print()
                    if www=='a' or www=='A':
                        wwww=input('Do you want to print the column names before selection?y/n:')
                        if wwww=='y' or wwww=='Y':
                            print(qwe.columns)
                        print()
                        wwwww=input('Enter column name to be used:')
                        print(qwe[wwwww].max())
                    elif www=='b' or www=='B':
                        print('a.Max from all rows')
                        print('b.Max from all coulums')
                        wwww=input('Enter your selection:')
                        print()
                        if wwww=='a' or wwww=='A':
                            print(qwe.max(axis=1))
                        elif wwww=='b' or wwww=='B':
                            print(qwe.max())
                    print()
                elif ww=='b' or ww=='B':
                    print('a. Main file containing data about all the countries')
                    print('b. File containing trends of covid in Top 10 countries')
                    print('c. File containing misc. infomation like age,population etc. of different countries')
                    opp=input('Select the csv file you want to use:')
                    if opp=='a' or opp=='A':
                        qwe=dff
                    elif opp=='b' or opp=='B':
                        qwe=dft
                    elif opp=='c' or opp=='C':
                        qwe=dfm
                    print()
                    print('a.Min from particular coulum')
                    print('b.Min from all the coulums/rows')
                    www=input('Enter you selection:')
                    print()
                    if www=='a' or www=='A':
                        wwww=input('Do you want to print the column names before selection?y/n:')
                        if wwww=='y' or wwww=='Y':
                            print(qwe.columns)
                        print()
                        wwwww=input('Enter column name to be used:')
                        print(qwe[wwwww].min())
                    elif www=='b' or www=='B':
                        print('a.Min from all rows')
                        print('b.Min from all coulums')
                        wwww=input('Enter your selection:')
                        print()
                        if wwww=='a' or wwww=='A':
                            print(qwe.min(axis=1))
                        elif wwww=='b' or wwww=='B':
                            print(qwe.min())
                    print()
                elif ww=='c' or ww=='C':
                    print('a. Main file containing data about all the countries')
                    print('b. File containing trends of covid in Top 10 countries')
                    print('c. File containing misc. infomation like age,population etc. of different countries')
                    opp=input('Select the csv file you want to use:')
                    if opp=='a' or opp=='A':
                        qwe=dff
                    elif opp=='b' or opp=='B':
                        qwe=dft
                    elif opp=='c' or opp=='C':
                        qwe=dfm
                    print()
                    print('a.Sum of a particular coulum')
                    print('b.Sum from all the coulums/rows')
                    www=input('Enter you selection:')
                    print()
                    if www=='a' or www=='A':
                        wwwwwwww=input('Do you want to print the column names before selection?y/n:')
                        if wwwwwwww=='y' or wwwwwwww=='Y':
                            print(qwe.columns)
                        print()
                        wwwww=input('Enter column name to be used:')
                        print(qwe[wwwww].sum())
                    elif www=='b' or www=='B':
                        print('a.Sum from all rows')
                        print('b.Sum from all coulums')
                        wwww=input('Enter your selection:')
                        print()
                        if wwww=='a' or wwww=='A':
                            print(qwe.sum(axis=1))
                        elif wwww=='b' or wwww=='B':
                            print(qwe.sum())
                    print()
                elif ww=='d' or ww=='D':
                    print('a. Main file containing data about all the countries')
                    print('b. File containing trends of covid in Top 10 countries')
                    print('c. File containing misc. infomation like age,population etc. of different countries')
                    opp=input('Select the csv file you want to use:')
                    if opp=='a' or opp=='A':
                        qwe=dff
                    elif opp=='b' or opp=='B':
                        qwe=dft
                    elif opp=='c' or opp=='C':
                        qwe=dfm
                    print()
                    print('a.Count from a particular coulum')
                    print('b.Count from all the coulums/rows')
                    www=input('Enter you selection:')
                    print()
                    if www=='a' or www=='A':
                        wwwwwwww=input('Do you want to print the column names before selection?y/n:')
                        if wwwwwwww=='y' or wwwwwwww=='Y':
                            print(qwe.columns)
                        print()
                        wwwww=input('Enter column name to be used:')
                        print(qwe[wwwww].count())
                    elif www=='b' or www=='B':
                        print('a.Count from all rows')
                        print('b.Count from all coulums')
                        wwww=input('Enter your selection:')
                        print()
                        if wwww=='a' or wwww=='A':
                            print(qwe.count(axis=1))
                        elif wwww=='b' or wwww=='B':
                            print(qwe.count())
                        print()
                elif ww=='e' or ww=='E':
                    print('a. Main file containing data about all the countries')
                    print('b. File containing trends of covid in Top 10 countries')
                    print('c. File containing misc. infomation like age,population etc. of different countries')
                    opp=input('Select the csv file you want to use:')
                    if opp=='a' or opp=='A':
                        qwe=dff
                    elif opp=='b' or opp=='B':
                        qwe=dft
                    elif opp=='c' or opp=='C':
                        qwe=dfm
                    print()
                    print('a.Average of a particular coulum')
                    print('b.Average from all the coulums/rows')
                    www=input('Enter you selection:')
                    print()
                    if www=='a' or www=='A':
                        wwwwwwww=input('Do you want to print the column names before selection?y/n:')
                        if wwwwwwww=='y' or wwwwwwww=='Y':
                            print(qwe.columns)
                        print()
                        wwwww=input('Enter column name to be used:')
                        check=qwe.dtypes[wwwww]
                        if check=='float' or check=='int64' or check=='int32':
                            print(qwe[wwwww].mean())
                        elif check=='object':
                            print('ERROR. Only integer values can be used for mean function')
                            print()
                            rick=input('Would you like to select another column?y/n:')
                            print()
                            if rick=='y' or rick=='Y':
                                morty=1#if user wants to select column again
                                while morty==1:
                                    wwwww=input('Enter column name to be used:')
                                    check=qwe.dtypes[wwwww]
                                    if check=='float' or check=='int64' or check=='int32':
                                        print(qwe[wwwww].mean())
                                        break#breaks the while loop since avg answer is correct
                                    elif check=='object' or check=='NaN':
                                        print('ERROR Only integer values can be used for mean function')
                                        print()
                                    rick=input('Would you like to select another column?y/n')
                                    print()
                                    if rick=='y' or rick=='Y':
                                        continue#if the user wamts to select a column again
                                    elif rick!='y' or rick!='Y':
                                        morty=0
                    elif www=='b' or www=='B':
                        print('a.Average from all integer rows')
                        print('b.Average from all integer coulums')
                        wwww=input('Enter your selection:')
                        print()
                        if wwww=='a' or wwww=='A':
                            print(qwe.mean(axis=1))
                        elif wwww=='b' or wwww=='B':
                            print(qwe.mean())
                    print()
                    
                elif ww=='f' or ww=='F':
                    analysis()
        elif op=='j' or op=='J':#printing countries with highest numbers
            print('a. Main file containing data about all the countries')
            print('b. File containing trends of covid in Top 10 countries')
            print('c. File containing misc. infomation like age,population etc. of different countries')
            opp=input('Select the csv file you want to use:')
            print()
            if opp=='a' or opp=='A':
                qwe=dff
            elif opp=='b' or opp=='B':
                qwe=dft
            elif opp=='c' or opp=='C':
                qwe=dfm
            print(qwe.columns)
            print()
            try:
                w=input('Country with highest and lowest:')
                print()
                print('Country with highest',w+':')
                print(qwe[qwe[w]== qwe[w].max()])
                print()
                print('Country with lowest',w+':')
                print(qwe[qwe[w]== qwe[w].min()])
            except:
                None
            
        elif op=='k' or op=='K':
            print(dff.aggregate(['max','min','count','mean','std']))
        
        elif op=='l' or op=='L':
            menu()
        print()




#Manipulation module
def manipulation():
    global dff,dft,dfm#This is suppose to be given because we are editing the csv data here
    while True:
        print()
        print('\n+一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一-')
        print('                                         =MANIPULATION=')
        print('-一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一+')
        print('a.Insert a new column')
        print('b.Insert a new row')
        print('c.Delete a column')
        print('d.Delete a row')
        print('e.Change column names')
        print('f.Set column as index')
        print('g.Change row index')
        print('h.Reset index')
        print('i.Reorder columns')
        print('j.Reset column order to default')
        print('k.Go back to main menu')
        op=input('Enter your selection:')
        print()
        if op=='a' or op=='A':#insert a new column
            print('a.Inserting by adding two or more existing columns [max 6]')
            print('b.Inserting by passing scalar value [Manual entring values not possible since data avaliable is large.]')
            w=input('Enter your selection here:')
            print()
            print('a.Insert into file containing total cases and total deaths in all the countries')
            print('b.Insert into file containing trends of covid in Top 10 countries')
            print('c.Insert into file containing misc. infomation like age,population etc. of different countries')
            ww=input('Select the csv file you want to use:')
            if ww=='a' or ww=='A':
                qwe=dff
            elif ww=='b' or ww=='B':
                qwe=dft
            elif ww=='c' or ww=='C':
                qwe=dfm
            print()
            if w=='a':
                qqq=input('Do you want to print the column names before selection?y/n:')
                if qqq=='y' or qqq=='Y':
                    print(qwe.columns)
                print()
                no=int(input('Enter the number of columns you want to combine to form a new column:'))
                print()
                #a=1
                if len(qwe.columns)>=1:
                    if no==1:
                        nam=input('Enter the name you would like to keep for the new column:')
                        print()
                        aa=input('Enter the name of the column you want to duplicate:')
                        qwe[nam]=qwe[aa]
                        print()
                        opp=input('The column has been added. Would you like to print the data?y/n:')
                        if opp=='y' or opp=='Y':
                            print(qwe)
                    if len(qwe.columns)>=2:
                        if no==2:
                            nam=input('Enter the name you would like to keep for the new column:')
                            print()
                            aa=input('Enter the name of the 1st column you want to join:')
                            bb=input('Enter the name of the 2nd column you want to join:')
                            try:
                                qwe[nam]=qwe[aa]+qwe[bb]
                                print()
                                opp=input('The column has been added. Would you like to print the data?y/n:')
                                if opp=='y' or opp=='Y':
                                    print(qwe)
                            except:
                                print('ERROR. Only columns of same datatype can be combined')
                        if len(qwe.columns)>=3:
                            if no==3:
                                nam=input('Enter the name you would like to keep for the new column:')
                                print()
                                aa=input('Enter the name of the 1st column you want to join:')
                                bb=input('Enter the name of the 2nd column you want to join:')
                                cc=input('Enter the name of the 3rd column you want to join:')
                                try:
                                    qwe[nam]=qwe[aa]+qwe[bb]+qwe[cc]
                                    print()
                                    opp=input('The column has been added. Would you like to print the data?y/n:')
                                    if opp=='y' or opp=='Y':
                                        print(qwe)
                                except:
                                    print('ERROR. Only columns of same datatype can be combined')
                            if len(qwe.columns)>=4:
                                if no==4:
                                    nam=input('Enter the name you would like to keep for the new column:')
                                    print()
                                    aa=input('Enter the name of the 1st column you want to join:')
                                    bb=input('Enter the name of the 2nd column you want to join:')
                                    cc=input('Enter the name of the 3rd column you want to join:')
                                    dd=input('Enter the name of the 4th column you want to join:')
                                    try:
                                        qwe[nam]=qwe[aa]+qwe[bb]+qwe[cc]+qwe[dd]
                                        print()
                                        opp=input('The column has been added. Would you like to print the data?y/n:')
                                        if opp=='y' or opp=='Y':
                                            print(qwe)
                                    except:
                                        print('ERROR. Only columns of same datatype can be combined')
                                if len(qwe.columns)>=5:
                                    if no==5:
                                        nam=input('Enter the name you would like to keep for the new column:')
                                        print()
                                        aa=input('Enter the name of the 1st column you want to join:')
                                        bb=input('Enter the name of the 2nd column you want to join:')
                                        cc=input('Enter the name of the 3rd column you want to join:')
                                        dd=input('Enter the name of the 4th column you want to join:')
                                        ee=input('Enter the name of the 5th column you want to join:')
                                        try:
                                            qwe[nam]=qwe[aa]+qwe[bb]+qwe[cc]+qwe[dd]+qwe[ee]
                                            print()
                                            opp=input('The column has been added. Would you like to print the data?y/n:')
                                            if opp=='y' or opp=='Y':
                                                print(qwe)
                                        except:
                                            print('ERROR. Only columns of same datatype can be combined')
                                    if len(qwe.columns)>=6:
                                        if no==6:
                                            nam=input('Enter the name you would like to keep for the new column:')
                                            print()
                                            aa=input('Enter the name of the 1st column you want to join:')
                                            bb=input('Enter the name of the 2nd column you want to join:')
                                            cc=input('Enter the name of the 3rd column you want to join:')
                                            dd=input('Enter the name of the 4th column you want to join:')
                                            ee=input('Enter the name of the 5th column you want to join:')
                                            ff=input('Enter the name of the 6th column you want to join:')
                                            try:
                                                qwe[nam]=qwe[aa]+qwe[bb]+qwe[cc]+qwe[dd]+qwe[ee]+qwe[ff]
                                                print()
                                                opp=input('The column has been added. Would you like to print the data?y/n:')
                                                if opp=='y' or opp=='Y':
                                                    print(qwe)
                                            except:
                                                print('ERROR. Only columns of same datatype can be combined')

            elif w=='b' or w=='B':
                if ww=='a' or ww=='A':
                    qwe=dff
                elif ww=='b' or ww=='B':
                    qwe=dft
                elif ww=='c' or ww=='C':
                    qwe=dfm
                w=input('Enter name you want to keep for the new column:')
                print()
                n=input('Enter scallar value:')
                try:#incase the user resets an index to string this will take string as well as int
                    if type(int(n))==int:
                        www=int(n)
                except:
                    www=n
                print()
                qwe[w]=www
                print('Column sucessfully added.')
                wwww=input('Would you like to print the data?y/n:')
                if wwww=='y' or wwww=='Y':
                    print()
                    print(qwe)

        elif op=='b' or op=='B':#insert a new row
            print('a.Insert into file containing total cases and total deaths in all the countries')
            print('b.Insert into file containing trends of covid in Top 10 countries')
            print('c.Insert into file containing misc. infomation like age,population etc. of different countries')
            opp=input('Select the csv file you want to use:')
            print()
            if opp=='a' or opp=='A':
                qwe=dff
                #nn='finaldata.csv'
            elif opp=='b' or opp=='B':
                qwe=dft
                #nn='top10aa.csv'
            elif opp=='c' or opp=='C':
                qwe=dfm
                #nn='misc data neww.csv'
            q=list(qwe.columns)
            l=[]
            for w in range(len(q)):
                if qwe[q[w]].dtype=='int64' or qwe[q[w]].dtype=='int32' or qwe[q[w]].dtype=='float':
                    try:
                        ww=int(input('Enter the number of '+q[w]+':'))#checking if the column is int or string
                    except:
                        ww=0#incase the user presses enter
                elif qwe[q[w]].dtype=='object':
                    ww=input('Enter the name of '+q[w]+':')
                l.append(ww)
            qwe.loc[len(qwe.index+1)]=l
            #append_list_as_row(nn,l)
            print()
            print('Row sucessfully added.')
            www=input('Would you like to print the data?y/n:')
            if www=='y' or www=='Y':
                print()
                print(qwe)



        elif op=='c' or op=='C':#deleting a column
            print('a.Insert into file containing total cases and total deaths in all the countries')
            print('b.Insert into file containing trends of covid in Top 10 countries')
            print('c.Insert into file containing misc. infomation like age,population etc. of different countries')
            ww=input('Select the csv file you want to  use:')
            print()
            if ww=='a' or ww=='A':
                qwe=dff
            elif ww=='b' or ww=='B':
                qwe=dft
            elif ww=='c' or ww=='C':
                qwe=dfm
            ww=int(input('Enter the number of columns you want to delete:'))
            print()
            www=input('Do you want to print column names before selection?y/n:')
            if www=='y' or www=='Y':
                print(qwe.columns)
            print()
            if ww==1:
                www=input('Enter name of the column to be deleted:')
                qwe.drop([www],axis=1,inplace=True)
            elif ww>1:
                l=[]
                for qq in range(ww):
                    if qq+1==1:
                        qqq='st'
                    elif qq+1==2:
                        qqq='nd'
                    elif qq+1==3:
                        qqq='rd'
                    elif qq+1<=4:
                        qqq='th'
                    print('Enter name of the',str(qq+1)+qqq+' column you want to be deleted below:-')
                    qq=input('')
                    l.append(qq)
                qwe.drop(l,axis=1,inplace=True)
            print()
            print('Dropping successful.')
            wwww=input('Would you like to print the data?y/n:')
            if wwww=='y' or wwww=='Y':
                print(qwe)
                
        elif op=='d' or op=='D':#deleting rows
            print('a.Insert into file containing total cases and total deaths in all the countries')
            print('b.Insert into file containing trends of covid in Top 10 countries')
            print('c.Insert into file containing misc. infomation like age,population etc. of different countries')
            opp=input('Select the csv file you want to use:')
            print()
            if opp=='a' or opp=='A':
                qwe=dff
            elif opp=='b' or opp=='B':
                qwe=dft
            elif opp=='c' or opp=='C':
                qwe=dfm
            print('a.Select using row index')
            print('b.Select using condition')
            ww=input('Enter your slection:')
            print()
            if ww=='a' or ww=='A':
                www=int(input('Enter the number of rows you want to delete:'))
                print()
                if www==1:
                    wwwwww=input('Do you want to print the data before selecting?y/n:')
                    if wwwwww=='y' or wwwwww=='Y':
                        print(qwe)
                    wwww=int(input('Enter index of the row to be deleted:'))
                    qwe.drop([wwww],inplace=True)
                    print()
                    print('Dropping successful.')
                    wwwww=input('Would you like to print the data?y/n:')
                    if wwwww=='y' or wwwww=='Y':
                        print()
                        print(qwe)
                elif www>1:
                    wwwwww=input('Do you want to print the data before selecting?y/n:')
                    if wwwwww=='y' or wwwwww=='Y':
                        print(qwe)
                    l=[]
                    for qq in range(www):
                        if qq+1==1:
                            qqq='st'
                        elif qq+1==2:
                            qqq='nd'
                        elif qq+1==3:
                            qqq='rd'
                        elif qq+1<=4:
                            qqq='th'
                        print('Enter index of the',str(qq+1)+qqq+' row you want to be deleted below:-')
                        qq=int(input(''))
                        l.append(qq)
                    qwe.drop(l,inplace=True)
                    print()
                    print('Dropping successful.')
                    wwwww=input('Would you like to print the data?y/n:')
                    if wwwww=='y' or wwwww=='Y':
                        print()
                        print(qwe)
            if ww=='b' or ww=='B':
                q=input('Do you want to print the data before selection?y/n:')
                if q=='y' or q=='Y':
                    print(qwe)
                print()
                ww=input('Enter name of the column you want to give condition on:')
                print()
                print('Conditions:')
                print('a.Greater than')#greater than or equals to is used because it makes more sense
                print('b.Less than')#less than or equals to is used because it makes more sense
                print('c.Equal to')
                print('d.Not Equal to')
                wwwww=input('Enter you selection:')
                print()
                if (qwe[ww].dtype)=='object':
                    if wwwww=='a' or wwwww=='A':
                        wwwwww=input('Enter value here: Greater than ')
                        print()
                        qwe.drop(qwe[qwe[ww]>wwwwww].index,inplace=True)
                    elif wwwww=='b' or wwwww=='B':
                        wwwwww=input('Enter value here: Less than ')
                        print()
                        qwe.drop(qwe[qwe[ww]<wwwwww].index,inplace=True)
                    elif wwwww=='c' or wwwww=='C':
                        wwwwww=input('Enter value here: Equal to ')
                        print()
                        qwe.drop(qwe[qwe[ww]==wwwwww].index,inplace=True)
                    elif wwwww=='d' or wwwww=='D':
                        wwwwww=input('Enter value here: Not equal to ')
                        print()
                        qwe.drop(qwe[qwe[ww]!=wwwwww].index,inplace=True)
                elif (qwe[ww].dtype)=='int64' or (qwe[ww].dtype)=='float' or (qwe[ww].dtype)=='int32':
                    if wwwww=='a' or wwwww=='A':
                        wwwwww=int(input('Enter value here: Greater than '))
                        print()
                        qwe.drop(qwe[qwe[ww]>wwwwww].index,inplace=True)
                    elif wwwww=='b' or wwwww=='B':
                        wwwwww=int(input('Enter value here: Less than '))
                        print()
                        qwe.drop(qwe[qwe[ww]<wwwwww].index,inplace=True)
                    elif wwwww=='c' or wwwww=='C':
                        wwwwww=int(input('Enter value here: Equal to '))
                        print()
                        qwe.drop(qwe[qwe[ww]==wwwwww].index,inplace=True)
                    elif wwwww=='d' or wwwww=='D':
                        wwwwww=int(input('Enter value here: Not equal to '))
                        print()
                        qwe.drop(qwe[qwe[ww]!=wwwwww].index,inplace=True)
                print()
                print('Dropping successful.')
                wwwww=input('Would you like to print the data?y/n:')
                if wwwww=='y' or wwwww=='Y':
                    print()
                    print(qwe)

        elif op=='e' or op=='E':#changing column name
            print('a.Rename columns of file containing total cases and total deaths in all the countries')
            print('b.Rename columns of file containing trends of covid in Top 10 countries')
            print('c.Rename columns of file containing misc. infomation like age,population etc. of different countries')
            ww=input('Select the csv file you want to use:')
            if ww=='a' or ww=='A':
                qwe=dff
            elif ww=='b' or ww=='B':
                qwe=dft
            elif ww=='c' or ww=='C':
                qwe=dfm
            print()
            qqq=input('Do you want to print the column names before selection?y/n:')
            if qqq=='y' or qqq=='Y':
                print(qwe.columns)
                print()
            d={}
            q=int(input('Enter the number of columns you want to rename:'))
            print()
            for qq in range(q):
                if qq+1==1:
                    qqq='st'
                elif qq+1==2:
                    qqq='nd'
                elif qq+1==3:
                    qqq='rd'
                elif qq+1<=4:
                    qqq='th'
                print('Enter name of the',str(qq+1)+qqq+' column you want to change below:')
                a=input('')
                b=input('Enter new name to be kept:')
                d[a]=b
                print()
            qwe.rename(columns=d,inplace=True)
            print('Renaming sucessfully done.')
            wwwww=input('Would you like to print the data?y/n:')
            if wwwww=='y' or wwwww=='Y':
                print()
                print(qwe)
            
        elif op=='f' or op=='F':#setting a column as index
                print('a.Setting index for file containing total cases and total deaths in all the countries')
                print('b.Setting index for file containing trends of covid in Top 10 countries')
                print('c.Setting index for file cotnaining misc. infomation like age,population etc. of different countries')
                ww=input('Select the csv file you want to use:')
                if ww=='a' or ww=='A':
                    qwe=dff
                elif ww=='b' or ww=='B':
                    qwe=dft
                elif ww=='c' or ww=='C':
                    qwe=dfm
                print()
                w=input('Do you want to print the columns before selection?y/n:')
                if w=='y' or w=='Y':
                    print(qwe.columns)
                    print()
                    print(qwe)
                print()
                try:
                    www=input('Enter the column name that you want to set as the index:')
                    try:#incase the user resets an index to string this will take string as well as int
                        if type(int(www))==int:
                            wwww=int(www)
                    except:
                        wwww=www
                    try:
                        qwe.set_index(wwww,inplace=True)
                        print()
                        print('Index sucessfully updated.')
                        wwwww=input('Would you like to print the data?y/n:')
                        if wwwww=='y' or wwwww=='Y':
                            print()
                            print(qwe)
                    except:
                        None
                except:
                    print('Column selected does not exist in the CSV file.')#write correct reason later on
                
        elif op=='g' or op=='G':#change row indexs
            print('a.Give custom index')
            print('b.Increase all indices by a specific number')
            opp=input('Enter your selection here:')
            print()
            if opp=='a' or opp=='A':
                print('a.Reindex file containing total cases and total deaths in all the countries')
                print('b.Reindex file containing trends of covid in Top 10 countries')
                print('c.Reindex file containing misc. infomation like age,population etc. of different countries')
                ww=input('Select the csv file you want to use:')
                if ww=='a' or ww=='A':
                    qwe=dff
                elif ww=='b' or ww=='B':
                    qwe=dft
                elif ww=='c' or ww=='C':
                    qwe=dfm
                print()
                w=input('Do you want to print the rows before selection?y/n:')
                if w=='y' or w=='Y':
                    print(qwe.index)
                    print()
                    print(qwe)

                d={}
                www=int(input('Enter the number of rows you want to reindex:'))
                print()
                for qq in range(www):
                    if qq+1==1:
                        qqq='st'
                    elif qq+1==2:
                        qqq='nd'
                    elif qq+1==3:
                        qqq='rd'
                    elif qq+1<=4:
                        qqq='th'
                    #this detects whether the value passed in the input statement is 'int' or 'str'
                    try:#detects the present index
                        print('Enter index of the',str(qq+1)+qqq+' row you want to change:')
                        aa=input()
                        try:
                            if type(int(aa))==int:
                                a=int(aa)
                        except:
                            a=aa
                    
                    except:
                        a=aa
                    b=input('Enter new index to be kept:')
                    try:#decides the dtype of the new index
                        if type(int(b))==int:
                            b=int(b)
                    except:
                        None#b will remain the same
                    d[a]=b
                    print()
                    
                qwe.rename(index=d,inplace=True)
                
                if www==1:#every detail matters!
                    print('Index sucessfully updated.')
                    wwww=input('Would you like to print the data?y/n')
                    if wwww=='y' or wwww=='Y':
                        print()
                        print(qwe)
                elif www>1:
                    print('Indices sucessfully updated.')#every detail matters!
                    wwww=input('Would you like to print the data?y/n')
                    if wwww=='y' or wwww=='Y':
                        print()
                        print(qwe)

            elif opp=='b' or opp=='B':
                print('a.Reindex file containing total cases and total deaths in all the countries')
                print('b.Reindex file containing trends of covid in Top 10 countries')
                print('c.Reindex file containing misc. infomation like age,population etc. of different countries')
                ww=input('Select the csv file you want to use:')
                if ww=='a' or ww=='A':
                    qwe=dff
                elif ww=='b' or ww=='B':
                    qwe=dft
                elif ww=='c' or ww=='C':
                    qwe=dfm
                print()
                w=input('Do you want to print the rows before selection?y/n:')
                if w=='y' or w=='Y':
                    print(qwe.index)
                    print()
                    print(qwe)
                print()
                try:
                    www=int(input('Enter the number to increase the indices by:'))
                    qwe.index=qwe.index+www
                    print('Indices sucessfully updated.')
                    www=input('Would you like to print the data?y/n')
                    if www=='y' or www=='Y':
                        print(qwe)
                except:
                    print('Invalid entry.')
                    
        elif op=='h' or op=='H':#reset index
            print('a.Reset index of file containing total cases and total deaths in all the countries')
            print('b.Reset index of file containing trends of covid in Top 10 countries')
            print('c.Reset index of file containing misc. infomation like age,population etc. of different countries')
            opp=input('Select the csv file you want to use:')
            if opp=='a' or opp=='A':
                dff.reset_index(inplace=True,drop=True)
                #dff.drop('index',axis=1,inplace=True)#deleting the index column which is created after reseting the index
                print()
                print('Index sucesfully reset.')
                w=input('Would you like to print the data?y/n:')
                if w=='y' or w=='Y':
                    print()
                    print(dff)
                    
            elif opp=='b' or opp=='B':
                dft.reset_index(inplace=True,drop=True)
                dftdrop('index',axis=1,inplace=True)#deleting the index column which is created after reseting the index
                print()
                print('Index sucesfully reset.')
                w=input('Would you like to print the data?y/n:')
                if w=='y' or w=='Y':
                    print()
                    print(dft)
                    
            elif opp=='c' or opp=='C':
                dfm.reset_index(inplace=True,drop=True)
                dfm.drop('index',axis=1,inplace=True)#deleting the index column which is created after reseting the index
                print()
                print('Index sucesfully reset.')
                w=input('Would you like to print the data?y/n:')
                if w=='y' or w=='Y':
                    print()
                    print(dfm)
            
        elif op=='i' or op=='I':#Reorder columns
            print('a.Rordering columns in file containing total cases and total deaths in all the countries')
            print('b.Rordering columns in file containing trends of covid in Top 10 countries')
            print('c.Rordering columns in file cotnaining misc. infomation like age,population etc. of different countries')
            ww=input('Select the csv file you want to use:')
            print()#reorder columns doesnt work with que=df [so the whole program has been written for all 3 csv]
            if ww=='a' or ww=='A':
                w=input('Do you want to print the columns before reordering?y/n:')
                if w=='y' or w=='Y':
                    print(dff.columns)
                    print()
                    print(dff)
                print()
                b=list(dff.columns)#all columns
                n=len(list(dff.columns))
                a=[]#entered by the user
                for qq in range(n):
                    if qq+1==1:
                        qqq='st'
                    elif qq+1==2:
                        qqq='nd'
                    elif qq+1==3:
                        qqq='rd'
                    elif qq+1<=4:
                        qqq='th'
                    print('Enter name of the',str(qq+1)+qqq+' column below:')
                    ww=input()
                    a.append(ww)
                
                garbage_a=[]
                l=[]
                for aq in a:#checkig if the columns entered by the user are actually preset in the data
                    if aq in b:
                        l.append(aq)
                    else:
                        garbage_a.append(aq)
                if len(garbage_a)==1:
                    print('The column \''+str(garbage_a[0])+'\' is not present in the selected csv file therefore it has been removed.')
                elif len(garbage_a)>1:
                    print('The columns',garbage_a,'are not present in the selected csv file therefore they have been removed.')

                garbage_b=[]
                for bq in b:
                    if bq not in a:
                        l.append(bq)
                        garbage_b.append(bq)
                if len(garbage_b)==1:
                    print('Since the position of the column \''+str(garbage_b[0])+'\' is not selected it has been put at the end.')
                elif len(garbage_b)>1:
                    print('Since the position of the columns',garbage_b,'is not selected they have been put at the end.')
                
                #now l has all the column names even if the user has not entered column name which present in the file
                dff=dff.reindex(columns=l)
                print()
                print('Columns successfully reordered.')
                www=input('Do you want to print the data?y/n:')
                if w=='y' or w=='Y':
                    print()
                    print(dff)
                
            elif ww=='b' or ww=='B':
                w=input('Do you want to print the columns before reordering?y/n:')
                if w=='y' or w=='Y':
                    print(dft.columns)
                    print()
                    print(dft)
                print()
                b=list(dft.columns)#all columns
                n=len(list(dft.columns))
                a=[]#entered by the user
                for qq in range(n):
                    if qq+1==1:
                        qqq='st'
                    elif qq+1==2:
                        qqq='nd'
                    elif qq+1==3:
                        qqq='rd'
                    elif qq+1<=4:
                        qqq='th'
                    print('Enter name of the',str(qq+1)+qqq+' column below:')
                    ww=input()
                    a.append(ww)
                
                garbage_a=[]
                l=[]
                for aq in a:#checkig if the columns entered by the user are actually preset in the data
                    if aq in b:
                        l.append(aq)
                    else:
                        garbage_a.append(aq)
                if len(garbage_a)==1:
                    print('The column \''+str(garbage_a[0])+'\' is not present in the selected csv file therefore it has been removed.')
                elif len(garbage_a)>1:
                    print('The columns',garbage_a,'are not present in the selected csv file therefore they have been removed.')

                garbage_b=[]
                for bq in b:
                    if bq not in a:
                        l.append(bq)
                        garbage_b.append(bq)
                if len(garbage_b)==1:
                    print('Since the position of the column \''+str(garbage_b[0])+'\' is not selected it has been put at the end.')
                elif len(garbage_b)>1:
                    print('Since the position of the columns',garbage_b,'is not selected they have been put at the end.')
                
                #now l has all the column names even if the user has not entered column name which present in the file
                dft=dft.reindex(columns=l)
                print()
                print('Columns successfully reordered.')
                www=input('Do you want to print the data?y/n:')
                if w=='y' or w=='Y':
                    print()
                    print(dft)
                
            elif ww=='c' or ww=='C':
                w=input('Do you want to print the columns before reordering?y/n:')
                if w=='y' or w=='Y':
                    print(dfm.columns)
                    print()
                    print(dfm)
                print()
                b=list(dfm.columns)#all columns
                n=len(list(dfm.columns))
                a=[]#entered by the user
                for qq in range(n):
                    if qq+1==1:
                        qqq='st'
                    elif qq+1==2:
                        qqq='nd'
                    elif qq+1==3:
                        qqq='rd'
                    elif qq+1<=4:
                        qqq='th'
                    print('Enter name of the',str(qq+1)+qqq+' column below:')
                    ww=input()
                    a.append(ww)
                
                garbage_a=[]
                l=[]
                for aq in a:#checkig if the columns entered by the user are actually preset in the data
                    if aq in b:
                        l.append(aq)
                    else:
                        garbage_a.append(aq)
                if len(garbage_a)==1:
                    print('The column \''+str(garbage_a[0])+'\' is not present in the selected csv file therefore it has been removed.')
                elif len(garbage_a)>1:
                    print('The columns',garbage_a,'are not present in the selected csv file therefore they have been removed.')
                
                garbage_b=[]
                for bq in b:
                    if bq not in a:
                        l.append(bq)
                        garbage_b.append(bq)
                if len(garbage_b)==1:
                    print('Since the position of the column \''+str(garbage_b[0])+'\' is not selected it has been put at the end.')
                elif len(garbage_b)>1:
                    print('Since the position of the columns',garbage_b,'is not selected they have been put at the end.')
               
                #now l has all the column names even if the user has not entered column name which present in the file
                dfm=dfm.reindex(columns=l)
                print()
                print('Columns successfully reordered.')
                www=input('Do you want to print the data?y/n:')
                if w=='y' or w=='Y':
                    print()
                    print(dfm)


        elif op=='j' or op=='J':#resetting column order to default
                print('a.Reset index of file containing total cases and total deaths in all the countries')
                print('b.Reset index of file containing trends of covid in Top 10 countries')
                print('c.Reset index of file cotnaining misc. infomation like age,population etc. of different countries')
                ww=input('Select the CSV file you want to use:')
                if ww=='a' or ww=='A':
                    dff_new_columns=list(dff.columns)
                    l=[]
                    ll=[]
                    dupe=[]
                    for q in dff_columns:#checking for the presence of default columns incase any column has been deleted
                        if q in dff_new_columns:
                            l.append(q)
                    for qq in l:#removing duplicates if any
                        if qq not in ll: 
                            ll.append(qq)
                        else:
                            dupe.append(qq)
                    try:#if column name has been changed previously then those particular columns will be removed
                        dff=dff[ll]#unfortunately reset index does not work here so instead we assign the columns to the file
                        
                    except:
                        print('ERROR.')
                        print('This error might be caused due to the presence of duplicate column names',dupe,'in the file')

                elif ww=='b' or ww=='B':
                    dft_new_columns=list(dft.columns)
                    l=[]
                    ll=[]
                    dupe=[]
                    for q in dft_columns:
                        if q in dft_new_columns:
                            l.append(q)
                    for qq in l:#removing duplicates if any
                        if qq not in ll: 
                            ll.append(qq)
                        else:
                            dupe.append(qq)
                    try:
                        dft=dft[ll]
                    except:
                        print('ERROR.')
                        print('This error might be caused due to the presence of duplicate column names',dupe,'in the file')

                elif ww=='c' or ww=='C':
                    dfm_new_columns=list(dfm.columns)
                    l=[]
                    ll=[]
                    dupe=[]
                    for q in dfm_columns:
                        if q in dfm_new_columns:
                            ll.append(q)
                    for qq in l:#removing duplicates if any
                        if qq not in ll: 
                            res.append(qq)
                        else:
                            dupe.append(qq)
                    try:
                        dfm=dfm[ll]
                    except:
                        print('ERROR.')
                        print('This error might be caused due to the presence of duplicate column names',dupe,'in the file')

                print()
                print('Column order sucessfully reset.')
                w=input('Would you like to print the data?y/n:')
                if w=='y' or w=='Y':
                    if ww=='a' or ww=='A':
                        print()
                        print(dff)
                    elif ww=='b' or ww=='B':
                        print()
                        print(dft)
                    elif ww=='c' or ww=='C':
                        print()
                        print(dfm)
                            
        elif op=='k' or op=='K':
            menu()
        print()



#module for printing the whole dataframe
def full():
    print()
    print('WARNING:')
    print('If you enable this function the data printed might not make sense since the data used is huge and this process')
    print('is irreversible. If you wish to revert this, it can only be done by restarting the whole program.')
    print('Enabling this might make your system extremely slow while printing the data and might lead to python crashing.')
    qq=input('Press y to continue:')
    if qq=='y' or qq=='Y' or qq=='yes' or qq=='Yes':
        pd.set_option("display.max_rows", None, "display.max_columns", None)
        print()
        print('Now onwards the whole dataframe will be printed without being truncated.')
        print()
        qqq=input('Do you want to print the data? y/n')
        if qqq=='y' or qqq=='Y':
            print('Main file containing data about all the countries[dff]:')
            print(dff)
            print()
            print('File containing trends of covid in Top 10 countries[dft]:')
            print(dft)
            print()
            print('File containing misc. infomation like age,population etc. of different countries[dfm]:')
            print(dfm)


def insert_file():
    global dff_raw,for_top10,dff,dft,dff_temp,dfm,dffg,dfmg,dftg,nop
    print()
    print('a.Update main file containing data about all the countries')
    print('b.Update file containing trends of covid in Top 10 countries')
    print('c.Update file containing misc. infomation like age,population etc. of different countries')
    print('d.Update all three files')
    qq=input('Enter your selection here:')
    print()
    print('Do you want to be redirected to the csv file site?')
    w=input('[Internet connection required].y/n:')
    print()
    if w=='y' or w=='Y':
        print(webbrowser.open('https://covid.ourworldindata.org/data/owid-covid-data.csv'))
        print()
    ww=input('Enter path of folder containing the CSV file:')
    if bool(ww)==True or ww!='':
        ww.encode('unicode_escape')#this is used to convert the escape sequence characters formed by the path eg.\n 
        nam=input('Enter the name of the CSV file:')
        www=(ww+'\\'+nam+'.csv')
        try:
            check_valid = pd.read_csv(www)
            tdate=str(date.today())#getting todays date
            ydate=str(date.today()-timedelta(days=3))#getting yesterdays date. Change has been made here to download data 
            dfdate=max(check_valid['date'])          #12 hours prior and store data for taking to school for presentation 
            #this checks todays and yesterdays date incase if the user runs this fuction after 11:59PM the computer takes
            #tomorrows date and the csv file sometimes isnt updated to the current date so just for extra flexibility it
            #checks for 2 dates i.e today and yesterday. This can be manually changed/increased to force apply data
            if tdate==dfdate or dfdate>=ydate:
                if qq=='a':
                    dff = pd.read_csv(www)
                    cleanup_dff()
                    dff_columns=list(dff.columns)
                    dff_raw = pd.read_csv(www)
                    dff=dff.fillna(0)#replacing Nan values with zero
                    dff['total_cases']=dff['total_cases'].astype(int)#converting float(deciaml) values to int
                    dff['total_deaths']=dff['total_deaths'].astype(int)#converting float(deciaml) values to int
                    nop=0
                    dffg=dff.copy()
                    dffg['total_cases'] = dffg['total_cases'].abs()
                    dffg['total_deaths'] = dffg['total_deaths'].abs()
                    for_top10=dffg.copy()
                elif qq=='b':
                    dff_temp=pd.read_csv(www)
                    dft = pd.read_csv(www)
                    cleanup_dff_temp()#since dff is used to create dft and dff is not being updated we create a temporary 
                    cleanup_dft()     #file [dff_temp] for forming dft
                    dft_columns=list(dft.columns)
                    dft=dft.fillna(0)#replacing Nan values with zero
                    dft['new_cases']=dft['new_cases'].astype(int)#converting float(deciaml) values to int
                    dft['new_deaths']=dft['new_deaths'].astype(int)#converting float(deciaml) values to int
                    nop=0
                    dftg=dft.copy()
                    dftg['new_cases'] = dftg['new_cases'].abs()#converting negative values into positive if any
                    dftg['new_deaths'] = dftg['new_deaths'].abs()#converting negative values into positive if any
                    #converting date column calues to dtype = datetime
                    dftg['date'] = pd.to_datetime(dftg['date'])
                    dftg.drop(dftg[dftg['date']<'3/11/2020'].index,inplace=True)#dropping some rows to match all the country data
                elif qq=='c':
                    dfm = pd.read_csv(www)
                    cleanup_dfm()
                    dfm_columns=list(dfm.columns)
                    dfm=dfm.fillna(0)#float values are kept here
                    nop=0
                    dfmg=dfm.copy()
                elif qq=='d':
                    dff = pd.read_csv(www)
                    dff_raw = pd.read_csv(www)
                    dft = pd.read_csv(www)
                    dfm = pd.read_csv(www)
                    cleanup_dff()
                    cleanup_dft()
                    cleanup_dfm()
                    dff_columns=list(dff.columns)
                    dft_columns=list(dft.columns)
                    dfm_columns=list(dfm.columns)
                    dff_raw = pd.read_csv(www)
                    dff=dff.fillna(0)#replacing Nan values with zero
                    dff['total_cases']=dff['total_cases'].astype(int)#converting float(deciaml) values to int
                    dff['total_deaths']=dff['total_deaths'].astype(int)#converting float(deciaml) values to int
                    dft=dft.fillna(0)#replacing Nan values with zero
                    dft['new_cases']=dft['new_cases'].astype(int)#converting float(deciaml) values to int
                    dft['new_deaths']=dft['new_deaths'].astype(int)#converting float(deciaml) values to int
                    dfm=dfm.fillna(0)#float values are kept here
                    nop=0
                    
                    #following data is for graphs
                    dffg=dff.copy()
                    dftg=dft.copy()
                    dfmg=dfm.copy()
                    dffg['total_cases'] = dffg['total_cases'].abs()
                    dffg['total_deaths'] = dffg['total_deaths'].abs()
                    dftg['new_cases'] = dftg['new_cases'].abs()#converting negative values into positive if any
                    dftg['new_deaths'] = dftg['new_deaths'].abs()#converting negative values into positive if any
                    for_top10=dffg.copy()
                    #converting date column calues to dtype = datetime
                    dftg['date'] = pd.to_datetime(dftg['date'])
                    dftg.drop(dftg[dftg['date']<'3/11/2020'].index,inplace=True)#dropping some rows to match all the country data
                    
                print()
                print('Data updated.')
                wwww=input('Would you like to print the data?y/n:')
                print()
                if wwww=='y' or wwww=='Y':
                    if qq=='a' or qq=='A':
                        print('Main file containing data about all the countries[dff]:')
                        print(dff)
                    elif qq=='b' or qq=='B':
                        print('File containing trends of covid in Top 10 countries[dft]:')
                        print(dft)
                    elif qq=='c' or qq=='C':
                        print('File containing misc. infomation like age,population etc. of different countries[dfm]:')
                        print(dfm)
                        
                    elif qq=='d' or qq=='D':
                        print('Main file containing data about all the countries[dff]:')
                        print(dff)
                        print()
                        print('File containing trends of Covid-19 in Top 10 countries[dft]:')
                        print(dft)
                        print()
                        print('File containing miscellaneous infomation like age,population etc. of different countries[dfm]:')
                        print(dfm)
            else:
                #if the data used is not recenly downloaded it will result in an error because while the fuction forms the
                #required dataframes it keeps data of 2 days ago therefore if the data isnt downloaded today it will lead
                #to an error
                print('ERROR.')
                print('Please download the csv file again and try performing this function again.')
        except:
            print()
            print('ERROR.')
            print('Invalid path')

#Module for forming the dff data from the downloaded data
def cleanup_dff():
    global dff_raw,for_top10,dff,dft,dff_temp,dfm
    from datetime import date,timedelta
    a=str(date.today()-timedelta(days=7))#getting day before yesterdays date
    qq=dff.index[dff['date'] != a]#getting the index of rows that do not contain the required date
    dff.drop(qq,inplace=True)#deleting the dows that do not contain the required date
    aq=['continent','location','total_cases','total_deaths']#this has the column names to be kept
    beth=list(dff.columns)#this contains all the column names

    lll=[]#here we basically remove the column names to be kept from all the column names
    for ab in beth:
        if ab in aq:
            continue
        else:
            lll.append(ab)

    dff.drop(lll,axis=1,inplace=True)#deleting the unnecessary columns
    dff.reset_index(inplace=True)#reseting the index after deleting rows
    dff.drop('index',axis=1,inplace=True)#deleting the index column that was created after reseting the index
    qqq=dff.index[dff['location']=='World']#getting index of the world row
    dff.drop(qqq,inplace=True)#deleting unwanted world row
    qqq=dff.index[dff['location']=='International']#getting index of the International row
    dff.drop(qqq,inplace=True)#deleting unwanted Internationl row
    
    #list of location names to be deleted since these are not country names
    a=['Asia','Europe','Africa','North America','South America','Oceania']
    for con in range(len(a)):
        q=dff.index[dff['location']==a[con]]
        dff.drop(q,inplace=True)#deleting unwanted continent row    for_top10 = dff.copy()



#Module for forming the dft data from the downloaded data without resetting the dff data
def cleanup_dff_temp():
    global dff_raw,for_top10,dff,dft,dff_temp,dfm
    a=str(date.today()-timedelta(days=7))#getting day before yesterdays date
    qq=dff_temp.index[dff_temp['date'] != a]#getting the index of rows that do not contain the required date
    dff_temp.drop(qq,inplace=True)#deleting the dows that do not contain the required date
    dff_temp.reset_index(inplace=True)#reseting the index after deleting rows
    dff_temp.drop('index',axis=1,inplace=True)#deleting the index column that was created after reseting the index
    qqq=dff_temp.index[dff_temp['location']=='World']#getting index of the world row
    dff_temp.drop(qqq,inplace=True)#deleting unwanted world row
    qqq=dff_temp.index[dff_temp['location']=='International']#getting index of the Internationl row
    dff_temp.drop(qqq,inplace=True)#deleting unwanted Internationl row
    #list of location names to be deleted since these are not country names
    a=['Asia','Europe','Africa','North America','South America','Oceania']
    for con in range(len(a)):
        q=dff.index[dff['location']==a[con]]
        dff.drop(q,inplace=True)#deleting unwanted continent row    for_top10 = dff.copy()
    for_top10 = dff_temp.copy()


#Module for forming DFT data from the downloaded csv file
def cleanup_dft():
    global dff_raw,for_top10,dff,dft,dff_temp,dfm
    #here we use the dff_raw,dft,for_top10 already made in the previous module
    for_top10.sort_values('total_cases',ascending=False,inplace=True)
    for_top10.reset_index(inplace=True)#reseting the index after deleting rows
    for_top10.drop('index',axis=1,inplace=True)#deleting the index column that was created after reseting the index

    aq=['continent','location','date','new_cases','new_deaths']#this has the column names to be kept
    beth=list(dft.columns)#this contains all the column names

    lll=[]#here we basically remove the column names to be kept from all the column names
    for ab in beth:
        if ab in aq:
            continue
        else:
            lll.append(ab)

    dft.drop(lll,axis=1,inplace=True)#deleting the unnecessary columns

    qop=len(for_top10)#this has the total nunber of countries
    l=[]
    for qqq in range(qop-10):#the loop repeats 10 times less so it keeps the top 10 countries
        l.append(qqq+10)#this begins insert index from 11th country 


    for_top10.drop(l,inplace=True)#dropping the countries which are not in the top 10
    qqqq=for_top10['location']#assigning only the country names to qqqq
    awe=qqqq[0]

    
    dft1=dft[dft['location']==qqqq[0]]#first country
    dft2=dft[dft['location']==qqqq[1]]#second country
    dft3=dft[dft['location']==qqqq[2]]#third country
    dft4=dft[dft['location']==qqqq[3]]#forth country
    dft5=dft[dft['location']==qqqq[4]]#fifth country
    dft6=dft[dft['location']==qqqq[5]]#sixth country
    dft7=dft[dft['location']==qqqq[6]]#seventh country
    dft8=dft[dft['location']==qqqq[7]]#eigth country
    dft9=dft[dft['location']==qqqq[8]]#ninth country
    dft10=dft[dft['location']==qqqq[9]]#tenth country
    
    
    dft=pd.concat([dft1,dft2,dft3,dft4,dft5,dft6,dft7,dft8,dft9,dft10])#concatinating all the countries together
    dft.reset_index(inplace=True)#restting index
    dft.drop('index',axis=1,inplace=True)#deleting the column formed by resetting the index

    dft=dft.fillna(0)#replacing Nan values with zero
    dft['new_cases']=dft['new_cases'].astype(int)#converting float(deciaml) values to int
    dft['new_deaths']=dft['new_deaths'].astype(int)#converting float(deciaml) values to int


#Module for forming dfm data from the downloaded csv file
def cleanup_dfm():
    global dff_raw,for_top10,dff,dft,dff_temp,dfm
    from datetime import date,timedelta
    a=str(date.today()-timedelta(days=7))#getting day before yesterdays date
    qq=dfm.index[dfm['date'] != a]#getting the index of rows that do not contain the required date
    dfm.drop(qq,inplace=True)#deleting the dows that do not contain the required date
    
    aq=['continent','location','stringency_index','population','median_age','gdp_per_capita','cardiovasc_death_rate',\
        'diabetes_prevalence','female_smokers','male_smokers','handwashing_facilities','hospital_beds_per_thousand',\
        'life_expectancy','human_development_index']#this has the column names to be kept
    beth=list(dfm.columns)#this contains all the column names

    lll=[]#here we basically remove the column names to be kept from all the column names
    for ab in beth:
        if ab in aq:
            continue
        else:
            lll.append(ab)

    dfm.drop(lll,axis=1,inplace=True)#deleting the unnecessary columns

    dfm.reset_index(inplace=True)#reseting the index after deleting rows
    dfm.drop('index',axis=1,inplace=True)#deleting the index column that was created after reseting the index
    qqq=dfm.index[dfm['location']=='World']#getting index of the world row
    dfm.drop(qqq,inplace=True)#deleting unwanted world row
    qqq=dfm.index[dfm['location']=='International']#getting index of the International row
    dfm.drop(qqq,inplace=True)#deleting unwanted International row
    #list of location names to be deleted since these are not country names
    a=['Asia','Europe','Africa','North America','South America','Oceania']
    for con in range(len(a)):
        q=dff.index[dff['location']==a[con]]
        dfm.drop(q,inplace=True)#deleting unwanted continent row    for_top10 = dff.copy()
    dfm=dfm.fillna(0)#replacing Nan values with zero


def details():
    print('Project topic - COVID 19')
    print()
    print('The Covid-19 data used is the data avaliable till 01/01/2021 and was downloaded from \'ourworldindata.org\'.')
    print('You can update the csv files with the latest data by going into extras and Instering new csv data.')
    print()
    print('This project uses 3 CSV files which can also be updated when you insert new data.')
    print('The files that this project uses are:')
    print()
    print('a) DFF [Dataframe final]')
    print('Contains data like total cases, deaths in all the countries as on 01-01-2021')
    print()
    print('b) DFT [Dataframe trends]')
    print('Contains data like Daily cases, deaths in Top 10 countries with highest cases')
    print('The daily deaths data taken starts from 03-11-2020')
    print()
    print('c) DFM [Dataframe miscellaneous]')
    print('Contains miscellaneous data about all the countries like population, life expectancy, male smokers, etc.')
    print()
    print('This program is written with efficiency in mind as no column names, etc are specified.')
    print('The program automatically finds column names, datatypes of the selected columns and adapts to suitable-')
    print('ways of performing the required function.')
    print()
    print('Any change made to the data under Manipulation will be shown under Analysis.')
    print()
    print('While entering your selection your selection is n/no then you can insted just press ENTER[↵]')


def reset_data():
    global dff,dft,dfm
    dff=pd.read_csv('finaldata.csv')
    dfm=pd.read_csv('miscdata.csv')
    dft=pd.read_csv('top10.csv')
    print('Data sucessfully reset.')
    qqq=input('Do you want to print the data? y/n')
    if qqq=='y' or qqq=='Y':
        print()
        print('Main file containing data about all the countries[dff]:')
        print(dff)
        print()
        print('File containing trends of covid in Top 10 countries[dft]:')
        print(dft)
        print()
        print('File containing misc. infomation like age,population etc. of different countries[dfm]:')
        print(dfm)
    #these are used for resetting the column names to default
    dff_columns=list(dff.columns)
    dft_columns=list(dft.columns)
    dfm_columns=list(dfm.columns)
    
    
    dff=dff.fillna(0)#replacing Nan values with zero
    dff['total_cases']=dff['total_cases'].astype(int)#converting float(decimal) values to int
    dff['total_deaths']=dff['total_deaths'].astype(int)#converting float(decimal) values to int
    dft=dft.fillna(0)#replacing Nan values with zero
    dft['new_cases']=dft['new_cases'].astype(int)#converting float(decimal) values to int
    dft['new_deaths']=dft['new_deaths'].astype(int)#converting float(decimal) values to int
    dfm=dfm.fillna(0)#float values are kept here
    
    dffg['total_cases'] = dffg['total_cases'].abs()
    dffg['total_deaths'] = dffg['total_deaths'].abs()
    dftg['new_cases'] = dftg['new_cases'].abs()#converting negative values into positive if any
    dftg['new_deaths'] = dftg['new_deaths'].abs()#converting negative values into positive if any
    
    for_top10=dffg.copy()
    #converting date column values to dtype = datetime
    dftg['date'] = pd.to_datetime(dftg['date'])
    dftg.drop(dftg[dftg['date']<'3/11/2020'].index,inplace=True)#dropping some rows to match all the country data





def extras():
    global dff,dft,dfm,saa,title_option,graph_option,path,fmt #This is suppose to be given because we are editing the csv data here
    while True:
        print()
        print('\n一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一')
        print('                                            EXTRAS')
        print('一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一一')
        print('a.Insert CSV data')
        print('b.Reset to default CSV data')
        print('c.Change title of the project')
        print('d.Print full/untruncated data')
        
        if title_option==True:#to detect weather title animation if acitve or not
            print('e.Turn off Project Title animation')
        elif title_option==False:#to detect weather title animation if inactive or not
            print('e.Turn on Project Title animation')
        
        print('f.Details about the project')
        
        if graph_option==True:#to detect weather save fig is acitve or not
            print('g.Turn off graph saving')
            print('h.Go back to main menu')
        elif graph_option==False:#to detect weather save fig is inactive or not
            print('g.Turn on graph saving')
            print('h.Go back to main menu')
            
        elif graph_option==None:#to detect weather save fig is inactive or not
            print('g.Go back to main menu')
        
        op=input('Enter your selection:')
        print()
        if op=='a' or op=='A':
            insert_file()
        elif op=='b' or op=='B':
            reset_data()
        elif op=='c' or op=='C':
            global title_op
            print()
            title_op='y'
            title()
            print('Title sucessfully updated.')
        elif op=='d' or op=='D':
            full()
        elif op=='e' or op=='E':
            if title_option==True:
                title_option=False #disabling animation
                print('Project title animation deactivated.')
            elif title_option==False:
                title_option=True #re-enabling animation
                print('Project title animation reactivated.')
        elif op=='f' or op=='F':
            details()
            
        elif graph_option==True and (op=='g' or op=='G'):
            graph_option=False
            saa=None #disabling graph saving
            print('Graph saving sucessfully disabled')
        
        elif graph_option==False and (op=='g' or op=='G'):
            #paste from visualisation
            print('a.Specify a folder for saving the graphs')
            print('b.Autosave to folder containing the python project file')
            saa=input('Enter your selection:')
            print()
            if saa=='a' or saa=='A':
                path=input('Enter path of the folder you want to save the graphs to:')
                path.encode('unicode_escape')
                print()
                print('Would you like to specify the format in which the graph is to be saved?')
                saaa=input('If no then the default format is JPEG.?y/n:')
                if saaa=='y' or saaa=='Y':
                    graph_option=True
                    print('a.PNG')
                    print('b.PDF')
                    print('c.SVG')
                    print('d.RAW')
                    print('e.JPG')
                    print('f.JPEG')
                    f=input('Enter your selection:')
                    if f=='a' or f=='A':
                        fmt='png'
                    elif f=='b' or f=='B':
                        fmt='pdf'
                    elif f=='c' or f=='C':
                        fmt='svg'
                    elif f=='d' or f=='D':
                        fmt='raw'
                    elif f=='e' or f=='E':
                        fmt='jpg'
                    elif f=='f' or f=='F':
                        fmt='jpeg'
                elif saaa!='y' or saaa!='Y':
                    graph_option=True
                    fmt='jpg'#since this is the format most widley seen
                print('Graph saving sucessfully re-enabled')
            elif saa=='b' or saa=='B':
                graph_option=True
                fmt='jpg'
                print('Graph saving sucessfully re-enabled')
        
        elif graph_option==None and (op=='g' or op=='G'):
            print()
            menu()
        elif (graph_option==True or graph_option==False) and (op=='h' or op=='H'):
            print()
            menu()
        print()






#Menu module
def menu():
    while True:
        print()
        print('«|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦»')
        if title_option==True:
            typewriter(i)
            print('\n«|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦»')
        else:
            print(i)
            print('«|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦|¦»')
        print('1.Visualisation')
        print('2.Analysis')
        print('3.Manipulation')
        print('4.Extras')
        print('5.Exit')
        try: 
            opt=int(input('Enter your selection:'))
        except:
            print()
            continue
        if opt==1:
            visualisation()
        elif opt==2:
            analysis()
        elif opt==3:
            manipulation()
        elif opt==4:
            extras()
        elif opt==5:
            ext=input('If you exit, python idle will be closed. Do you want to continue?y/n:')
            if ext=='y' or ext=='Y':
                quit()
        print()
    if opt!=5:
        print('Invalid selection.')
        print()
        menu()


menu()
#creator/owner XII-D
#orignal piece of work
#2020-2021
#Total lines of code- 3945 lines
