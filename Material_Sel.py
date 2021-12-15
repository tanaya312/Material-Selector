import sys
import pandas as pd
from tkinter import *

df=pd.read_csv("materials_csv_1.csv")
#df.reset_index(drop=True,inplace=True)
Mat=df["Materials"]
Mat_list=list(Mat)
#print(df)
DF=df
DF=DF.fillna("Unavailable")
print(DF)

def openInfo():

    def onGet():
        Tx=e1.get()
        tx1=Tx.lower()
        #e1.delete(0,'end')
        
        if tx1 not in Mat_list:
            info=Label(tk1,text="Material Unavailable",bg='Black',fg='Yellow',font='Helvetica 30',)
            info.grid(row=4,column=1)
            
        else:
            df1=df[df['Materials']==tx1]
            print(df1.T)
            
            info=Label(tk1,text=df1.T.head(6),bg='Purple',fg='Yellow',font='Helvetica 20',justify=LEFT)
            info.grid(row=4,column=1)
    def onHome():
        tk1.destroy()
        tk.deiconify()
    
    tk.withdraw()
    tk1 = Tk()
    tk1.geometry('800x600')
    tk1.title('Info')
    tk1.config(bg='Purple')

    b3=Button(tk1, text="Home",bg='SlateBlue1',font='Helvetica 15',command=onHome).grid(row=0,column=0,pady=10,padx=10)
    t2=Label(tk1,text="Give Material name for info",bg='Purple',fg='Yellow',font='Helvetica 30',).grid(row=1,column=1,padx=50)
    e1=Entry(tk1,bg='Purple',fg='Yellow',font='Helvetica 30')
    e1.grid(row=2,column=1)
    b3=Button(tk1, text="Get Info",bg='SlateBlue1',font='Calibary 20',command=onGet).grid(row=3,column=1,pady=10)

q=0
ans=[]   
def openSel():
    def Next():
        global q
        if(q==7):bt.config(text="Finish")
        if(q<=7):
            q+=1
            ans.append([var1.get(),var2.get(),var3.get(),var4.get()])
            if(q!=8):Q.config(text=Questions[q].capitalize())
            
        else:
            for i in range(len(ans)):
                if ans[i]==[1,0,0,0]: ans[i]='A' 
                elif ans[i]==[0,1,0,0]: ans[i]='B'
                elif ans[i]==[0,0,1,0]: ans[i]='C'
                else: ans[i]="None"

            def low(c):
                if c=='B': return 'C'
                elif c=='A': return 'B'
                elif c=='C': return None
                elif c==None: return None
            
            def CheckAttr1(list):
                global DF
                I=[]

                if list[0]!='D':
                    for i in range(len(DF)):
                        if(DF["Strength_Grade"][i]==low(list[0]) or DF["Strength_Grade"][i]==low(low(list[0]))):
                            I.append(i)
                    D=DF.drop(I,axis=0)
                    D.reset_index(drop=True,inplace=True)
                    I=[]
                print(D)

                if list[1]!='D':
                    for i in range(len(D)-1):
                        if(D["salt water"][i]==low(list[1]) or D["salt water"][i]==low(low(list[1]))):
                            I.append(i)
                    D=D.drop(I,axis=0)
                    D.reset_index(drop=True,inplace=True)
                    I=[]
                print(D)

                if list[2]!='D':
                    for i in range(len(D)-1):
                        if(D["fresh water"][i]==low(list[2]) or D["fresh water"][i]==low(low(list[2]))):
                            I.append(i)
                    D=D.drop(I,axis=0)
                    D.reset_index(drop=True,inplace=True)
                    I=[]
                print(D)

                if list[3]!='D':
                    for i in range(len(D)-1):
                        if(D["Flammability"][i]==low(list[3]) or D["Flammability"][i]==low(low(list[3]))):
                            I.append(i)
                    D=D.drop(I,axis=0)
                    D.reset_index(drop=True,inplace=True)
                    I=[]
                print(D)
        
                if list[4]!='D':
                    for i in range(len(D)-1):
                        if(D["MP_grade"][i]==low(list[4]) or D["MP_grade"][i]==low(low(list[4]))):
                            I.append(i)
                    D=D.drop(I,axis=0)
                    D.reset_index(drop=True,inplace=True)
                    I=[]
                print(D)

                if list[5]!='D':
                    for i in range(len(D)-1):
                        if(D["Fracture_Grade"][i]==low(list[5]) or D["Fracture_Grade"][i]==low(low(list[5]))):
                            I.append(i)
                    D=D.drop(I,axis=0)
                    D.reset_index(drop=True,inplace=True)
                    I=[]
                print(D)

                if list[6]!='D':
                    for i in range(len(D)-1):
                        if(D["sunlight"][i]==low(list[6]) or D["sunlight"][i]==low(low(list[6]))):
                            I.append(i)
                    D=D.drop(I,axis=0)
                    D.reset_index(drop=True,inplace=True)
                    I=[]
                print(D)

                if list[7]!='D':
                    for i in range(len(D)-1):
                        if(D["wear"][i]==low(list[7]) or D["wear"][i]==low(low(list[7]))):
                            I.append(i)
                    D=D.drop(I,axis=0)
                    D.reset_index(drop=True,inplace=True)
                    I=[]
                print(D.T)

                return D
                
            Final=CheckAttr1(ans)
            
            def Det():
                F1=Final.set_index('Materials')
                ANS.config(text=F1.T.tail(8).to_string(),font='Helvetica 12',justify=LEFT)
                bt.destroy()

            Q.config(text="Responce Recorded",font='Helvetica 50')
            mat=Label(Sel,text="Best Suitable materials : ",fg="Yellow",bg="Black",font='Helvetica 30').place(relx=0.1,rely=0.2)
            ANS=Label(Sel,text=Final["Materials"].to_string(),fg="Orange",bg="Black",font='Helvetica 20',justify=LEFT)
            ANS.place(relx=0.1,rely=0.3)
            ck1.destroy()
            ck2.destroy()
            ck3.destroy()
            ck4.destroy()
            bt.config(text="Details",command=Det)
            print(ans)
        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
    Questions=("How strenght material should provide?",
               "How material should be resistant to salt water?",
               "How material should be resistant to fresh water?",
               "How flammability material should provide?",
               "How should be the melting point of material?",
               "How fracture resistance material should have?",
               "How sunlight resistant the material should be?",
               "How wear resistance material should provide?")
    

    tk.withdraw()
    Sel=Toplevel()
    Sel.geometry('800x600')
    Sel.title("Material Selection")
    Sel.config(bg='Black')

    #Adding bck image
    canvas=Canvas(Sel,width=800,height=600)


    img=PhotoImage(file="back.png")
    #canvas.create_image(0,0,anchor=NW,image=img)
    bck=Label(Sel,image=img)
    bck.place(x=0,y=0,relwidth=1,relheight=1)


    
    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()

    def Start():
        Nav.destroy()
        btn.destroy()

    
    
    Q=Label(Sel,text=Questions[0].capitalize(),bg='Navy',fg='Yellow',font='Helvetica 25',)
    Q.place(relx=0.05,rely=0.02)
    ck1=Checkbutton(Sel,text="A. Excellent    ",bg='midnight blue',fg='Red',font='Helvetica 20',variable=var1)
    ck1.place(relx=0.05,rely=0.1)
    ck2=Checkbutton(Sel,text="B. Good         ",bg='midnight blue',fg='Red',font='Helvetica 20',variable=var2)
    ck2.place(relx=0.05,rely=0.18)
    ck3=Checkbutton(Sel,text="C. Poor           ",bg='midnight blue',fg='Red',font='Helvetica 20',variable=var3)
    ck3.place(relx=0.05,rely=0.26)
    ck4=Checkbutton(Sel,text="D. Unessential",bg='midnight blue',fg='Red',font='Helvetica 20',variable=var4)
    ck4.place(relx=0.05,rely=0.34)
    bt=Button(Sel,text="Next",bg='SlateBlue1',font='Helvetica 20',command=Next)
    bt.place(relx=0.8,rely=0.4)

    Nav=Label(Sel,text='''Welcome to Material Selector

>This is Material selector system based on user responces

>You will be asked few questions about the material you
will require for your application.

>If you feel any inadequacy in questions being asked,
you can tick "Unessential" option.

>Based on your responces(i.e. Excellent, Good, Poor)
given on questions, you will be provided the best suitable
material for your application''',bg='dodger blue',fg='light yellow',font='Helvetica 20',borderwidth=6,relief="ridge",justify=LEFT)
    Nav.place(relx=0.05,rely=0.02)
    btn=Button(Sel,text="Get Started",bg='royal blue',font='Helvetica 20',command=Start)
    btn.place(relx=0.7,rely=0.7)


    #Overriding[x]/reopening Home when we quit Sel tab
    def end():
        Sel.destroy()
        tk.deiconify()
    Sel.protocol('WM_DELETE_WINDOW',end)
    
    Sel.mainloop()
  
def Describe():
    def X1():
        des.destroy()
        X.destroy()
    des=Label(tk,text='''        >>Melting point: The stronger the forces of attraction between the particles,
                          the more energy is needed to overcome them. The more energy is needed, the higher
                          the melting point. The melting temperature of a crystalline solid is thus an
                          indicator for the stability of its lattice.

        >>Density : The density of a substance is the relationship between the mass of the
                          substance and how much space it takes up (volume). Density indicates how much of a
                          substance occupies a specific volume at a defined temperature and pressure.

        >>Young’s modulus : The Young's Modulus of a material is a fundamental property of
                          every material that cannot be changed. It is dependent upon temperature and pressure
                          however. The Young's Modulus (or Elastic Modulus) is in essence the stiffness of a material.
                          In other words, it is how easily it is bended or stretched.

        >>Yield Stress: Yield occurs when the maximum principal strain reaches the strain
                          corresponding to the yield point during a simple tensile test

        >>Tensile strength: Tensile strength is indicative of the strength derived from factors
                          such as fibre strength, fibre length, and bonding. It may be used to deduce information
                          about these factors, especially when used as a tensile strength index.

        >>Fracture Toughness: Toughness is ability of material to resist fracture.

        >>Flammability: Flammability is determined by the flash point of a material.
                          Flash point is the minimum temperature at which a liquid forms a vapor above its surface in
                          sufficient concentration that it can be ignited. Flammable liquids have a flash point of
                          less than 100°F. Liquids with lower flash points ignite easier.''',bg='dodger blue',fg='light yellow',font='Helvetica 12',borderwidth=6,relief="ridge",justify=LEFT)
    des.place(relx=0.02,rely=0.02)
    X=Button(tk,text='X',bg='Red',font='Calibary 20',command=X1)
    X.place(relx=0.9,rely=0.05)


tk=Tk()
tk.geometry('800x600')
tk.title("Material Selection")
tk.config(bg='Purple')

#Adding bck image
canvas=Canvas(tk,width=800,height=600)


img=PhotoImage(file="back.png")
#canvas.create_image(0,0,anchor=NW,image=img)
bck=Label(tk,image=img)
bck.place(x=0,y=0,relwidth=1,relheight=1)


t1=Label(tk,text="     Material Selection     ",bg='Black',fg='Yellow',font='Helvetica 40',).grid(row=2,column=2,padx=120,pady=100)
b1=Button(tk, text="Check for Suitable Material",bg='SlateBlue1',font='Calibary 20',command=openSel).grid(row=3,column=2,pady=30)
b2=Button(tk, text="Check information about Material",bg='SlateBlue1',font='Calibary 20',command=openInfo).grid(row=5,column=2,pady=30)
In=Button(tk, text="Info",bg='SlateBlue1',font='Calibary 20',command=Describe).place(relx=0.02,rely=0.02)
#t2=Label(tk,text=df)
#t2=Label(tk,text=df,bg='Purple',font='Calibary 30',).grid(row=2,column=1)
#canvas.pack()

#making background of app transperent##tk.wm_attributes("-transparentcolor",'gray')
tk.mainloop()



