
print("The operations are:-")
print("1.String Operations")
print("2.Tuple Operations")
print("3.Exit")
choice=int(input("enter your valid choice"))
if choice==1:
	s1=input("enter first string")
	s2=input("enter second string")
	while True:
			print("the operations are for string")
			print("1.Length of the string")
			print("2.Concatenation of the string")
			print("3.Reverse of the string")
			print("4.Uppercase of the given string")
			print("5.Lowercase of the given string")
			print("6.Maximum of the string")
			print("7.Minimum of the string")
			print("8.Sorting of the string")
			print("9.use of split into list")
			print("10.Swapcase of the string ")
			print("11.Exit")
			ch=int(input("enter your choice")

				if ch == 1:
		                	print(len(s1))
			elif ch==2:
			 	print(s1+s2)
 			elif ch==3:
				print(s1[::-1])
			elif ch==4:
		        	print(s1.upper())
			elif ch==5:
				print(s2.lower())
			elif ch==6:
		   		print(max(s1))
			elif ch==7:
                        	print(min(s2))
 		        elif ch==8:
				print("".join(sorted(s1)))
			elif ch==9:
				print(s1.split())
			elif ch==10:
				print(s2.swapcase())
			elif ch==11:
				break
					else:
						print("give a valid input")
	elif ch==2:
     	    t1=tuple(input("enter the values for first tuple")
	    t2=tuple(input("enter the values for second tuple")
	    choice=int(input("enter your choice")
	    while True:
		print("The Tuples operations are")
		print("1.Extract the elements from tuple")
		print("2.Length of the tuple")
		print("3.Joining of the tuple")
		print("4.Maximum of the tuple")
		print("5.Minimum of the tuple")
		print("6.Convert tuple into list")
		print("7.Print the last element of the tuple")
		print("8.Extract the part of the tuple")
		print("9.Repetation of the elemnets of the tuple")
		print("10.Count the element in the tuple")
		ch=int(input("enter your choice"))
		if ch==1:
		  x=int(input("enter the location")
		  print(t1[x])
		elif ch==2:
		  print(len(t1))
		elif ch==3:
		  print(t1+t2)
		elif ch==4:
		  print(max(t1))
		elif ch==5:
		  print(min(t1))
		elif ch==6:
		  l=list(t1)
		  print(l)
 		elif ch==7:
		  print(t1[-1])
		elif ch==8:
		  y=int(input("enter the starting index")
		  z=int(input("enter the ending index")
		  print(t1[y:z])
		elif ch==9:
		  print(t1*3)
		elif ch==10:
		  e=int(input("enter the input to count")
		  print(t1(e))
		elif ch==11:
 		  break
			else:
                          print("invalid choice")

	elif choice==3:
		break
		else:
	          print("invalid choice")		
		
					
