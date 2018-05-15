from vpython import *
#GlowScript 2.6 VPython


value=0
j=0
k=0

print("Creating hashtable..")
class Node:

   def __init__(self,data,hashv,sizm,nextNode=None):
       self.data = data
       self.nextNode = nextNode
       self.hash=hashv
       newnode=[]
       
       if(sizm==0):
           pointer = arrow(pos=vector(3,hashv+0.5,0), axis=vector(3,0,0), shaftwidth=0.2,)
           newnode[sizm]=curve(vector(6+(4*sizm),hashv,0),vector(10+(4*sizm),hashv,0))
           newnode[sizm].append(vector(10+(4*sizm),hashv,0),vector(10+(4*sizm),hashv+0.7,0))
           newnode[sizm].append(vector(6+(4*sizm),hashv+0.7,0))
           newnode[sizm].append(vector(6+(4*sizm),hashv,0),)
           newnode[sizm].append(vector(8+(4*sizm),hashv,0),vector(8+(4*sizm),0.7+hashv,0))
           node1=label(pos=vector(7+(4*sizm),0.35+hashv,0),text=data,box=False,height=10,opacity=0)
           pointer = arrow(pos=vector(10+(sizm*4),hashv+0.35,0), axis=vector(1,0,0), shaftwidth=0.2,)
        
       else:
           
           print("inside create new node: printing size: ",sizm)
           newnode[sizm]=curve(vector(6+(4*sizm)+sizm,hashv,0),vector(10+(4*sizm)+sizm,hashv,0))
           newnode[sizm].append(vector(10+(4*sizm)+sizm,hashv,0),vector(10+(4*sizm)+sizm,hashv+0.7,0))
           newnode[sizm].append(vector(6+(4*sizm)+sizm,hashv+0.7,0))
           newnode[sizm].append(vector(6+(4*sizm)+sizm,hashv,0),)
           newnode[sizm].append(vector(8+(4*sizm)+sizm,hashv,0),vector(8+(4*sizm)+sizm,0.7+hashv,0))
           node1=label(pos=vector(7+(4*sizm)+sizm,0.35+hashv,0),text=data,box=False,height=10,opacity=0)
           pointer = arrow(pos=vector(10+(sizm*4)+sizm,hashv+0.35,0), axis=vector(1,0,0), shaftwidth=0.2,)
           
           
           
           
       
   def getData(self):
       return self.data

   def setData(self,val):
       self.data = val

   def getNextNode(self):
       return self.nextNode

   def setNextNode(self,val):
       self.nextNode = val

class LinkedList:

   def __init__(self,head = None):
       self.head = None
       self.size = 0
       cur = None

   def getSize(self):
       return self.size
       
       
    
            

   def addNode(self,data,hashv,sizm):
       print("adding node..:")
       
       temp = Node(data,hashv,sizm,self.head)
       temp.setNextNode(self.head)
       self.head = temp
       self.size+=1
       return True
           
           
     
       
       
     
       
   def printNode(self,hashv,v):
       a=[]
       curr = self.head
       i=0
       sizm=self.size
       
       print("Value of curr:",curr.getData())
       a.append(curr.getData())
       sizm-=1
       
       print("Value of bucket :",hashv ,"and size is:",self.size)
       
           
       
           
       while curr != None:
               
           curr = curr.getNextNode()
           
           a.append(curr.getData())
           sizm-=1
           i+=1
           print("Data:",curr.getData())
           print("List:")
           print(a)
           
       self.head=None
       self.size=0
       for j in a:
           self.addNode(self,j,hashv,self.size)
           
               
               
             
               
    
     
           
       
           
      
               
               
                
       
           
           
      
           
          
  
   def search(self, k, hashv,sizm):
        print("searching..")
        
        p = self.head
        if p is not None:
            
            sizm=sizm-1
            if p.getData() == k:
                
                newnode=curve(vector(6+(4*sizm)+sizm,hashv,0),vector(10+(4*sizm)+sizm,hashv,0))
                newnode.append(vector(10+(4*sizm)+sizm,hashv,0),vector(10+(4*sizm)+sizm,hashv+0.7,0))
                newnode.append(vector(6+(4*sizm)+sizm,hashv+0.7,0))
                newnode.append(vector(6+(4*sizm)+sizm,hashv,0),)
                newnode.append(vector(8+(4*sizm)+sizm,hashv,0),vector(8+(4*sizm)+sizm,0.7+hashv,0))
                newnode.color=color.red
                  
                         
                 
           
                 
                 
                print("Item found at position:",sizm)
                return True
            
            else:
                
                while p.getNextNode() is not None:
                     p = p.getNextNode()
                     sizm=sizm-1
                    
                     if p.getData() == k:
                         if(sizm==0):
                             pointer = arrow(pos=vector(3,hashv+0.5,0), axis=vector(3,0,0), shaftwidth=0.2,)
                             newnode=curve(vector(6+(4*sizm),hashv,0),vector(10+(4*sizm),hashv,0))
                             newnode.append(vector(10+(4*sizm),hashv,0),vector(10+(4*sizm),hashv+0.7,0))
                             newnode.append(vector(6+(4*sizm),hashv+0.7,0))
                             newnode.append(vector(6+(4*sizm),hashv,0),)
                             newnode.append(vector(8+(4*sizm),hashv,0),vector(8+(4*sizm),0.7+hashv,0))
                             newnode.color=color.red
                             
                             
                         else:
                             newnode=curve(vector(6+(4*sizm)+sizm,hashv,0),vector(10+(4*sizm)+sizm,hashv,0))
                             newnode.append(vector(10+(4*sizm)+sizm,hashv,0),vector(10+(4*sizm)+sizm,hashv+0.7,0))
                             newnode.append(vector(6+(4*sizm)+sizm,hashv+0.7,0))
                             newnode.append(vector(6+(4*sizm)+sizm,hashv,0),)
                             newnode.append(vector(8+(4*sizm)+sizm,hashv,0),vector(8+(4*sizm)+sizm,0.7+hashv,0))
                             newnode.color=color.red
                             
                         print("Item found at position:",sizm)
                         return True
                     
                sizm=sizm-1
                if p.getData()==k and sizm==0:
                        
                         
                         newnode=curve(vector(6+(4*sizm),hashv,0),vector(10+(4*sizm),hashv,0))
                         newnode.append(vector(10+(4*sizm),hashv,0),vector(10+(4*sizm),hashv+0.7,0))
                         newnode.append(vector(6+(4*sizm),hashv+0.7,0))
                         newnode.append(vector(6+(4*sizm),hashv,0),)
                         newnode.append(vector(8+(4*sizm),hashv,0),vector(8+(4*sizm),0.7+hashv,0))
                         newnode.color=color.red
                        
                         
                else:
                         return False
               
   def remove(self, k, hashv,sizm):
        print("searching..")
        
        p = self.head
        if p is not None:
            
            sizm=sizm-1
            if p.getData() == k:
                 newbox=box(pos=vector(6,0,0),height=0.7,length=6,width=0,color=color.red)
                 
                 
                 print("Itemzsd found at position:",sizm)
                 return True
            
            else:
                
                while p.getNextNode() is not None:
                     p = p.getNextNode()
                     sizm=sizm-1
                    
                     if p.getData() == k:
                         if(sizm==0):
                             newbox=box(pos=vector(4+(4*sizm),hashv,0),height=0.7,length=6,width=0,color=color.black)
                             
                         else:
                             newbox=box(pos=vector(4+(4*sizm),hashv,0),height=0.7,length=6,width=0,color=color.black)
                         print("Item found at position:",sizm)
                         return True
                     
                sizm=sizm-1
                if p.getData()==k and sizm==0:
                        
                         
                         newbox=box(pos=vector(4+(4*sizm),hashv,0),height=0.7,length=6,width=0,color=color.black)
                else:
                         return False
               
                                        
                
   def remove123(self,item,hashv,sizm,a):
       
       
       current = self.head
       previous = None
       found = False
       while not found:
           
           
           if current.getData() == item:
               
               
               found = True
           else:
               previous = current
               current = current.getNextNode()

       if previous == None:
           self.head = current.getNextNode()
       else:
           previous.setNextNode(current.getNextNode())
           
       print("Printing values now..")   
       self.size-=1
       
       curve(pos=[vector(3,hashv+0.4,0),vector(3+sizm*10,hashv+0.4,0)],radius=0.53,color=color.black)
       
       self.printNode(hashv) 
       
      
       
      
       
       
       
             

                
           


ero=LinkedList()
one=LinkedList()
two=LinkedList()
three=LinkedList()
four=LinkedList()
five=LinkedList()
six=LinkedList()
seven=LinkedList()
eight=LinkedList()
nine=LinkedList()



node1=label(visible=False)
hashtable()
def hashtable():
    a=curve(pos=[vector(-3,0,0),vector(3,0,0)],radius=0.2,color=color.cyan)
    a.append(pos=[vector(3,0,0),vector(3,10,0)],radius=0.2,color=color.cyan)
    a.append(pos=[vector(3,10,0),vector(-3,10,0)],radius=0.2,color=color.cyan)
    a.append(pos=[vector(-3,10,0),vector(-3,0,0)],radius=0.2,color=color.cyan)
    
    
    i=0

    while(i<10):
        
        e=curve(pos=[vector(-3,i,0),vector(3,i,0)],color=color.cyan,radisu=0.2)
        la=label(pos=vector(0,i+0.5,0),text=i,height=11,opacity=0,box=False,color=color.blue)
            
        i=i+1
   
        
print("Enter value:")
p1=label(text="Get input",pos=vector(-7,8,0),box=False)
prose=label(pos=vector(-5,2,0,),box=False,color=color.blue)
prose.visible=False



def keyInput(evt):
    global k
    global value
    global prose
    global j
   
    
    prose.visible=True
    
    s = evt.key
    if len(s) == 1:
        prose.text += s # append new character
    elif s == 'delete' and len(prose.text) > 0:
        prose.text = prose.text[:-1] 
         
        
    if evt.shift:
            prose.text = ''   
            
            
def getl(evt):
    global j
    global prose
    global value
   
   
    
    value=prose.text
    
    prose.text = ''  
    print("value:",value)
  

def search(evt):
    
    global value
    
    val=value
    hashv=hash(val)
    print("Inside search function:",hashv)
    if hashv==0:
       sizm=ero.getSize()
       
       ero.search(val,hashv,sizm)
       
    elif hashv==1:
        sizm=one.getSize()
        one.search(val,hashv,sizm)
    elif hashv==2:
        sizm=two.getSize()
        two.search(val,hashv,sizm)
    elif hashv==3:
        sizm=three.getSize()
        three.search(val,hashv,sizm)
    elif hashv==4:
        sizm=four.getSize()
        four.search(val,hashv,sizm)
    elif hashv==5:
        sizm=five.getSize()
        five.search(val,hashv,sizm)
    elif hashv==6:
        sizm=six.getSize()
        six.search(val,hashv,sizm)
    elif hashv==7:
        sizm=seven.getSize()
        seven.search(val,hashv,sizm)
    elif hashv==8:
        sizm=eight.getSize()
        eight.search(val,hashv,sizm)
    elif hashv==9:
        sizm=nine.getSize()
        nine.search(val,hashv,sizm) 
    else:
        print("Error")
        
def createnode(evt):
    
    global value
    global j
    ab=curve(vector(-12,0,0),vector(-8,0,0))
    ab.append(vector(-8,0,0),vector(-8,1,0))
    ab.append(vector(-12,1,0))
    ab.append(vector(-12,0,0))
    ab.append(vector(-10,0,0),vector(-10,1,0))
   
    node1=label(pos=vector(-11,0.5,0),text=value,box=False,height=10,opacity=0)
    print("Inserting")
    hashv=hash(value)
    print("Hash value is:",hashv)
    if hashv==0:
       
        sizm=ero.getSize()
        print(ero.addNode(value,hashv,sizm))
        ero.printNode()
        print("Size of zeroth bucket:")
        print(ero.getSize())
    elif hashv==1:
        
        sizm=one.getSize()
        print(one.addNode(value,hashv,sizm))
        one.printNode()
        print("Size of first bucket:")
        print(one.getSize())
    elif hashv==2:
        sizm=two.getSize()
        print(two.addNode(value,hashv,sizm))
        two.printNode()
        print("Size of second bucket:")
        print(two.getSize())
    elif hashv==3:
        sizm=three.getSize()
        print(three.addNode(value,hashv,sizm))
        three.printNode()
        print("Size of third bucket:")
        print(three.getSize())
    elif hashv==4:
        sizm=four.getSize()
        print(four.addNode(value,hashv,sizm))
        four.printNode()
        print("Size of fourth bucket:")
        print(four.getSize())
    elif hashv==5:
        sizm=five.getSize()
        print(five.addNode(value,hashv,sizm))
        five.printNode()
        print("Size of fifth bucket:")
        print(five.getSize())
    elif hashv==6:
        sizm=six.getSize()
        print(six.addNode(value,hashv,sizm))
        six.printNode()
        print("Size of sixth bucket:")
        print(six.getSize())
    elif hashv==7:
        sizm=seven.getSize()
        print(seven.addNode(value,hashv,sizm))
        seven.printNode()
        print("Size of seventh bucket:")
        print(seven.getSize())
    elif hashv==8:
        sizm=eight.getSize()
        print(eight.addNode(value,hashv,sizm))
        eight.printNode()
        print("Size of eight bucket:")
        print(eight.getSize())
    elif hashv==9:
        sizm=nine.getSize()
        print(nine.addNode(value,hashv,sizm))
        nine.printNode()
        print("Size of ninth bucket:")
        print(nine.getSize())    
    else:
        print("hashing error..")
    
    
def delete1(evt):
    
    global value
    
    val=value
    hashv=hash(val)
    print("Inside delete function:",hashv)
    if hashv==0:
       sizm=ero.getSize()
       
       ero.remove123(val,hashv,sizm)
       
    elif hashv==1:
        sizm=one.getSize()
        one.search(val,hashv,sizm)
    elif hashv==2:
        sizm=two.getSize()
        two.search(val,hashv,sizm)
    elif hashv==3:
        sizm=three.getSize()
        three.search(val,hashv,sizm)
    elif hashv==4:
        sizm=four.getSize()
        four.search(val,hashv,sizm)
    elif hashv==5:
        sizm=five.getSize()
        five.search(val,hashv,sizm)
    elif hashv==6:
        sizm=six.getSize()
        six.search(val,hashv,sizm)
    elif hashv==7:
        sizm=seven.getSize()
        seven.search(val,hashv,sizm)
    elif hashv==8:
        sizm=eight.getSize()
        eight.search(val,hashv,sizm)
    elif hashv==9:
        sizm=nine.getSize()
        nine.search(val,hashv,sizm) 
    else:
        print("Error")
        
        
    
    
    
   
    
    
    
    
    

    
    
    
def hash(v):
    hashvalue=v%10
    return hashvalue
    
    



scene.bind('keydown', keyInput)
button( bind=getl, text='GetInput' )
scene.append_to_caption('\n\n')
button( bind=createnode, text='Hash' )
scene.append_to_caption('\n\n')
button( bind=search, text='Search hash value' )
scene.append_to_caption('\n\n')
button( bind=delete1, text='Delete hash value' )
scene.append_to_caption('\n\n')

