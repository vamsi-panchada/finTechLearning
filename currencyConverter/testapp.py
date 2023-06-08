import streamlit as st

col1, col2 = st.columns(2)

col1.write('column 1')
col2.write('column 2')

curcol1, valcol1 = col1.columns(2)
curcol2, valcol2 = col1.columns(2)


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

val1 = valcol1.number_input('Enter number1')
val2 = valcol2.number_input('Enter number2')

if val1>0:
    val2 = val1*int(cur1)
    # st.write('inside val1')
if val2>0:
    val1 = val2/int(cur2)
    # st.write('inside val2')

st.write(f'{val1} --> {val2}')

st.write(f'{cur1},--> {cur2}')