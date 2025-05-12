import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

screen_w, screen_h = pyautogui.size()

click_touch_threshold = 0.04  
left_click_down = False
right_click_down = False

smoothening = 1  
prev_loc_x, prev_loc_y = 0, 0
curr_loc_x, curr_loc_y = 0, 0

def calculate_distance(p1, p2):
    return np.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def move_cursor(x, y):
    global prev_loc_x, prev_loc_y, curr_loc_x, curr_loc_y
    curr_loc_x = prev_loc_x + (x - prev_loc_x) / smoothening
    curr_loc_y = prev_loc_y + (y - prev_loc_y) / smoothening
    pyautogui.moveTo(curr_loc_x, curr_loc_y)
    prev_loc_x, prev_loc_y = curr_loc_x, curr_loc_y

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            thumb = hand_landmarks.landmark[4]
            index = hand_landmarks.landmark[8]
            middle = hand_landmarks.landmark[12]

            ix, iy = int(index.x * w), int(index.y * h)
            screen_x = np.interp(index.x, [0, 1], [0, screen_w])
            screen_y = np.interp(index.y, [0, 1], [0, screen_h])

            move_cursor(screen_x, screen_y)

            thumb_index_dist = calculate_distance(thumb, index)
            index_middle_dist = calculate_distance(index, middle)

            cv2.putText(frame, f"T-I Dist: {thumb_index_dist:.3f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)
            cv2.putText(frame, f"I-M Dist: {index_middle_dist:.3f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)

            # LEFT CLICK
            if thumb_index_dist < click_touch_threshold:
                if not left_click_down:
                    pyautogui.mouseDown()
                    left_click_down = True
                    cv2.putText(frame, "LEFT CLICK HOLD", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                if left_click_down:
                    pyautogui.mouseUp()
                    left_click_down = False

            # RIGHT CLICK
            if index_middle_dist < click_touch_threshold:
                if not right_click_down:
                    pyautogui.mouseDown(button='right')
                    right_click_down = True
                    cv2.putText(frame, "RIGHT CLICK HOLD", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                if right_click_down:
                    pyautogui.mouseUp(button='right')
                    right_click_down = False

            cv2.circle(frame, (ix, iy), 10, (0, 255, 0), cv2.FILLED)

    cv2.imshow('Hand Mouse Control', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
