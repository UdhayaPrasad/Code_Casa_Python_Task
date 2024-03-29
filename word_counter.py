print("Word Count in Text")

print("1.Read Text from user 2.Read Text from file" )
option=int(input("Enter your option:"))

if option==1:
  string=input("Enter the string:")
  string_list=string.split()
  print("Displaying the string in list format:",string_list)
  word_count=len(string_list)
  print("WordCount in the string:",word_count)

else:
  file=open('demo.txt','r')
  count=0
  for line in file:
      words=line.split()
      count+=len(words)

  print("Displaying the text in the file:",words)
  print("Number of the words in the file:",count)

