col1,col2,col3 = st.columns(3)
with col1:
    st.write('col1')

with col2:
    st.markdown(" ## Column 2")
    st.write('col2')

with col3:
    st.write('col3')
    st.markdown("**Often professionals**")

input_text = st.text_area(label="",placeholder="Your Email....",key="email_input")
if input_text:
    st.write("用户输入的文本是....")
    st.write(input_text)