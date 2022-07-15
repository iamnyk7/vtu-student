from django.shortcuts import render

subject_cse3={'sub1':'MATH','sub2':'PHY/CHEM','sub3':'ELE/CPS','sub4':'CIVIL/ELN','sub5':'EVN/EME','sub6':'LAB1','sub7':'LAB2','sub8':'EGH','sub9':'IDT/SFH'}

# Create your views here.
def index(request):
    return render(request,'sgpa/index.html')

def direct(request,slug):
    if slug=="cses":
        context={'name':'CSE6','subject':subject_cse3}
        return render(request,'sgpa/home.html',context)
    else:
        return render(request,'sgpa/index.html')

def calc(request):
    if request.method == "POST":
        ixt=[]
        b=len(request.POST)

        
        for i in range(1,10):
            ixt.append(int(request.POST.get('subi'+str(i))))


        print(ixt)
        points=grade(round(ixt[1]),3)+grade(round(ixt[2]),3)+grade(round(ixt[3]),3)+grade(round(ixt[4]),3)+grade(round(ixt[5]),3)+grade(round(ixt[6]),1)+grade(round(ixt[7]),1)+grade(round(ixt[8]),2)+grade(round(ixt[9]),1)
        print(points)
        sgpa=round(points/20,2)
        per=(sgpa-0.75)*10
        context={'sgpa':sgpa,'per':per}
        return render(request,'sgpa/home.html',context)

        

def grade(marks,sub):
    if marks>=90:
        points=sub*10
        return points
    
    elif marks>=80:
        points=sub*9
        return points
       
    elif marks>=70:
        points=sub*8
        return points
      
    elif marks>=60:
        points=sub*7
        return points
    
    elif marks>=50:
        points=sub*6
        return points
    
    else:
        return sub*5

def cgpa(request):
    return render(request,'sgpa/cgpa.html')

def cgpacalc(request):
    c=[]
    total={'s0':20,'s1':20,'s2':24,'s3':24,'s4':25,'s5':24,'s6':20,'s7':18}
    points=0
    tot_cgpa=0
    for i in range(1,9):
        c.append(float(request.POST.get('sem'+str(i))))
    print(c)
    
    for i in range(0,8):
        if c[i]==0.0:
            total['s'+str(i)]=0
        else:
            points+=c[i]*total['s'+str(i)]
    
    for i in range(0,8):
        tot_cgpa+=total['s'+str(i)]
    
    res=round(points/tot_cgpa,2)
    per=(res-0.75)*10
    context={'res':res,'per':per}

    return render(request,'sgpa/cgpa.html',context)
