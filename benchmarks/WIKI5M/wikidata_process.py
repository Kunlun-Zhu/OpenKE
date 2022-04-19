#!/usr/bin/env python
# coding: utf-8




#step1. Load the file
triple = open("train.txt", "r")
valid = open("valid.txt", "r")
test = open("test.txt", "r")


tripleline = len(triple.readlines())
validline = len(valid.readlines())
testline = len(test.readlines())

triple = open("train.txt", "r")
valid = open("valid.txt", "r")
test = open("test.txt", "r")


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

f_e = open("entity2id.txt", "w")
f_e.write("%d\n"%len(ent_dict))
for key, value in ent_dict.items():
    f_e.write("%s\t%d\n"%(key, value))
f_e.close()

f_r = open("relation2id.txt", "w")
f_r.write("%d\n"%len(rel_dict))
for key, value in rel_dict.items():
    f_r.write("%s\t%d\n"%(key, value))
f_r.close()

