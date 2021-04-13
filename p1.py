import os

def check(a):
  f = open('data.txt', 'r')
  while(1):
    data = f.readline()
    l = len(data)
    if(l==0):
      break
    detail = data.split('-')
    if(a==detail[0]):
      print("Roll No. already exist")
      yn = input('Do you want to add another Student y/n')
      if(yn == 'y'):
        add()
      elif(yn == 'n'):
        main()
      else:
        main()
  f.close()
     
def add():
  roll_no = input('Enter Roll NO ')
  check(roll_no)
  name = input('Enter Name ')
  div = input('Enter Div ')
  year = input('Enter year ')
  f = open('data.txt', 'a')
  f.write(roll_no + "-" + name + "-" + div + "-" + year + "\n")
  f.close()
  print("|--------------------|")
  print("| Added Successfully |")
  print("|--------------------|")

def dis():
  print('*******************************************')
  print("['ROLL NO', 'NAME', 'DIV', 'YEAR']")
  f = open('data.txt', 'r')
  while(1):
    data = f.readline()
    l = len(data)
    if(l==0):
      break
    detail = data.split('-')
    print(detail)
  f.close()
  print('*******************************************')

def search():
  flag = 0;
  sr = input("Search by Roll NO.")
  f = open('data.txt', 'r')
  while(1):
    data = f.readline()
    l = len(data)
    if(l==0):
      break
    detail = data.split('-')
    if(sr==detail[0]):
      flag = 1
      print('*******************************************')
      print('Name is :' + detail[1])
      print('Division is :' + detail[2])
      print('Year is :' + detail[3])
      print('*******************************************')
      break
  f.close()
  if(flag==0):
    print('Student Not Found')

def main():
  while(1):
    print("---Student Management System---")
    print("\t1 : Add")
    print("\t2 : Display")
    print("\t3 : Search")
    print("\t4 : Delete")
    print("\t5 : Exit")

    choice = input("Enter Your choice : ")
    if(choice=='5'):
      break
    elif(choice=='1'):
      add()
    elif(choice=='2'):
      dis()
    elif(choice=='3'):
      search()
main()
    
      


