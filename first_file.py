import streamlit as st
#from streamlit_ace import st_ace
image = "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"

st.title('10 Cool Beginner Python Tricks That Will Make Your Life Easier')

col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    st.write("")

with col2:
    st.image(image)

with col3:
    st.write("")

# First content
st.write("The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities. In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.")


st.header("1. Walrus operator")
st.write("The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.")
st.markdown('**_Example_**:')
st.write("If we want to check and print the length of a list:")
walrus = '''Mylist = [1,2,3]
if(l := len(mylist) > 2)
print(l)'''
st.code(walrus, language='python')
st.markdown('**_Output_**:')
st.code(3)


st.header("2. Splitting a string")
st.write("If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!")
st.markdown('**_Example_**:')
string = '''hello world
string.split()'''
st.code(string, language='python')
st.markdown('**_Output_**:')
st.code("['hello','world']")


st.header("3. Reversing a string")
st.write("If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.")
st.markdown('**_Example_**:')
stringr = '''str=”hello world!”
a=str[::-1]
print(a)'''
st.code(stringr, language='python')
st.markdown('**_Output_**:')
st.code("!dlrow olleh")


st.header("4. Merging two dictionaries")
st.write("This amazing trick will help you merge two dictionaries with just 1 line of code. We just need to use ** in front of the name of the two dictionaries like below two merge them into a single dictionary:")
st.markdown('**_Example_**:')
dic = '''d1 = {“a”: 10, “b”:20}
d2 = {“c”: 30, “d”:40}
d3 = {**d1, **d2}
print(d3)'''
st.code(dic, language='python')
st.markdown('**_Output_**:')
st.code("{‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}")


st.header("5. The zip() function")
st.write("The zip() function in python can make your life a lot easier when working with lists and dictionaries. It is used to combine several lists of the same length.")
st.markdown('**_Example_**:')
zip_fun = '''colour = [“red”, “yellow”, “green”]
fruits = [‘apple’, ‘banana’, ‘mango’]
for colour, fruits in zip(colour, fruits):
print(colour, fruits)'''
st.code(zip_fun, language='python')
st.markdown('**_Output_**:')
out = '''red apple
yellow banana
green mango'''
st.code(out)

st.write("The zip() function can also be used for combining two lists into a dictionary. This method can be really helpful while grouping data from the list.")
st.markdown('**_Example_**:')
zip_fun = '''students = [“Rajesh”, “kumar”, “Kriti”]
marks = [87, 90, 88]
dictionary = dict(zip(students, marks))
print(dictionary)'''
st.code(zip_fun, language='python')
st.markdown('**_Output_**:')
st.code("{‘Rajesh’: 87, ‘kumar’: 90, ‘Kriti’: 88}")


st.header("6. Assigning multiple list values to a variable")
st.write("If you want to assign some specific values of a list to a variable and all the remaining values to another variable in a list format, you can use the following technique:")
st.markdown('**_Example_**:')
var = '''mylist = [1,2,3,4,5]
a,*b = mylist
print(f”a =”,a)
print(f”b =”,b)'''
st.code(var, language='python')
st.markdown('**_Output_**:')
out = '''a = 1
b = [2, 3, 4, 5]'''
st.code(out)
st.write("This process is also called list unpacking and you can apply this method for more than 2 variables also!")


st.header("7. Remove duplicate list items")
st.write("Do you have duplicate items in your list which you want to remove? You can do that with only one line of code using the set() function")
st.markdown('**_Example_**:')
lis = '''mylist = [1,1,1,2,2,3,3,4,4,5,6,7,7,8,9]
newlist = set(mylist)
print(newlist)'''
st.code(lis, language='python')
st.markdown('**_Output_**:')
out = '''{1, 2, 3, 4, 5, 6, 7, 8, 9}'''
st.code(out)


st.header("8. Lambda function")
st.write("If you need a function that is not very complicated, it can be done easily in one line using lambda. They are also called anonymous functions and are used heavily in data science and web development.")
st.markdown('**_Example_**:')
st.write("Let’s say you want to write a function to multiply two numbers. Instead of writing a conventional function, you can do that in one line using :")
lam = '''mul = lambda a,b: a*b
mul(5,6)'''
st.code(lam, language='python')
st.markdown('**_Output_**:')
out = '''30'''
st.code(out)


st.header("9. Swapping variable value")
st.write("One of the first programs that we learn while learning about variables is swapping the values of two variables. In python you can achieve that with one line of code:")
st.markdown('**_Example_**:')
var_val = '''a = 100
b = 200
a,b = b,a
print(f’a = ‘,a)
print(f’b = ‘,b)'''
st.code(var_val, language='python')
st.markdown('**_Output_**:')
out = '''a = 200
b = 100'''
st.code(out)


st.header("10. Use a password in your code")
st.write("This python trick is amazing for securing your code with a password. We will use the getpass() function from the library getpass which encodes your input. This will prevent anyone from running the code without a password. Isn’t that cool!")
st.markdown('**_Example_**:')
passw = '''from getpass import getpass
password = getpass(“password: “)
if password == “abcd”:
    print(“welcome strnger!”)
else:
    print(“wrong password”)'''
st.code(passw, language='python')
st.markdown('**_Output_**:')
out = '''password: **** [abcd]
Welcome stranger!
Password: **** [abdc]
Wrong password'''
st.code(out)

st.header("Conclusion")
st.write("These were a few amazing Python tips and tricks which will make your work a lot easier while coding. There are many more shortcuts like these that you can explore from the official documentation or any other website. Note: This article contains an affiliate link. This means that if you click on it and choose to buy the resource I linked above, a small portion of your subscription fee will go to me. However, the recommended resource is experienced by me and helped me in my data science career journey.")
