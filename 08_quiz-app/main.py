import streamlit as st
import random
import time

st.title("🎉 Fun Quiz Challenge! 📝")



# Get user's name
name = st.text_input("👋 Enter your name to start the quiz:")

if name:
    st.subheader(f"Welcome, {name}! Let's begin the quiz. 🎯")

    # Initialize countdown state
    if "countdown_done" not in st.session_state:
        st.session_state.countdown_done = False

    # Show countdown only once per session
    if not st.session_state.countdown_done:
        countdown_placeholder = st.empty()
        for i in range(3, 0, -1):
            countdown_placeholder.write(f"⏳ Quiz starting in {i}...")
            time.sleep(1)
        countdown_placeholder.empty()
        st.session_state.countdown_done = True  # Mark countdown as completed

    # Initialize session variables
    if "questions" not in st.session_state:
        all_questions = [
            {"question": "🌍 What is the capital of France?", "options": ["Berlin", "Madrid", "Paris", "Rome"], "answer": "Paris"},
            {"question": "🚀 Who was the first person to walk on the Moon?", "options": ["Buzz Aldrin", "Yuri Gagarin", "Neil Armstrong", "Michael Collins"], "answer": "Neil Armstrong"},
            {"question": "🍕 Which country is famous for pizza?", "options": ["France", "Italy", "Mexico", "Japan"], "answer": "Italy"},
            {"question": "🎭 Who wrote 'Hamlet'?", "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Leo Tolstoy"], "answer": "William Shakespeare"},
            {"question": "⚡ What is the chemical symbol for gold?", "options": ["Au", "Ag", "Pb", "Fe"], "answer": "Au"},
            {"question": "🦁 What is the largest land animal?", "options": ["Elephant", "Giraffe", "Hippopotamus", "Rhino"], "answer": "Elephant"},
            {"question": "🎶 Who is known as the 'King of Pop'?", "options": ["Elvis Presley", "Freddie Mercury", "Michael Jackson", "Prince"], "answer": "Michael Jackson"},
            {"question": "🌊 What is the largest ocean?", "options": ["Atlantic", "Indian", "Pacific", "Arctic"], "answer": "Pacific"},
            {"question": "🧪 What planet is known as the 'Red Planet'?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "answer": "Mars"},
            {"question": "📖 How many letters are there in the English alphabet?", "options": ["24", "25", "26", "27"], "answer": "26"},
        ]
        random.shuffle(all_questions)
        st.session_state.questions = all_questions[:5]  # Pick only 5 questions
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.selected_option = None
        st.session_state.quiz_completed = False

    # Get current question
    if not st.session_state.quiz_completed and st.session_state.current_question < len(st.session_state.questions):
        q = st.session_state.questions[st.session_state.current_question]

        # Ask question
        st.subheader(q["question"])
        selected_option = st.radio("🧐 Choose your answer:", q["options"], index=None, key=f"q{st.session_state.current_question}")

        # Submit Answer
        if st.button("🚀 Submit Answer"):
            if selected_option is None:
                st.warning("⚠️ Please select an answer before submitting!")  
            else:
                if selected_option == q["answer"]:
                    st.success("🎉 ✅ Correct!")
                    st.session_state.score += 1
                else:
                    st.error(f"😞 ❌ Incorrect! The correct answer is {q['answer']}")

                # Move to next question
                time.sleep(1.5)
                st.session_state.current_question += 1
                st.rerun()
    
    # Show final results
    if st.session_state.current_question >= len(st.session_state.questions):
        st.session_state.quiz_completed = True
        st.subheader(f"🎊 Quiz Completed, {name}! 🎊")
        st.write(f"Your final score: **{st.session_state.score}/{len(st.session_state.questions)}**")
        
        # **Motivational Messages**
        if st.session_state.score == len(st.session_state.questions):
            st.success("🌟 **Perfect Score! You're a genius! Keep it up! 🚀**")
        elif st.session_state.score >= 4:
            st.info("💪 **Great Job! You're really smart! Keep learning! 🎯**")
        elif st.session_state.score >= 2:
            st.warning("👏 **Not bad! You're on the right track. Keep practicing!**")
        else:
            st.error("😅 **Keep trying! Every mistake is a lesson. Don't give up!**")

        st.balloons()

        if st.button("🔄 Play Again"):
            st.session_state.clear()
            st.rerun()
