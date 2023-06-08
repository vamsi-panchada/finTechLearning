import streamlit as st

col1, col2 = st.columns(2)

col1.write('column 1')
col2.write('column 2')

curcol1, valcol1 = col1.columns(2)
curcol2, valcol2 = col1.columns(2)

# def updateKey(state):
#     st.session_state.key=state

# if 'key' not in st.session_state:
#     st.session_state.key = None


# se1 = col1.empty()
# se2 = col1.empty()

# l1 = ['1', '2', '3', '4']
# s1 = se1.selectbox('list1', l1)
# l2 = l1.copy()
# l2.remove(s1)
# s2 = se2.selectbox('list2', l2)

l1 = ['1', '2', '3', '4']

cur1 = curcol1.selectbox('list1', l1)
l2 = l1.copy()
l2.remove(cur1)
cur2 = curcol2.selectbox('list2', l2)

valEmp1 = valcol1.empty()
valEmp2 = valcol2.empty()

val1 = valEmp1.number_input('Enter number1', value=1, step=1)
val2 = valEmp2.number_input('Enter number2', value=1, step=1)

# if val1>0:
#     val2 = val1*int(cur1)
#     # st.write('inside val1')
# if val2>0:
#     val1 = val2/int(cur2)
#     # st.write('inside val2')

if 'val1Prev' not in st.session_state:
    st.session_state.val1Prev=val1

if 'val2Prev' not in st.session_state:
    st.session_state.val2Prev=val2


if st.session_state.val1Prev != val1:
    res = val1*int(cur1)
    val2 = valEmp2.number_input(f'{val1} * {cur1}', value=res, step=1)
    val1 = valEmp1.number_input('Enter number1', value=val1, step=1, key='val1')
    st.session_state.val1Prev=val1
    st.session_state.val2Prev=val2

if st.session_state.val2Prev != val2:
    res = val2//int(cur2)
    val1 = valEmp1.number_input(f'{val2} // {cur2}', value=res, step=1)
    val2 = valEmp2.number_input('Enter number2', value=val2, step=1, key='val2')
    st.session_state.val1Prev=val1
    st.session_state.val2Prev=val2

# print(st.session_state)

# if st.session_state.key == 'val1':
#     st.write('inside val1 updating val2')
#     res = val1*int(cur1)
#     val2 = valEmp2.number_input(f'{val1} * {cur1}', value=res, step=1)
#     # val1 = valEmp1.number_input('Enter number1', value=val1, step=1)

# elif st.session_state.key == 'val2':
#     st.write('inside val2 updating val1')
#     res = val2/int(cur2)
#     val1 = valEmp1.number_input(f'{val2} / {cur2}', value=res, step=1.0, on_change=updateKey('val1'))
#     # val2 = valEmp2.number_input('Enter number2', value=val2, step=1)

# print(st.session_state)

st.write(f'{val1} --> {val2}')

st.write(f'{cur1} --> {cur2}')


# import streamlit as st
# from streamlit import session_state

# def on_number_change(i):
#     st.write(f"Number {i} changed!")

# # Create a number input field
# default_number = 10
# input_value1 = st.number_input('Enter a number', value=default_number, key="number_input1")
# # input_value2 = st.number_input('Enter a number', value=default_number, key="number_input2")


# # print(session_state, input_value1, input_value2)
# print(session_state, input_value1)


# # Check if the number has changed
# if session_state.number_input1 != input_value1:
#     print('i1')
#     session_state.number_input1 = input_value1
#     on_number_change(1)

# # if session_state.number_input2 != input_value2:
# #     print('i2')
# #     session_state.number_input2 = input_value2
# #     on_number_change(2)


# import streamlit as st

# input_value1 = st.number_input('Enter a number1', value=1)
# input_value2 = st.number_input('Enter a number2', value=1)

# if 'input1Prev' not in st.session_state:
#     st.session_state.input1Prev=1

# if 'input2Prev' not in st.session_state:
#     st.session_state.input2Prev=1

# if st.session_state.input1Prev != input_value1:
#     print('input1 modified')
#     st.session_state.input1Prev = input_value1

# if st.session_state.input2Prev != input_value2:
#     print('input2 modified')
#     st.session_state.input2Prev = input_value2