import pyperclip
import pyautogui
import time
import tkinter as tk
import threading

higlighted_text =[]
previous_clipboard = ''

window = tk.Tk()
listbox = tk.Listbox(window)
listbox.pack()
window.title("Clipy")
window.geometry("700x500")


def extracted_text():

    try:    
        time.sleep(6)
        mouse_x, mouse_y = pyautogui.position()


        pyautogui.hotkey('ctrl', 'c')

        time.sleep(2)

        selected_text= pyperclip.paste().strip()

        higlighted_text.append(selected_text)

        
        listbox.delete(0, tk.END)
        for line in higlighted_text:
            listbox.insert(tk.END, line)

        print("Highlighted Text:")
        print(higlighted_text)
    except KeyboardInterrupt:
        print("Incomplete execution")



def check_clipboard(stop_flag):
    global previous_clipboard

    while not stop_flag.is_set():
        current_clipboard = pyperclip.paste()

        if current_clipboard != previous_clipboard:
            previous_clipboard = current_clipboard
            extracted_text()

        time.sleep(1) 


def start_task():
    global task_thread
    global stop_flag
    stop_flag = threading.Event()
    task_thread = threading.Thread(target=lambda: check_clipboard(stop_flag))
    task_thread.start()


def stop_task():
    global stop_flag
    stop_flag.set()

def exit_program():
    stop_task() 
    window.quit()




listbox.pack()
start_button = tk.Button(window, text="Start Task", command=start_task)
start_button.pack()

stop_button = tk.Button(window, text="Stop Task", command=stop_task)
stop_button.pack()

exit_button = tk.Button(window, text="Exit", command=exit_program)
exit_button.pack()

task_thread = None

window.mainloop()





