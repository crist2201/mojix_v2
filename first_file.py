import streamlit as st
#from streamlit_ace import st_ace

st.title('10 Cool Beginner Python Tricks That Will Make Your Life Easier')

#

# First content
st.write("The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities. In today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.")


st.header("1. Walrus operator")
st.write("The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.")
st.markdown('**Example**:')
st.write ("If we want to check and print the length of a list:")
walrus = '''Mylist = [1,2,3]
if(l := len(mylist) > 2)
print(l)'''
st.code(walrus, language='python')
st.markdown('**Output**:')
st.code(3,language='python')


st.header("2. Splitting a string")
st.write("If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!")
st.markdown('**Example**:')
string = '''hello world
string.split()'''
st.code(string, language='python')
st.markdown('**Output**:')
st.code("['hello','world']",language='python')



st.header("3. Reversing a string")
st.write("If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.")
st.markdown('**Example**:')
string = '''str=”hello world!”
a=str[::-1]
print(a)'''
st.code(string, language='python')
st.markdown('**Output**:')
st.code("!dlrow olleh",language='python')

