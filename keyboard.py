from pynput.keyboard import Key, Listener
import cv2 as cv
import numpy as np
import pyautogui


def on_release(key):
    if key == Key.shift:
        ix, iy = pyautogui.position()

        screenshot = pyautogui.screenshot("currentboard.png")
        screenshot = np.array(screenshot)
        screenshot = screenshot[:, :, ::-1].copy()

        haystack_img = cv.imread("currentboard.png", cv.IMREAD_UNCHANGED)
        haystack_img = cv.cvtColor(haystack_img, cv.COLOR_BGR2GRAY)

        needle_img = cv.imread("Pieces/king.png", cv.IMREAD_UNCHANGED)
        needle_img = cv.cvtColor(needle_img, cv.COLOR_BGR2GRAY)

        result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        pyautogui.moveTo(max_loc[0] + 38, max_loc[1] + 38)  # TODO tam ortasını bul
        pyautogui.click()
        pyautogui.moveTo(ix, iy)
        pyautogui.click()
    if key == Key.space:
        ix, iy = pyautogui.position()

        screenshot = pyautogui.screenshot("currentboard.png")
        screenshot = np.array(screenshot)
        screenshot = screenshot[:, :, ::-1].copy()

        haystack_img = cv.imread("currentboard.png", cv.IMREAD_UNCHANGED)
        haystack_img = cv.cvtColor(haystack_img, cv.COLOR_BGR2GRAY)

        needle_img = cv.imread("Pieces/queen.png", cv.IMREAD_UNCHANGED)
        needle_img = cv.cvtColor(needle_img, cv.COLOR_BGR2GRAY)

        result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

        pyautogui.moveTo(max_loc[0] + 38, max_loc[1] + 38)  # TODO tam ortasını bul
        pyautogui.click()
        pyautogui.moveTo(ix, iy)
        pyautogui.click()


# Collect events until released
with Listener(on_release=on_release) as listener:
    listener.join()