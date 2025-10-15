import os
import sys
import tkinter as tk
from gui import FractalGUI
from license import check_license

def setup_environment():
    if getattr(sys, 'frozen', False):
        os.chdir(os.path.dirname(sys.executable))
def create_gui_window():
    root = tk.Tk()
    app = FractalGUI(root)
    return root, app

def run_gui(root):
    root.mainloop()

def main():
    setup_environment()

    root = tk.Tk()
    root.withdraw()
    ok = check_license()
    root.destroy()
    if not ok:
        sys.exit(1)
    root, app = create_gui_window()
    run_gui(root)



if __name__ == '__main__':
    main()
