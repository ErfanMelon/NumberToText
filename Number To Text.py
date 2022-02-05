
Number_text = ['', 'one', 'two', 'three', 'four',
           'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteenth', 'fourteen',
                      'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
list10 = ['twenty', 'thirty', 'forty', 'fifty',
           'sixty', 'seventy', 'eighty', 'ninety']
hugeamount = ['hundred', 'thousand', 'million', 'billion']

i = int(input("Please enter a number: "))



def numtotext100(Number_text, list10, hugeamount, i):
    out = None

    number_list = list(str(i))
    size = len(number_list)  # count members

    if(size == 1):
        if i == 0:
            print('Zero')
        else:
            out = Number_text[i]

    elif(size == 2):
        ab = int(number_list[-2]+number_list[-1])
        if ab >= 10 and ab < 20:
            out = Number_text[ab]
        else:
            out = list10[int(number_list[-2])-2]+" "+Number_text[int(number_list[-1])]

    elif(size == 3):
        out = Number_text[int(number_list[-3])]+" "+hugeamount[0]+" "
        bc = int(number_list[-2]+number_list[-1])
        if bc < 20:
            out += Number_text[bc]
        else:
            out += list10[int(number_list[-2])-2]+" "+Number_text[int(number_list[-1])]
    if out==None:
        out=""
    return out


string_num=str(i)
list_num=[]
s=''
reversednum=[number for number in string_num]
reversednum.reverse()

string_num=''
for w in reversednum:
    string_num+=w

for n in string_num:
    if len(s)<3:
        s+=n
    else:
        list_num.insert(0,s)
        s=''
        s+=n

list_num.insert(0,s)
newlist=[]
for item in list_num:
    k=[d for d in item]
    k.reverse()
    text=''
    for items in k:
        text+=items
    newlist.append(text)
list_num=newlist       

list_num=[int(n) for n in list_num]

if len(list_num)==1:
    out=numtotext100(Number_text, list10, hugeamount, list_num[0])
elif len(list_num)==2:
    out=numtotext100(Number_text, list10, hugeamount, list_num[0])+" "+hugeamount[1]+" "+numtotext100(Number_text, list10, hugeamount, list_num[1])
elif len(list_num)==3:
    out=numtotext100(Number_text, list10, hugeamount, list_num[0])+" "+hugeamount[2]+" "+numtotext100(Number_text, list10, hugeamount, list_num[1])+" "+hugeamount[1]+" "+numtotext100(Number_text, list10, hugeamount, list_num[2])
else:
    out=None
print(out)

print('Press any key to continue ...')