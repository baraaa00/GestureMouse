import cv2
import numpy as np
import pyautogui
import random
import time

screen_w, screen_h = pyautogui.size()

circle_radius = 50
circle_color = (0, 0, 255)
score = 0

def new_circle_position():
    x = random.randint(circle_radius, screen_w - circle_radius)
    y = random.randint(circle_radius, screen_h - circle_radius)
    return x, y

circle_x, circle_y = new_circle_position()

game_name = "Catch The Circle"
cv2.namedWindow(game_name, cv2.WINDOW_NORMAL)
cv2.setWindowProperty(game_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    frame = np.zeros((screen_h, screen_w, 3), dtype=np.uint8)

    cv2.circle(frame, (circle_x, circle_y), circle_radius, circle_color, -1)

    mouse_x, mouse_y = pyautogui.position()

    cv2.circle(frame, (mouse_x, mouse_y), 10, (0, 255, 0), -1)

    distance = np.sqrt((mouse_x - circle_x)**2 + (mouse_y - circle_y)**2)
    if distance < circle_radius:
        score += 1
        circle_x, circle_y = new_circle_position()
        time.sleep(0.3) 
    cv2.putText(frame, f"Score: {score}", (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)

    cv2.imshow(game_name, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
