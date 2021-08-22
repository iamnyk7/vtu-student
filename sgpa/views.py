from django.shortcuts import render

subject_cse3={'sub1':'M3','sub2':'DS','sub3':'ADE','sub4':'CO','sub5':'SE','sub6':'DMS','sub7':'ADELAB','sub8':'DSLAB','sub9':'CIP/KAN'}
subject_cse4={'subi1':'M4','subi2':'DAA','subi3':'OS','subi4':'ME','subi5':'OOC','subi6':'DC','subi7':'DALAB','subi8':'MELAB','subi9':'CIP/KAN'}

subject_cse5={'sub1':'ME','sub2':'CNS','sub3':'DBMS','sub4':'ATC','sub5':'PY','sub6':'UNIX','sub7':'CNSLAB','sub8':'DBLAB','sub9':'EVS'}
subject_cse6={'subi1':'SSCD','subi2':'CGV','subi3':'WEB','subi4':'ELECTIVE 1','subi5':'ELETIVE 2','subi6':'SSLAB','subi7':'CGLAB','subi8':'MADLAB'}

subject_ise6={'subi1':'FS','subi2':'ST','subi3':'WEB','subi4':'ELECTIVE 1','subi5':'ELECTIVE 2','subi6':'LAB1','subi7':'LAB2','subi8':'LAB3'}

subject_ece3={'sub1':'M3','sub2':'NT','sub3':'ED','sub4':'DS','sub5':'CO','sub6':'PE&I','sub7':'EDLAB','sub8':'DSLAB','sub9':'CIP/KAN'}
subject_ece4={'subi1':'M4','subi2':'AC','subi3':'CS','subi4':'ES&ALGEBRA','subi5':'S&S','subi6':'MC','subi7':'MCLAB','subi8':'ACLAB','subi9':'CIP/KAN'}

subject_ece5={'sub1':'ME','sub2':'DSP','sub3':'PCS','sub4':'IT','sub5':'EW','sub6':'VHDL','sub7':'DSPLAB','sub8':'DHLLAB','sub9':'EVS'}
subject_ece6={'subi1':'DC','subi2':'ES','subi3':'M&A','subi4':'ELECTIVE 1','subi5':'ELECTIVE 2','subi6':'ESLAB','subi7':'COMLAB','subi8':'MINIPROJECT'}

subject_me3={'sub1':'M3','sub2':'MOM','sub3':'THERMODYNAMICS','sub4':'MS','sub5':'18ME35A/B','sub6':'18ME36A/B','sub7':'18MEL37A/B','sub8':'18MEL38A/B','sub9':'CIP/KAN'}
subject_me4={'sub1':'M4','sub2':'APPLIED THERMODYNAMICS','sub3':'FM','sub4':'KM','sub5':'18ME45A/B','sub6':'18ME46A/B','sub7':'18MEL47A/B','sub8':'18MEL48A/B','sub9':'CIP/KAN'}

subject_me5={'sub1':'ME','sub2':'DOM','sub3':'DM','sub4':'TM','sub5':'FPE','sub6':'OM','sub7':'FMLAB','sub8':'ECLAB','sub9':'EVS'}
subject_me6={'subi1':'FEM','subi2':'DOM2','subi3':'HT','subi4':'ELECTIVE 1','subi5':'ELECTIVE 2','subi6':'CAEDLAB','subi7':'HT LAB','subi8':'MINIPROJECT'}

subject_eee5={'sub1':'ME','sub2':'MC','sub3':'PE','sub4':'S&S','sub5':'EMD','sub6':'HV','sub7':'MCLAB','sub8':'PELAB','sub9':'EVS'}
subject_eee6={'subi1':'CS','subi2':'PS-1','subi3':'DSP','subi4':'ELECTIVE 1','subi5':'ELECTIVE 2','subi6':'CSLAB','subi7':'DSPLAB','subi8':'MINIPROJECT'}

# Create your views here.
def index(request):
    return render(request,'sgpa/index.html')

def direct(request,slug):
    if slug=="cses":
        context={'name':'CSE6','subject':subject_cse5,'subjecti':subject_cse6}
        return render(request,'sgpa/home.html',context)
    elif slug=="csef":
        context={'name':'CSE4','subject':subject_cse3,'subjecti':subject_cse4}
        return render(request,'sgpa/home.html',context)
    elif slug=="isef":
        context={'name':'ISE4','subject':subject_cse3,'subjecti':subject_cse4}
        return render(request,'sgpa/home.html',context)
    elif slug=="ises":
        context={'name':'ISE6','subject':subject_cse5,'subjecti':subject_ise6}
        return render(request,'sgpa/home.html',context)
    elif slug=="ecef":
        context={'name':'ECE4','subject':subject_ece3,'subjecti':subject_ece4}
        return render(request,'sgpa/home.html',context)
    elif slug=="eces":
        context={'name':'ECE6','subject':subject_ece5,'subjecti':subject_ece6}
        return render(request,'sgpa/home.html',context)
    elif slug=="mes":
        context={'name':'ECE6','subject':subject_me5,'subjecti':subject_me6}
        return render(request,'sgpa/home.html',context)
    elif slug=="mef":
        context={'name':'ME4','subject':subject_me3,'subjecti':subject_me4}
        return render(request,'sgpa/home.html',context)
    elif slug=="eees":
        context={'name':'EEE%','subject':subject_me3,'subjecti':subject_me4}
        return render(request,'sgpa/home.html',context)
    else:
        return render(request,'sgpa/home.html')

def calc(request):
    if request.method == "POST":
        b=len(request.POST)

        if b==19:
            # second year
            avg=0
            ixt=[]
            for i in range(1,9):
                avg+=(int(request.POST.get('sub'+str(i))))*0.83

            last=int(request.POST.get('sub9'))
            if last >60:
                # kannada
                avg+=last*0.5
            else:
                avg+=last*0.83
        
            avg=round(avg/9)
            
            for i in range(1,9):
                ixt.append(int(request.POST.get('subi'+str(i)))*1.25+avg)

            nine=int(request.POST.get('subi9'))
            
            if nine>40:
                # kannada
                ixt.append(nine*0.5+avg)
            else:
                ixt.append(nine*1.25+avg)

            print(ixt)
            points=grade(round(ixt[0]),3)+grade(round(ixt[1]),4)+grade(round(ixt[2]),3)+grade(round(ixt[3]),3)+grade(round(ixt[4]),3)+grade(round(ixt[5]),3)+grade(round(ixt[6]),2)+grade(round(ixt[7]),2)+grade(round(ixt[8]),1)

            sgpa=round(points/24,2)
            per=(sgpa-0.75)*10
            context={'sgpa':sgpa,'per':per}
            return render(request,'sgpa/home.html',context)

        else:
            avg=0
            ixt=[]
            for i in range(1,10):
                mark_con=round(((int(request.POST.get('sub'+str(i))))*0.83),2)
                # print(mark_con)
                avg+=mark_con
            
            # print(avg)
            avg=round(avg,2)
            # print(avg)
            avg=round(avg/9,2)

            # print(avg)
            
            
            for i in range(1,9):
                iam=((int(request.POST.get('subi'+str(i))))*1.25)
                ixt.append((iam+avg))
            
            print(ixt)
           
            points=grade((round(ixt[0])),4)+grade((round(ixt[1])),4)+grade((round(ixt[2])),4)+grade((round(ixt[3])),3)+grade((round(ixt[4])),3)+grade((round(ixt[5])),2)+grade((round(ixt[6])),2)+grade((round(ixt[7])),2)
            print(points)
            sgpa=round(points/24,2)


            per=round(((sgpa-0.75)*10),2)
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