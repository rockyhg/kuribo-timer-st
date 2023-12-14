import time

import streamlit as st

COUNT_IMG = './sleeping.gif'
TIMEUP_IMG = './wakeup.gif'

def format_time(seconds):
    """Format time in seconds into mm:ss"""
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"


def main():
    st.title("Lightning Talk Timer")
    timer_time_minutes = st.number_input("Enter the time in minutes:", min_value=1, max_value=25)
    timer_time_sec = timer_time_minutes * 60

    if st.button('START'):
        with st.empty():
            for remaining in range(timer_time_sec, 0, -1):
                st.write(format_time(remaining))
                time.sleep(1)
            st.image(TIMEUP_IMG)


if __name__ == "__main__":
    main()
