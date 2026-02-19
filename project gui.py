import tkinter as tk

def which_button(button_press):
    if button_press == "btn_loc":
        txt_edit.delete("1.0", tk.END)
        txt_edit.insert(tk.END, "This is the location category.")
    elif button_press == "btn_wtd":
        txt_edit.delete("1.0", tk.END)
        txt_edit.insert(tk.END, "This is the things to do category.")
    elif button_press == "btn_tp":
        txt_edit.delete("1.0", tk.END)
        txt_edit.insert(tk.END, "This is the transportation category.")
    elif button_press == "btn_web":
        txt_edit.delete("1.0", tk.END)
        txt_edit.insert(tk.END, "This is the website category.")

window = tk.Tk()
window.title("Location")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_loc = tk.Button(frm_buttons, text="장소", command=lambda: which_button("btn_loc"))
btn_wtd = tk.Button(frm_buttons, text="할 것들", command=lambda: which_button("btn_wtd"))
btn_tp = tk.Button(frm_buttons, text="가는 방법", command=lambda: which_button("btn_tp"))
btn_web = tk.Button(frm_buttons, text="웹사이트", command=lambda: which_button("btn_web"))

btn_loc.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_wtd.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_tp.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_web.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
