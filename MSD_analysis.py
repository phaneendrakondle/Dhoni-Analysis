#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
pip install matplotlib
import matplotlib.pyplot as plt

#to display all rows columns 
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)  
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)


# In[ ]:


df=pd.read_csv('drive/MyDrive/Colab Notebooks/IPL_ball_by_ball_updated.csv')


# In[ ]:


dhoni_sixes=pd.DataFrame(df[(df.striker=='MS Dhoni')&(df.runs_off_bat==6)].groupby('season')['runs_off_bat'].count())
dhoni_fours=pd.DataFrame(df[(df.striker=='MS Dhoni')&(df.runs_off_bat==4)].groupby('season')['runs_off_bat'].count())
dhoni_runs=pd.DataFrame(df[(df.striker=='MS Dhoni')].groupby('season')['runs_off_bat'].sum())
dhoni_balls=pd.DataFrame(df[(df.striker=='MS Dhoni')].groupby('season')['ball'].count())
dhoni_stats=dhoni_runs.merge(dhoni_balls,on='season')
dhoni_stats=dhoni_stats.merge(dhoni_fours,on='season')
dhoni_stats=dhoni_stats.merge(dhoni_sixes,on='season')
dhoni_stats.rename(columns = {'runs_off_bat_x':'Runs_Scored','ball':'Balls_Faced','runs_off_bat_y':'Fours','runs_off_bat':'Sixes'}, inplace = True)
dhoni_stats['strike_rate']=100*dhoni_stats['Runs_Scored']/dhoni_stats['Balls_Faced']
dhoni_stats


# **Insights from above data collected :**
# Since past couple of years, his strike rate is below 130 which indicates that his performance is low. All we know that he's a great finisher. Let's analyze his finishing skills.

# In[ ]:


dhoni_death_sixes=pd.DataFrame(df[(df.striker=='MS Dhoni')&(df.runs_off_bat==6)&(df.ball>16)].groupby('season')['runs_off_bat'].count())
dhoni_death_fours=pd.DataFrame(df[(df.striker=='MS Dhoni')&(df.runs_off_bat==4)&(df.ball>16)].groupby('season')['runs_off_bat'].count())
dhoni_death_runs=pd.DataFrame(df[(df.striker=='MS Dhoni')&(df.ball>16)].groupby('season')['runs_off_bat'].sum())
dhoni_death_balls=pd.DataFrame(df[(df.striker=='MS Dhoni')&(df.ball>16)].groupby('season')['ball'].count())
dhoni_death_stats=dhoni_death_runs.merge(dhoni_death_balls,on='season')
dhoni_death_stats=dhoni_death_stats.merge(dhoni_death_fours,on='season')
dhoni_death_stats=dhoni_death_stats.merge(dhoni_death_sixes,on='season')
dhoni_death_stats.rename(columns = {'runs_off_bat_x':'Runs_Scored_death','ball':'Balls_Faced_death','runs_off_bat_y':'Fours_death','runs_off_bat':'Sixes_death'}, inplace = True)
dhoni_death_stats['strike_rate_death']=100*dhoni_death_stats['Runs_Scored_death']/dhoni_death_stats['Balls_Faced_death']
dhoni_death_stats['Boundaries_death']=dhoni_death_stats['Fours_death']+dhoni_death_stats['Sixes_death']
dhoni_death_stats['Balls_per_bdry_death']=dhoni_death_stats['Balls_Faced_death']/dhoni_death_stats['Boundaries_death']
dhoni_death_stats


# In[ ]:


pandya_death_sixes=pd.DataFrame(df[(df.striker=='HH Pandya')&(df.runs_off_bat==6)&(df.ball>16)].groupby('season')['runs_off_bat'].count())
pandya_death_fours=pd.DataFrame(df[(df.striker=='HH Pandya')&(df.runs_off_bat==4)&(df.ball>16)].groupby('season')['runs_off_bat'].count())
pandya_death_runs=pd.DataFrame(df[(df.striker=='HH Pandya')&(df.ball>16)].groupby('season')['runs_off_bat'].sum())
pandya_death_balls=pd.DataFrame(df[(df.striker=='HH Pandya')&(df.ball>16)].groupby('season')['ball'].count())
pandya_death_stats=pandya_death_runs.merge(pandya_death_balls,on='season')
pandya_death_stats=pandya_death_stats.merge(pandya_death_fours,on='season')
pandya_death_stats=pandya_death_stats.merge(pandya_death_sixes,on='season')
pandya_death_stats.rename(columns = {'runs_off_bat_x':'Runs_Scored_death','ball':'Balls_Faced_death','runs_off_bat_y':'Fours_death','runs_off_bat':'Sixes_death'}, inplace = True)
pandya_death_stats['strike_rate_death']=100*pandya_death_stats['Runs_Scored_death']/pandya_death_stats['Balls_Faced_death']
pandya_death_stats['Boundaries_death']=pandya_death_stats['Fours_death']+pandya_death_stats['Sixes_death']
pandya_death_stats['Balls_per_bdry_death']=pandya_death_stats['Balls_Faced_death']/pandya_death_stats['Boundaries_death']
pandya_death_stats


# In[ ]:


russell_death_sixes=pd.DataFrame(df[(df.striker=='AD Russell')&(df.runs_off_bat==6)&(df.ball>16)].groupby('season')['runs_off_bat'].count())
russell_death_fours=pd.DataFrame(df[(df.striker=='AD Russell')&(df.runs_off_bat==4)&(df.ball>16)].groupby('season')['runs_off_bat'].count())
russell_death_runs=pd.DataFrame(df[(df.striker=='AD Russell')&(df.ball>16)].groupby('season')['runs_off_bat'].sum())
russell_death_balls=pd.DataFrame(df[(df.striker=='AD Russell')&(df.ball>16)].groupby('season')['ball'].count())
russell_death_stats=russell_death_runs.merge(russell_death_balls,on='season')
russell_death_stats=russell_death_stats.merge(russell_death_fours,on='season')
russell_death_stats=russell_death_stats.merge(russell_death_sixes,on='season')
russell_death_stats.rename(columns = {'runs_off_bat_x':'Runs_Scored_death','ball':'Balls_Faced_death','runs_off_bat_y':'Fours_death','runs_off_bat':'Sixes_death'}, inplace = True)
russell_death_stats['strike_rate_death']=100*russell_death_stats['Runs_Scored_death']/russell_death_stats['Balls_Faced_death']
russell_death_stats['Boundaries_death']=russell_death_stats['Fours_death']+russell_death_stats['Sixes_death']
russell_death_stats['Balls_per_bdry_death']=russell_death_stats['Balls_Faced_death']/russell_death_stats['Boundaries_death']
russell_death_stats


# In[ ]:


pollard_death_sixes=pd.DataFrame(df[(df.striker=='KA Pollard')&(df.runs_off_bat==6)&(df.ball>16)].groupby('season')['runs_off_bat'].count())
pollard_death_fours=pd.DataFrame(df[(df.striker=='KA Pollard')&(df.runs_off_bat==4)&(df.ball>16)].groupby('season')['runs_off_bat'].count())
pollard_death_runs=pd.DataFrame(df[(df.striker=='KA Pollard')&(df.ball>16)].groupby('season')['runs_off_bat'].sum())
pollard_death_balls=pd.DataFrame(df[(df.striker=='KA Pollard')&(df.ball>16)].groupby('season')['ball'].count())
pollard_death_stats=pollard_death_runs.merge(pollard_death_balls,on='season')
pollard_death_stats=pollard_death_stats.merge(pollard_death_fours,on='season')
pollard_death_stats=pollard_death_stats.merge(pollard_death_sixes,on='season')
pollard_death_stats.rename(columns = {'runs_off_bat_x':'Runs_Scored_death','ball':'Balls_Faced_death','runs_off_bat_y':'Fours_death','runs_off_bat':'Sixes_death'}, inplace = True)
pollard_death_stats['strike_rate_death']=100*pollard_death_stats['Runs_Scored_death']/pollard_death_stats['Balls_Faced_death']
pollard_death_stats['Boundaries_death']=pollard_death_stats['Fours_death']+pollard_death_stats['Sixes_death']
pollard_death_stats['Balls_per_bdry_death']=pollard_death_stats['Balls_Faced_death']/pollard_death_stats['Boundaries_death']
pollard_death_stats


# In[ ]:


abd_death_sixes=pd.DataFrame(df[(df.striker=='AB de Villiers')&(df.runs_off_bat==6)&(df.ball>16)].groupby('season')['runs_off_bat'].count())
abd_death_fours=pd.DataFrame(df[(df.striker=='AB de Villiers')&(df.runs_off_bat==4)&(df.ball>16)].groupby('season')['runs_off_bat'].count())
abd_death_runs=pd.DataFrame(df[(df.striker=='AB de Villiers')&(df.ball>16)].groupby('season')['runs_off_bat'].sum())
abd_death_balls=pd.DataFrame(df[(df.striker=='AB de Villiers')&(df.ball>16)].groupby('season')['ball'].count())
abd_death_stats=abd_death_runs.merge(abd_death_balls,on='season')
abd_death_stats=abd_death_stats.merge(abd_death_fours,on='season')
abd_death_stats=abd_death_stats.merge(abd_death_sixes,on='season')
abd_death_stats.rename(columns = {'runs_off_bat_x':'Runs_Scored_death','ball':'Balls_Faced_death','runs_off_bat_y':'Fours_death','runs_off_bat':'Sixes_death'}, inplace = True)
abd_death_stats['strike_rate_death']=100*abd_death_stats['Runs_Scored_death']/abd_death_stats['Balls_Faced_death']
abd_death_stats['Boundaries_death']=abd_death_stats['Fours_death']+abd_death_stats['Sixes_death']
abd_death_stats['Balls_per_bdry_death']=abd_death_stats['Balls_Faced_death']/abd_death_stats['Boundaries_death']
abd_death_stats


# In[ ]:


pant_death_sixes=pd.DataFrame(df[(df.striker=='RR Pant')&(df.runs_off_bat==6)&(df.ball>16)].groupby('season')['runs_off_bat'].count())
pant_death_fours=pd.DataFrame(df[(df.striker=='RR Pant')&(df.runs_off_bat==4)&(df.ball>16)].groupby('season')['runs_off_bat'].count())
pant_death_runs=pd.DataFrame(df[(df.striker=='RR Pant')&(df.ball>16)].groupby('season')['runs_off_bat'].sum())
pant_death_balls=pd.DataFrame(df[(df.striker=='RR Pant')&(df.ball>16)].groupby('season')['ball'].count())
pant_death_stats=pant_death_runs.merge(pant_death_balls,on='season')
pant_death_stats=pant_death_stats.merge(pant_death_fours,on='season')
pant_death_stats=pant_death_stats.merge(pant_death_sixes,on='season')
pant_death_stats.rename(columns = {'runs_off_bat_x':'Runs_Scored_death','ball':'Balls_Faced_death','runs_off_bat_y':'Fours_death','runs_off_bat':'Sixes_death'}, inplace = True)
pant_death_stats['strike_rate_death']=100*pant_death_stats['Runs_Scored_death']/pant_death_stats['Balls_Faced_death']
pant_death_stats['Boundaries_death']=pant_death_stats['Fours_death']+pant_death_stats['Sixes_death']
pant_death_stats['Balls_per_bdry_death']=pant_death_stats['Balls_Faced_death']/pant_death_stats['Boundaries_death']
pant_death_stats


# In[ ]:


dff=pd.merge(dhoni_death_stats.Balls_per_bdry_death,pant_death_stats.Balls_per_bdry_death,how='left',on='season')
dff.rename(columns = {'Balls_per_bdry_death_x':'DHONI','Balls_per_bdry_death_y':'PANT'}, inplace = True)
dff=pd.merge(dff,abd_death_stats.Balls_per_bdry_death,how='left',on='season')
dff=pd.merge(dff,pandya_death_stats.Balls_per_bdry_death,how='left',on='season')
dff.rename(columns = {'Balls_per_bdry_death_x':'ABD','Balls_per_bdry_death_y':'HARDIK'}, inplace = True)
dff=pd.merge(dff,pollard_death_stats.Balls_per_bdry_death,how='left',on='season')
dff=pd.merge(dff,russell_death_stats.Balls_per_bdry_death,how='left',on='season')
dff.rename(columns = {'Balls_per_bdry_death_x':'POLLARD','Balls_per_bdry_death_y':'RUSSELL'}, inplace = True)

dff


# Above we have got the data about the balls per boundary by few of the top finishers  ABD,PANT,RUSSELL,PANDYA,POLLY. Among all these we can clearly see that the balls per boundary around 3 indicates a sublime form of finishing the innings but unlike this, dhoni never been to that figure in his career. So, let's analyze his strike rate as well.

# In[ ]:


death_17runs=pd.DataFrame(df[(df.ball>16)&(df.ball<17)&(df.striker=='MS Dhoni')].groupby('season')['runs_off_bat'].sum())
death_17balls=pd.DataFrame(df[(df.ball>16)&(df.ball<17)&(df.striker=='MS Dhoni')].groupby('season')['ball'].count())
death_17out=pd.DataFrame(df[(df.ball>16)&(df.ball<17)&(df.striker=='MS Dhoni')&((df.wicket_type=='caught')|(df.wicket_type=='caught and bowled')|(df.wicket_type=='stumped')|(df.wicket_type=='bowled')|(df.wicket_type=='lbw'))].groupby('season')['wicket_type'].count())
death_17runs.rename(columns={'runs_off_bat':'over_17_runs'},inplace=True)
death_17balls.rename(columns={'ball':'over_17_balls'},inplace=True)
death_17_stats=death_17runs.merge(death_17balls,on='season')
death_17_stats['SR']=100*death_17_stats['over_17_runs']/death_17_stats['over_17_balls']
death_17_stats = pd.merge(death_17_stats, death_17out, how='left', on='season')
death_17_stats


# In[ ]:


ax = plt.gca()
death_17_stats.plot(kind = 'bar',
        y = 'SR',
        color = 'green',ax = ax)
plt.show()


# **Overs 17 :** we can see that his strike rate in past five seasons is not impressive

# In[ ]:


death_18runs=pd.DataFrame(df[(df.ball>17)&(df.ball<18)&(df.striker=='MS Dhoni')].groupby('season')['runs_off_bat'].sum())
death_18balls=pd.DataFrame(df[(df.ball>17)&(df.ball<18)&(df.striker=='MS Dhoni')].groupby('season')['ball'].count())
death_18out=pd.DataFrame(df[(df.ball>17)&(df.ball<18)&(df.striker=='MS Dhoni')&((df.wicket_type=='caught')|(df.wicket_type=='caught and bowled')|(df.wicket_type=='stumped')|(df.wicket_type=='bowled')|(df.wicket_type=='lbw'))].groupby('season')['wicket_type'].count())
death_18runs.rename(columns={'runs_off_bat':'over_18_runs'},inplace=True)
death_18balls.rename(columns={'ball':'over_18_balls'},inplace=True)
death_18_stats=death_18runs.merge(death_18balls,on='season')
death_18_stats['SR']=100*death_18_stats['over_18_runs']/death_18_stats['over_18_balls']
death_18_stats = pd.merge(death_18_stats, death_18out, how='left', on='season')
death_18_stats


# In[ ]:


ax = plt.gca()
death_18_stats.plot(kind = 'bar',
        y = 'SR',
        color = 'green',ax = ax)
plt.show()


# **Over 18 :** Strike Rate hardly touches 140 to 150 in over 18 which is considerable.

# In[ ]:


death_19runs=pd.DataFrame(df[(df.ball>18)&(df.ball<19)&(df.striker=='MS Dhoni')].groupby('season')['runs_off_bat'].sum())
death_19balls=pd.DataFrame(df[(df.ball>18)&(df.ball<19)&(df.striker=='MS Dhoni')].groupby('season')['ball'].count())
death_19out=pd.DataFrame(df[(df.ball>18)&(df.ball<19)&(df.striker=='MS Dhoni')&((df.wicket_type=='caught')|(df.wicket_type=='caught and bowled')|(df.wicket_type=='stumped')|(df.wicket_type=='bowled')|(df.wicket_type=='lbw'))].groupby('season')['wicket_type'].count())
death_19runs.rename(columns={'runs_off_bat':'over_19_runs'},inplace=True)
death_19balls.rename(columns={'ball':'over_19_balls'},inplace=True)
death_19_stats=death_19runs.merge(death_19balls,on='season')
death_19_stats['SR']=100*death_19_stats['over_19_runs']/death_19_stats['over_19_balls']
death_19_stats = pd.merge(death_19_stats, death_19out, how='left', on='season')
death_19_stats


# In[ ]:


ax = plt.gca()
death_19_stats.plot(kind = 'bar',
        y = 'SR',
        color = 'green',ax = ax)
plt.show()


# **Over 19 :** He's very poor striking in this over throughout his career.

# In[ ]:


death_20runs=pd.DataFrame(df[(df.ball>19)&(df.ball<20)&(df.striker=='MS Dhoni')].groupby('season')['runs_off_bat'].sum())
death_20balls=pd.DataFrame(df[(df.ball>19)&(df.ball<20)&(df.striker=='MS Dhoni')].groupby('season')['ball'].count())
death_20out=pd.DataFrame(df[(df.ball>19)&(df.ball<20)&(df.striker=='MS Dhoni')&((df.wicket_type=='caught')|(df.wicket_type=='caught and bowled')|(df.wicket_type=='stumped')|(df.wicket_type=='bowled')|(df.wicket_type=='lbw'))].groupby('season')['wicket_type'].count())
death_20runs.rename(columns={'runs_off_bat':'over_20_runs'},inplace=True)
death_20balls.rename(columns={'ball':'over_20_balls'},inplace=True)
death_20_stats=death_20runs.merge(death_20balls,on='season')
death_20_stats['SR']=100*death_20_stats['over_20_runs']/death_20_stats['over_20_balls']
death_20_stats = pd.merge(death_20_stats, death_20out, how='left', on='season')
death_20_stats


# In[ ]:


from google.colab import drive
drive.mount('/content/drive')


# In[ ]:


ax = plt.gca()
death_20_stats.plot(kind = 'bar',
        y = 'SR',
        color = 'green',ax = ax)
plt.show()


# **Over 20 :** The above visualization shows how he got transformed as a final over specialist. His strikes almost at 250.

# **Conclusion:**
# 
# Dhoni is not the one who keeps striking all over the death overs, his balls per boundary is around 4 which is not a great stat to consider. Interestingly, he never touched 3(which is a best rate) in his career throughout. But he has the ability to play a finisher role even at this stage. We have seen how hard he is going after the ball in 20th over (SR almost 250) and still maintains it consistently over past 5 years. His age is not a factor. One thing I can conclude is that he can't play a finisher who can hit right from 16-20 overs but has the ability to finish the innings high.
