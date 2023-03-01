n=int(input("enter the number of elements"))
list1=[]
#list1=[8,9,2,1]
while True:
	print("1.List operations")
	print("2.Exit")
	choice=int(input("enter your choice"))

	if choice==1:
		while True:
			print("Operations on Lists")
			print("1.Append an element in list")
			print("2.Remove an element from list")
			print("3.Sorting of the list")
			print("4.Count an element in the list")
			print("5.Reverse the list")
			print("6.Insert an element at a specific index")
			print("7.Get maximu of the list")
			print("8.Get minimum of the list")
			print("9.Sum of all eleemnts in the list")
			print("10.POP an element in the list")
			print("11.Exit")
			ch=int(input("enter your choice"))
			if ch==1:
				e=int(input("enter an elemnt to append"))
				list1.append(e)
				print(list1)
			elif ch==2:
				e=int(input("enter element to remove"))
				list1.remove(e)
				print(list1)
			elif ch==3:
				list1.sort()
				print(list1)
			elif ch==4:
				b=int(input("enter an element to count"))
				count=list1.count(b)
				print(count)
			elif ch==5:
				list1.reverse()
				print(list1)
			elif ch==6:
				y=int(input("enter element to be inserted"))
				x=int(input("insert an element at specifc index"))
				list1.insert(x,y)
				print(list1)
			elif ch==7:
				maxx=max(list1)
				print(maxx)
			elif ch==8:
				minn1=min(list1)
				print(minn1)
			elif ch==9:
				summ=sum(list1)
				print(summ)
			elif ch==10:
				r=int(input("enter location to remove the element"))
				relement=list1.pop(r)
				print(relement)
			elif ch==11:
				break
			else:
				print("invalid choice")
