import time

import streamlit as st

COUNTDOWN_IMG = "./sleeping.gif"
TIME_UP_IMG = "./wakeup.gif"
IMG_WIDTH = 360


def format_time(seconds):
    """Format time in seconds into mm:ss"""
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"


def main():
    st.set_page_config(page_title="Lightning Talk Timer", page_icon="⏰")
    st.title("Lightning Talk Timer")

    # セッションステートの初期化
    if "running" not in st.session_state:
        st.session_state.running = False
    if "minutes" not in st.session_state:
        st.session_state.minutes = 0
    if "seconds" not in st.session_state:
        st.session_state.seconds = 0

    # カラムの作成
    cols = st.columns(2)

    # Inputウィジェットを配置
    timer_minutes = st.number_input("Minutes:", value=1, min_value=0, max_value=60)
    timer_seconds = st.number_input(
        "Seconds:", value=0, min_value=0, max_value=59, step=10
    )

    # 合計タイマー時間(秒)を計算
    total_seconds = timer_minutes * 60 + timer_seconds

    # 設定時間を表示する場所を確保
    time_display = st.empty()

    # タイマー開始とリセットボタン
    start_button, reset_button = st.columns([1, 7])

    if start_button.button("START"):
        st.session_state.running = True

    if reset_button.button("RESET"):
        st.session_state.running = False
        st.session_state.minutes = 0
        st.session_state.seconds = 0

    # 画像表示のためのプレースホルダー
    image_placeholder = st.empty()

    # タイマー実行
    if st.session_state.running:
        image_placeholder.image(COUNTDOWN_IMG, width=IMG_WIDTH)  # カウントダウン中の画像を表示
        for remaining in range(total_seconds, 0, -1):
            time_display.markdown(f"# {format_time(remaining)}")
            time.sleep(1)
            if not st.session_state.running:
                break
        if st.session_state.running:
            time_display.markdown("# TIME UP!")
            image_placeholder.image(TIME_UP_IMG, width=IMG_WIDTH)  # タイマー終了時の画像を表示
            st.session_state.running = False
    else:
        time_display.markdown(f"# {format_time(total_seconds)}")
        image_placeholder.empty()


if __name__ == "__main__":
    main()
