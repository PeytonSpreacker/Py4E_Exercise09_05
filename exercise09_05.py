#Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

# Use the file name mbox-short.txt as the file name
fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('File does not exist:', fname)
    quit()
#create dictionary and lists
domain = dict()
lst = list()
newlst = list()
#go through lines
for line in fh:
    line.strip()
    words = line.split()
    if not line.startswith('From ') :
        continue
    if not len(words) > 3 :
        continue
    else:
        exwords = words[1]
        lst.append(exwords)
for x in lst:
    loc = x.find('@')
    partneeded = x[loc+1:]
    newlst.append(partneeded)
for mails in newlst:
    domain[mails] = domain.get(mails, 0) + 1
print(domain)