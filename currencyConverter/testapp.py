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

valEmp1 = valcol1.empty()
valEmp2 = valcol2.empty()

val1 = valEmp1.number_input('Enter number1', value=1, step=1)
val2 = valEmp2.number_input('Enter number2', value=1*int(cur1), step=1)

# if val1>0:
#     val2 = val1*int(cur1)
#     # st.write('inside val1')
# if val2>0:
#     val1 = val2/int(cur2)
#     # st.write('inside val2')

if 'previous_input' not in st.session_state:
    st.session_state.previous_input = None

if st.session_state.previous_input != val1:
    res = val1*int(cur1)
    val2 = valEmp2.number_input(f'{val1} * {cur1}', value=res, step=1)
    # val1 = valEmp1.number_input('Enter number1', value=val1, step=1)

elif st.session_state.previous_input != val2:
    res = val2/int(cur2)
    val1 = valEmp1.number_input(f'{val2} / {cur2}', value=res, step=1.0)
    # val2 = valEmp2.number_input('Enter number2', value=val2, step=1)

st.write(f'{val1} --> {val2}')

st.write(f'{cur1},--> {cur2}')