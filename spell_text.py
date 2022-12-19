import plac
import re

Promptlist=[]
Prompt=[]
Weights=[]
x=0

def main():
    global x
    global Prompt
    global Weights
    power = 0
    print("Enter the prompt and weight Format:prompt,weight example:1girl,2.0\nEnter -i or info get more information\nYou can enter continuously or with a single input\nEnter 0 to leave the loop and display the result.\n")
    while (power ==0):
        request = input()
        if (request=="1"):
            if (x!=0):
                for i in range(len(Prompt)):
                    print("("+Prompt[i]+":"+Weights[i]+"),",end = '')
            power = 1
        else:
            process(request);


def process(request):
    if (request.lower() == "info")|(request.lower() =="-i"):
        print("The program will automatically delete the input {}() and newline\nfollowing is an example\n{masterpiece},2.0 -->(masterpiece:2.0)\nmasterpiece,1.5,best quality,1.3,Highest image quality,1.2 -->(masterpiece:1.5),(best quality:1.3),(Highest image quality:1.2),\nI'm Cloveriow, I want to make a sorting method that automatically sorts Tags,\nbut the operation screen of Python is not ideal, and I will develop in C# in the future.")
    else:
        global x
        global Prompt
        global Weights
        request= request.strip(',');
        request = re.sub('[{}()\n]','',request)
        Promptlist=re.split(r'[,]',request)
        if (len(Promptlist)%2!=0):
            print("Formatting error,It is detected that there are only singular numbers, and the correct format should be double numbers.")
            return
        elif len(Promptlist) >2:
            for i in range(0,len(Promptlist),2):
                Prompt.append(Promptlist[i+0])
                Weights.append(Promptlist[i+1])
            for i in range(len(Prompt)):
                print("("+Prompt[i]+":"+Weights[i]+"),",end = '')
            #print("("+Prompt[x]+":"+Weights[x]+"),",end = '')
                x+=1
        else: 
            Prompt.append(Promptlist[0])
            Weights.append(Promptlist[1])
            #print("("+Prompt[x]+":"+Weights[x]+"),")
            for i in range(len(Prompt)):
                print("("+Prompt[i]+":"+Weights[i]+"),",end = '')
            x+=1
        




if __name__ == '__main__':
    plac.call(main)