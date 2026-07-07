import streamlit as st

#task 1:the ui shell
st.title("Echo Chamber 9000")
st.write("Enter your details below and click Transmit to send your message.")

#task2:multi-data collection
user_name = st.text_input("Enter your Name")
user_message = st.text_input("Enter your Message")

#task 3:the action gate
if st.button("Transmit"):

    #task 4:conditional routing(edge cases)
    if user_name.strip() == "":
        st.error("Please provide your name.")
    elif user_message.strip() == "":
        st.warning("Please type a message to transmit.")
    
    #task 5:the formatted output
    else:
        st.success(
            f"Transmission successful! Greetings, {user_name}. We received your message: {user_message}"
        )

        #advanced challenge:token cost estimator
        total_characters = len(user_message)
        token_count = total_characters / 4
        st.info(
            f"System Check: Your message will consume approximately {token_count:.2f} tokens from our context window."
        )