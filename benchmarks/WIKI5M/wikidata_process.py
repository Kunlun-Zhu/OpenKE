#!/usr/bin/env python
# coding: utf-8

# In[22]:


#step1. Load the file
triple = open("wikidata5m_transductive_train.txt", "r")
valid = open("wikidata5m_transductive_valid.txt", "r")
test = open("wikidata5m_transductive_test.txt", "r")


# In[21]:


tripleline = len(triple.readlines())
validline = len(valid.readlines())
testline = len(test.readlines())

triple = open("wikidata5m_transductive_train.txt", "r")
valid = open("wikidata5m_transductive_valid.txt", "r")
test = open("wikidata5m_transductive_test.txt", "r")


# In[23]:


#Load triplet
ent_num = 0
rel_num = 0
ent_dict = {}
rel_dict = {}

f_t = open("train2id.txt", "w")
write_line = ""

###wikifile triplet form is 'h,r,t', while Openke form should be'h,t,r'
f_t.write("%d\n"%tripleline)
for line in triple:
    h, r, t = line.strip('\t').split()
    if h in ent_dict.keys():
        write_line += ("%d "%ent_dict[h])
    else:
        ent_dict[h] = ent_num
        write_line += ("%d "%ent_num)
        ent_num += 1
    if t in ent_dict.keys():
        write_line += ("%d "%ent_dict[t])
    else:
        ent_dict[h] = ent_num
        write_line += ("%d "%ent_num)
        ent_num += 1
    if r in rel_dict.keys():
        write_line += ("%d\n"%rel_dict[r])
        rel_num += 1
    else:
        rel_dict[r] = rel_num
        write_line += ("%d\n"%rel_num)
        rel_num += 1
        
    f_t.write(write_line)
    write_line = ""

f_t.close()
triple.close()

f_v = open("valid2id.txt", "w")
f_v.write("%d\n"%validline)
for line in valid:
    h, r, t = line.strip('\t').split()
    if h in ent_dict.keys():
        write_line += ("%d "%ent_dict[h])
    else:
        ent_dict[h] = ent_num
        write_line += ("%d "%ent_num)
        ent_num += 1
    if t in ent_dict.keys():
        write_line += ("%d "%ent_dict[t])
    else:
        ent_dict[h] = ent_num
        write_line += ("%d "%ent_num)
        ent_num += 1
    if r in rel_dict.keys():
        write_line += ("%d\n"%rel_dict[r])
        rel_num += 1
    else:
        rel_dict[r] = rel_num
        write_line += ("%d\n"%rel_num)
        rel_num += 1
        
    f_v.write(write_line)
    write_line = ""
f_v.close()
valid.close()

f_t = open("test2id.txt", "w")
f_t.write("%d\n"%testline)
for line in test:
    h, r, t = line.strip('\t').split()
    if h in ent_dict.keys():
        write_line += ("%d "%ent_dict[h])
    else:
        ent_dict[h] = ent_num
        write_line += ("%d "%ent_num)
        ent_num += 1
    if t in ent_dict.keys():
        write_line += ("%d "%ent_dict[t])
    else:
        ent_dict[h] = ent_num
        write_line += ("%d "%ent_num)
        ent_num += 1
    if r in rel_dict.keys():
        write_line += ("%d\n"%rel_dict[r])
        rel_num += 1
    else:
        rel_dict[r] = rel_num
        write_line += ("%d\n"%rel_num)
        rel_num += 1
        
    f_t.write(write_line)
    write_line = ""
f_t.close()
test.close()


# In[ ]:





# In[ ]:





# In[ ]:




