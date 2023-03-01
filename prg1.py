while True:
	print("1.String Operations")
	print("2.Tuple Operations")
	print("3.Exit")
	choice=int(input("enter your choice"))
	if choice==1:
		s1=input("enter first string")
		s2=input("enter second string")
		while True:
			print("String Operations are:")
			print("1.Length Of the string")
			print("2.Concatenation Of The String")
			print("3.Reverse OF the string:")
			print("4.Uppercase of the string")
			print("5.Lowercase of the string")
			print("6.Maximum of the string")
			print("7.Minimum of the string")
			print("8.Split String into list")
			print("9.Swapcase of the string")
			print("10.Sorting of the string")
			print("11.Exit")
			ch=int(input("enter your choice"))
			if ch==1:
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
				print(s1.split())
			elif ch==9:
				print(s1.swapcase())
			elif ch==10:
				print(''.join(sorted(s2)))
			elif ch==11:
				break
			else:
				print("bye,invalid choice")

	elif choice==2:
		t1=tuple(input("enter values of first"))
		t2=tuple(input("enter values of second"))
		while True:
			print("Tuple Operations are:-")
			print("1.Length of the tuple")
			print("2.Concat of two tuple")
			print("3.Extract an element from tuple")
			print("4.Maximum of the tuple")
			print("5.Minimum of the tuple")
			print("6.Extract part of the tuple")
			print("7.Convert tuple into list")
			print("8.count the element of tuple")
			print("9.use of repetition")
			print("10.print last element of the tuple")
			print("11.Exit")
			ch=int(input("enter your choice"))
			if ch==1:
				print(len(t1))
			elif ch==2:
				print(t1+t2)
			elif ch==3:
				x=int(input("enter the location"))
				print(t1[x])
			elif ch==4:
				print(max(t1))
			elif ch==5:
				print(min(t1))
			elif ch==6:
				print(t1[-1])
			elif ch==7:
				l=list(t1)
				print(l)
			elif ch==8:
				b=int(input("enter the element"))
				print(t1.count(b))
			elif ch==9:
				print(t1*3)
			elif ch==10:
				y=int(input("enter starting index"))
				z=int(input("enter the ending index"))
				print(t1[y:z])
			elif ch==11:
				break
			else:
				print("invalid choice")
	elif choice==3:
		break
	else:
		print("invalid choice")

