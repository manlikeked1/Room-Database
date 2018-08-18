print('''A DATABASE FOR THE STUDENTS PRESENT ON 400 FLOOR.''')

while True:
    order=input("Enter the name of the student:")

    if order =="Ebube Donald":
        print('You are in B401.You are welcome.' )
    elif order =='Imoukhuede William':
        print('You are in B401.')
    elif order =="Basuo Bio":
        print("You are in B401")
    elif order =='Sipo(StJ)':
        print('B401')
    elif order =='B401':
        mylist= ['Sipo(StJ)','Imoukhuede William','Basuo Bio','Ebube Donald']
        print(*mylist,sep="\n")
    elif order =='James Rae':
        print('B402')
    elif order =='Tade':
        print ('B402')
    elif order =='Gabriel':
        print('B402')
    elif order =='Michael':
        print('B402')
    elif order =='B402':
        mylist=['James Rae','Tade','Gabriel','Michael']
        print(*mylist,sep='\n')
    elif order =='Jones':
        print('B403')
    elif order =='Jerry':
        print ('B403')
    elif order =='Raphael':
        print('B403')
    elif order =='King':
        print('B403')
    elif order =='B403':
        mylist=['Jones','Jerry','Raphael','King']
        print(*mylist,sep='\n')
    elif order =='Seun':
        print('B404')
    elif order =='Luke':
        print ('B404')
    elif order =='Damian':
        print('B404')
    elif order =='Tom':
        print('B404')
    elif order =='B404':
        mylist=['Seun','Luke','Damian','Tom']
        print(*mylist,sep='\n')
    elif order =='Made':
        print('B405')
    elif order =='Nonso':
        print ('B405')
    elif order =='Joshua':
        print('B405')
    elif order =='Kingsley':
        print('B405')
    elif order =='B405':
        mylist=['Made','Nonso','Joshua','Kingsley']
        print(*mylist,sep='\n')
    else:
        print('This user does not exist. Have a good day.')



