# -------------------- Coordination Conversion ----------------
#                       Anupong
#                       20230315
#					Convert Lat/Long DMS to DD


# ----------------------Libraries----------------------
from tkinter import *
from tkinter import ttk                                        # Theme of tkinter
from tkinter import messagebox

# ----------------------my function----------------

def convertButton():
    entryOutputLat.delete(0,END)
    entryOutputLong.delete(0,END)
    try:
        lat_DMS_str = lat_DMS.get()
        long_DMS_str = long_DMS.get()
        if len(lat_DMS_str) == 0 or len(long_DMS_str) == 0:
            latDeg = float(entryLat1.get())
            latMin = float(entryLat2.get())
            latSec = float(entryLat3.get())
            latDir = comboLat1.get()
            longDeg = float(entryLong1.get())
            longMin = float(entryLong2.get())
            longSec = float(entryLong3.get())
            longDir = comboLong1.get()
        else:
            latDeg = float(lat_DMS_str.split('°')[0])
            latMin = float(lat_DMS_str.split('°')[1].split('\'')[0])
            latSec = float(lat_DMS_str.split('°')[1].split('\'')[1].split('\"')[0])
            latDir = lat_DMS_str[-1]
            longDeg = float(long_DMS_str.split('°')[0])
            longMin = float(long_DMS_str.split('°')[1].split('\'')[0])
            longSec = float(long_DMS_str.split('°')[1].split('\'')[1].split('\"')[0])
            longDir = long_DMS_str[-1]
        if latDir == 'N':
            multiplierLat = 1
        elif latDir == 'S':
            multiplierLat = -1
        else:
            messagebox.showwarning("Warning", "Bad Direction")
            return
        if longDir == 'E':
            multiplierLong = 1
        elif longDir == 'W':
            multiplierLong = -1
        else:
            messagebox.showwarning("Warning", "Bad Direction")
            return
        newLat = round((latDeg + latMin/60 + latSec/3600)*multiplierLat,5)
        newLong = round((longDeg + longMin/60 + longSec/3600)*multiplierLong,5)

        entryOutputLat.insert(0, newLat)
        entryOutputLong.insert(0, newLong)
    except ValueError:
        messagebox.showerror("Error Handling", "Please enter the valid values")
    except TypeError:
        messagebox.showerror("Error Handling", "Something goes wrong")

# -------------------------variables-----------------

# ----------------------the main code----------------

GUI = Tk()                                                      # This is main interface
GUI.title("Coordinate Conversion")                              # This is program name
#GUI.geometry('800x500')                                         # This is width x height


main_frame = Frame(GUI)                                                     # Main frame
main_frame.pack()
# -------------------------Subframe #1 --------------
input_info_frame = LabelFrame(main_frame, text= "Original Coordination")    
input_info_frame.grid(row = 0, column = 0, padx=20, pady=10)

lat_label = Label(input_info_frame, text = "Latitude DMS")
lat_label.grid(row = 0,column = 0)
lat_DMS = Entry(input_info_frame)
lat_DMS.grid(row=0, column =1)

long_label = Label(input_info_frame, text = "Longitude DMS")
long_label.grid(row = 3,column = 0)
long_DMS = Entry(input_info_frame)
long_DMS.grid(row=3, column =1)

labelLat1 = Label(input_info_frame, text = "Degrees")
labelLat1.grid(row=1, column = 1)
labelLat2 = Label(input_info_frame, text = "Minutes")
labelLat2.grid(row=1, column = 2)
labelLat3 = Label(input_info_frame, text = "Seconds")
labelLat3.grid(row=1, column = 3)
labelLat4 = Label(input_info_frame, text = "Direction")
labelLat4.grid(row=1, column = 4)

entryLat1 = Entry(input_info_frame, width = 10)
entryLat2 = Entry(input_info_frame, width = 10)
entryLat3 = Entry(input_info_frame, width = 10)

dirLat = ["N",
           "S"
]
comboLat1 =ttk.Combobox(input_info_frame, values = dirLat, width = 5)
comboLat1.set("S")
comboLat1.grid(row =2, column = 4)

entryLat1.grid(row = 2, column = 1)
entryLat2.grid(row = 2, column = 2)
entryLat3.grid(row = 2, column = 3)


labelLong1 = Label(input_info_frame, text = "Degrees")
labelLong1.grid(row=4, column = 1)
labelLong2 = Label(input_info_frame, text = "Minutes")
labelLong2.grid(row=4, column = 2)
labelLong3 = Label(input_info_frame, text = "Seconds")
labelLong3.grid(row=4, column = 3)

entryLong1 = Entry(input_info_frame, width = 10)
entryLong2 = Entry(input_info_frame, width = 10)
entryLong3 = Entry(input_info_frame, width = 10)
entryLong1.grid(row = 5, column = 1)
entryLong2.grid(row = 5, column = 2)
entryLong3.grid(row = 5, column = 3)
dirLong = ["E",
           "W"
]
comboLong1 =ttk.Combobox(input_info_frame, values = dirLong, width = 5)
comboLong1.set("E")
comboLong1.grid(row =5, column = 4)

for widget in input_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


# -------------------------Subframe #2 --------------
# calculate_frame = LabelFrame(main_frame)
# calculate_frame.grid(row = 1, column = 0, sticky = "news", padx =20, pady = 10)
# buttonConvert = Button(calculate_frame, text = "Convert", command=convertButton)
# buttonConvert.grid(row = 1, column = 0, sticky = "news")
buttonConvert = Button(main_frame, text = "Convert", command=convertButton)                     # Execute function
buttonConvert.grid(row = 1, column = 0, sticky = "news", padx = 20, pady = 10)
# for widget in calculate_frame.winfo_children():
#     widget.grid_configure(padx=10, pady=5)
# -------------------------Subframe #3 --------------
output_info_frame = LabelFrame(main_frame, text= "Converted Coordination")
output_info_frame.grid(row = 2, column = 0, sticky = "news", padx=20, pady=10)
lat_label = Label(output_info_frame, text = "Latitude Decimal Degrees")
lat_label.grid(row = 0,column = 0)
lat_label = Label(output_info_frame, text = "Longitude Decimal Degrees")
lat_label.grid(row = 2,column = 0)
entryOutputLat = Entry(output_info_frame)
entryOutputLong = Entry(output_info_frame)
entryOutputLat.grid(row =1, column = 1)
entryOutputLong.grid(row = 3, column = 1)

for widget in output_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


GUI.mainloop()



