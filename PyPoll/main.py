
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


file = "Resources/election_data.csv"


# In[90]:


df = pd.read_csv(file)
df.head()


# In[66]:


#The total number of votes cast
total_votes_cast = df["Voter ID"].count()
total_votes_cast


# In[67]:


#A complete list of candidates who received votes
df["Candidate"].value_counts()


# In[101]:


#The percentage of votes each candidate won
pct = round((df['Candidate'].value_counts()/total_votes_cast)*100, 2)
pct


# In[62]:


#The total number of votes each each candidate won
candidates = df["Candidate"].value_counts()
candidates


# In[92]:


#The winner of the election
#winner = max(candidates)
winner = candidates.idxmax()
winner


# In[108]:


print("Election Results")
print("---------------------------")
print("Total Votes: " + str(total_votes_cast))
print("---------------------------")
print("Khan: " + str(pct[0]) + "% " + " (" + str(candidates[0]) + ")")
print("Correy: " + str(pct[1]) + "% " + " (" + str(candidates[1]) + ")")
print("Li: " +  str(pct[2]) + "% " + " (" + str(candidates[2]) + ")")
print("O'Tooley: " + str(pct[3]) + "% " + " (" + str(candidates[3]) + ")")
print("---------------------------")
print("Winner: " + winner)
print("---------------------------")


# In[112]:


with open("output_file.txt", "w") as datafile:
    
    datafile.write("Election Results\n")
    datafile.write("---------------------------\n")
    datafile.write("Total Votes: " + str(total_votes_cast) + "\n")
    datafile.write("---------------------------\n")
    datafile.write("Khan: " + str(pct[0]) + "% " + " (" + str(candidates[0]) + ")\n")
    datafile.write("Correy: " + str(pct[1]) + "% " + " (" + str(candidates[1]) + ")\n")
    datafile.write("Li: " +  str(pct[2]) + "% " + " (" + str(candidates[2]) + ")\n")
    datafile.write("O'Tooley: " + str(pct[3]) + "% " + " (" + str(candidates[3]) + ")\n")
    datafile.write("---------------------------\n")
    datafile.write("Winner: " + winner + "\n")
    datafile.write("---------------------------\n")

