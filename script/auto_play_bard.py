import pyautogui
import time
# pip install pyautogui
setting = dict()
target_image_path = 'image.png'
def read_text_file_to_list(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # Remove newline characters at the end of each line
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"File '{file_path}' does not exist.")
        return []

def default_set():    
    setting["confidence"] = 0.8
    setting["grayscale"] = True
    # left, top, width, height
    setting["region"]=(0, 0, 1920, 1080)

def load_set(list):
    for i in list:
        if "confidence" in i:
            print("confidence loaded: "+i)
            setting["confidence"] = float(i.split("=")[-1])
        elif "grayscale" in i:
            print("grayscale loaded: "+i)
            setting["grayscale"] = bool(i.split("=")[-1])
        elif "region" in i:
            scale_set = tuple([int(item) for item in i.split("=")[-1].split(",")])
            print("region set loaded: "+str(scale_set))
            setting["region"] = scale_set

def detect_tempo():
    while True:
        try:
            location = pyautogui.locateOnScreen(target_image_path, confidence=setting["confidence"], grayscale=setting["grayscale"], region=setting["region"])
            if location is not None:
                pyautogui.mouseDown(button='right')
                time.sleep(0.05)
                pyautogui.mouseUp(button='right')
                print("play")

        except Exception as e:
            print(f"error: {str(e)}")

if __name__ == "__main__":
    default_set()
    load_set(read_text_file_to_list("setting.txt"))
    detect_tempo()
