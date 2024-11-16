#   Todo:
#   Separate Figures from Genre dfs into dislike moderate and like
#   Average out all the values into their own categories
#
#   Required vars:
#   [3] d/m/l_color : vector3
#
#   [9] d/m/l_h/s/l_val : float
#
#   TK modules:
#   - Labels
#   [1] genre_label
#   [3] d/m/l_label
#   [9] d/m/l_h/s/l_label
#
#   - Frames
#   [1] main_frame
#   [3] d/m/l_frame

import tkinter as tk
#import GenreProcessing as gp

window = tk.Tk()
window.geometry('900x600')

# TODO: update genre
genre_label = tk.Label(window, text="Genre",font=("Times New Roman", 26))
genre_label.place(x = 400 ,y = 0 )

main_frame = tk.Frame(window, bg="#DEDEDE", width=880, height=540, borderwidth=1, relief="solid")
main_frame.place(x = 10,y = 50)
left_frame = tk.Frame(window,bg="#DEDEDE", width=293, height=540, borderwidth=1, relief="solid")
left_frame.place(x = 10,y = 50)
mid_frame = tk.Frame(window,bg="#DEDEDE", width=294, height=540, borderwidth=1, relief="solid")
mid_frame.place(x = 303,y = 50)
right_frame = tk.Frame(window,bg="#DEDEDE", width=293, height=540, borderwidth=1, relief="solid")
right_frame.place(x = 597,y = 50)

left_s_frame = tk.Frame(window,bg="#DEDEDE", width=293, height=490, borderwidth=1, relief="solid")
left_s_frame.place(x = 10,y = 50)
mid_s_frame = tk.Frame(window,bg="#DEDEDE", width=294, height=490, borderwidth=1, relief="solid")
mid_s_frame.place(x = 303,y = 50)
right_s_frame = tk.Frame(window,bg="#DEDEDE", width=293, height=490, borderwidth=1, relief="solid")
right_s_frame.place(x = 597,y = 50)

left_h_frame = tk.Frame(window,bg="#DEDEDE", width=293, height=440, borderwidth=1, relief="solid")
left_h_frame.place(x = 10,y = 50)
mid_h_frame = tk.Frame(window,bg="#DEDEDE", width=294, height=440, borderwidth=1, relief="solid")
mid_h_frame.place(x = 303,y = 50)
right_h_frame = tk.Frame(window,bg="#DEDEDE", width=293, height=440, borderwidth=1, relief="solid")
right_h_frame.place(x = 597,y = 50)

# d/m/l Labels
d_label = tk.Label(window, text="Dislike", font=("Times New Roman", 20), bg="#DEDEDE")
d_label.place(x = 105 ,y = 53 )
m_label = tk.Label(window, text="Moderate", font=("Times New Roman", 20), bg="#DEDEDE")
m_label.place(x = 398 ,y = 53 )
l_label = tk.Label(window, text="Like", font=("Times New Roman", 20), bg="#DEDEDE")
l_label.place(x = 712 ,y = 53 )

# d/m/l Frames
# TODO: [ADD BGS]
d_frame = tk.Frame(window,bg="Red", width=293, height=340, borderwidth=1, relief="solid")
d_frame.place(x = 10,y = 100)
m_frame = tk.Frame(window,bg="Blue", width=294, height=340, borderwidth=1, relief="solid")
m_frame.place(x = 303,y = 100)
l_frame = tk.Frame(window,bg="Green", width=293, height=340, borderwidth=1, relief="solid")
l_frame.place(x = 597,y = 100)

d_h_label = tk.Label(window, text="d_h_value", font=("Times New Roman", 20), bg="#DEDEDE")
d_h_label.place(x = 90,y = 442)
d_s_label = tk.Label(window, text="d_s_value", font=("Times New Roman", 20), bg="#DEDEDE")
d_s_label.place(x = 90,y = 492)
d_l_label = tk.Label(window, text="d_l_value", font=("Times New Roman", 20), bg="#DEDEDE")
d_l_label.place(x = 90,y = 542)

m_h_label = tk.Label(window, text="m_h_value", font=("Times New Roman", 20), bg="#DEDEDE")
m_h_label.place(x = 390,y = 442)
m_s_label = tk.Label(window, text="m_s_value", font=("Times New Roman", 20), bg="#DEDEDE")
m_s_label.place(x = 390,y = 492)
m_l_label = tk.Label(window, text="m_l_value", font=("Times New Roman", 20), bg="#DEDEDE")
m_l_label.place(x = 390,y = 542)

l_h_label = tk.Label(window, text="l_h_value", font=("Times New Roman", 20), bg="#DEDEDE")
l_h_label.place(x = 680,y = 442)
l_s_label = tk.Label(window, text="l_s_value", font=("Times New Roman", 20), bg="#DEDEDE")
l_s_label.place(x = 680,y = 492)
l_l_label = tk.Label(window, text="l_l_value", font=("Times New Roman", 20), bg="#DEDEDE")
l_l_label.place(x = 680,y = 542)

window.mainloop()