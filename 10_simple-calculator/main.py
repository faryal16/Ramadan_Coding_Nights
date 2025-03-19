import streamlit as st

def main():
    st.title("🧮 Calculator ")
    st.write("🚀 Enter two numbers and choose an operation")
    
    # Session state for history
    if 'history' not in st.session_state:
        st.session_state.history = []
    
    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("Enter first number", value=0.0)
        
    with col2:
        num2 = st.number_input("Enter second number", value=0.0)
        
    operation = st.selectbox("Select operation", [
        "Addition (+)", "Subtraction (-)", "Multiplication (x)", "Division (/)",
        "Modulus (%)", "Exponentiation (^)", "Floor Division (//)"
    ])
    
    if st.button("✍ Calculate"):
        try:
            if operation == "Addition (+)":
                result = num1 + num2
                symbol = "+"
            elif operation == "Subtraction (-)":
                result = num1 - num2
                symbol = "-"
            elif operation == "Multiplication (x)":
                result = num1 * num2 
                symbol = "x"
            elif operation == "Division (/)":
                if num2 == 0:
                    st.error("Error: Division by Zero") 
                    return
                result = num1 / num2
                symbol = "/"
            elif operation == "Modulus (%)":
                result = num1 % num2
                symbol = "%"
            elif operation == "Exponentiation (^)":
                result = num1 ** num2
                symbol = "^"
            elif operation == "Floor Division (//)":
                if num2 == 0:
                    st.error("Error: Division by Zero") 
                    return
                result = num1 // num2
                symbol = "//"
            
            calculation = f"{num1} {symbol} {num2} = {result}"
            st.success(calculation)
            
            # Store in history
            st.session_state.history.append(calculation)
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            
    st.write("---")        
    # Summary
    st.subheader("📊 Summary")
    st.write(f"Total calculations performed: {len(st.session_state.history)}")
    
    st.write("---")        
    # Show history
    st.subheader("📜 Calculation History")
    for cal in st.session_state.history[-5:]:  # Show last 5 calculations
        st.write(cal)
    
    
if __name__ == "__main__":
    main()
