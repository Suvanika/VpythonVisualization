from vpython import *
#GlowScript 2.6 VPython

c = curve(vector(-0.2,-1,0), vector(0.2,-1,0))
c = curve(vector(-0.2,-1,0), vector(-0.2,0.05,0))
c = curve(vector(0.2,-1,0), vector(0.2,0.05,0))
pos = vector(0.0055, -0.88, 0)
a =vector(-0.2,0.05,0)
b = vector(0.2,0.05,0)
line1 = vector(-0.2,-0.7,0)
line2= vector(0.2,-0.7,0)
i=0
sphere1=1
label1=1
pointer1=1


def showSphere(evt):
    global line1
    global line2
    global i
    global pos
    loc = evt.pos
    print("Pushing in top element..")
    
    global label1
    global pointer1
    if i>=1:
         i=i+1
         pointer = arrow(pos=pos, axis=vector(0.6,0,0), shaftwidth=0.01, color=color.black, opacity=1)
         label1=label( pos=pos+vector(0.7,0,0), text='Top', color=color.black, opacity=1,box=False )
         label2=label( pos=pos+vector(1,0,0), text=i, color=color.black, opacity=1,box=False )
         global sphere1
         pos= pos + vector(0,0.25,0)
         sphere1=sphere(pos=pos ,radius=0.06, color=color.cyan)
         pointer = arrow(pos=pos, axis=vector(0.6,0,0), shaftwidth=0.01)
         label1=label( pos=pos+vector(0.7,0,0), text='Top',box=False )
         label2=label( pos=pos+vector(1,0,0), text=i, color=color.white, opacity=1,box=False )
         sphere1.visible=True
         line1=line1 +vector(0,0.25,0)
         line2=line2+vector(0,0.25,0)
         c = curve(line1, line2)
         
         if i%4==0:
             global a
             global b
             c=a
             d=b
             a=a+vector(0,1,0)
             b=b+vector(0,1,0)
             c = curve(c,a)
             c = curve(d,b )
             
             
             
    else if i==0 | i==1:
        j=0
        global sphere1
        i=1
        sphere1=sphere(pos=pos ,radius=0.06, color=color.cyan)
        pointer = arrow(pos=pos, axis=vector(0.6,0,0), shaftwidth=0.01,)
        label1=label( pos=pos+vector(0.7,0,0), text='Top',box=False)
        label2=label( pos=pos+vector(1,0,0), text=i, color=color.white, opacity=1,box=False )
        sphere1.visible=True
        c = curve(vector(-0.2,-0.7,0), vector(0.2,-0.7,0))
       
        

        
def hideSphere(evt):
    print("Popping top element..")
    global i
    global pos
    
    global sphere1
    if i>1:
         label2=label( pos=pos+vector(1,0,0), text=i, color=color.black, opacity=1,box=False )
         sphere1=sphere(pos=pos ,radius=0.06, color=color.black,opacity=1)
         pointer = arrow(pos=pos, axis=vector(0.6,0,0), shaftwidth=0.01, color=color.black, opacity=1)
         label1=label( pos=pos+vector(0.7,0,0), text='Top', color=color.black, opacity=1,box=False )
         del sphere1
          
         pos= pos - vector(0,0.25,0)
       
         i=i-1
         pointer = arrow(pos=pos, axis=vector(0.6,0,0), shaftwidth=0.01)
         label1=label( pos=pos+vector(0.7,0,0), text='Top',box=False )
         label2=label( pos=pos+vector(1,0,0), text=i, color=color.white, opacity=1,box=False )
        
    else if i==1: 
        
         sphere1=sphere(pos=pos ,radius=0.06, color=color.black, opacity=1)
         i=i-1
         pointer = arrow(pos=pos, axis=vector(0.6,0,0), shaftwidth=0.01, color=color.black, opacity=1)
         label1=label( pos=pos+vector(0.7,0,0), text='Top', color=color.black, opacity=1,box=False )
         label2=label( pos=pos+vector(1,0,0), text=i, color=color.white, opacity=1,box=False )
         Print("Stack is now empty..")
             
    else :
        print("Sorry, Stack empty") 
        pointer = arrow(pos=pos, axis=vector(0.6,0,0), shaftwidth=0.01, color=color.black, opacity=1)
        label1=label( pos=pos+vector(0.7,0,0), text='Top', color=color.black, opacity=1,box=False )
        label2=label( pos=pos+vector(1,0,0), text=i, color=color.white, opacity=1,box=False )

def reference():
    global pos
    global sphere1
    sphere1=sphere(pos=pos ,radius=0.06, color=color.cyan)
    sphere1.visible=False
    
    
button( bind=showSphere, text='Push' )
scene.append_to_caption('\n\n')

button( bind=hideSphere, text='Pop' )
scene.append_to_caption('\n\n')
