import streamlit as st
import numpy as np
import random
import time

# 게임 보드 크기
BOARD_WIDTH = 10
BOARD_HEIGHT = 20

# 블록 정의
SHAPES = [
    np.array([[1, 1, 1, 1]]),
    np.array([[1, 1], [1, 1]]),
    np.array([[0, 1, 0], [1, 1, 1]]),
    np.array([[1, 1, 0], [0, 1, 1]]),
    np.array([[0, 1, 1], [1, 1, 0]]),
]

# 초기화
if 'board' not in st.session_state:
    st.session_state.board = np.zeros((BOARD_HEIGHT, BOARD_WIDTH), dtype=int)
    st.session_state.current_shape = random.choice(SHAPES)
    st.session_state.x = BOARD_WIDTH // 2 - 1
    st.session_state.y = 0

# 게임 보드 출력 함수
def draw_board():
    board = st.session_state.board.copy()
    shape = st.session_state.current_shape
    x, y = st.session_state.x, st.session_state.y
    
    for i in range(shape.shape[0]):
        for j in range(shape.shape[1]):
            if shape[i, j]:
                if 0 <= y + i < BOARD_HEIGHT and 0 <= x + j < BOARD_WIDTH:
                    board[y + i, x + j] = 1
    
    st.write("### Tetris Game")
    st.write("⬇️ 움직이려면 아래 버튼을 눌러 주세요!")
    st.table(board)

# 블록 이동 함수
def move(dx, dy):
    new_x = st.session_state.x + dx
    new_y = st.session_state.y + dy
    
    if 0 <= new_x < BOARD_WIDTH - len(st.session_state.current_shape[0]) and new_y < BOARD_HEIGHT:
        st.session_state.x = new_x
        st.session_state.y = new_y

def drop():
    move(0, 1)

def restart():
    st.session_state.board = np.zeros((BOARD_HEIGHT, BOARD_WIDTH), dtype=int)
    st.session_state.current_shape = random.choice(SHAPES)
    st.session_state.x = BOARD_WIDTH // 2 - 1
    st.session_state.y = 0

# UI 버튼
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️ Left"):
        move(-1, 0)
with col2:
    if st.button("⬇️ Down"):
        drop()
with col3:
    if st.button("➡️ Right"):
        move(1, 0)

if st.button("🔄 Restart"):
    restart()

draw_board()
