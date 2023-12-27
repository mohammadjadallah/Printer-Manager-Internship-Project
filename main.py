from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import clr

# Add reference to the compiled ClientRuntime.dll
clr.AddReference(
    r'C:\Users\Wesam\OneDrive\Desktop\Premium_SDK_rev165_1728\Premium_SDK_rev165_1728\PremiumSDK_rev165_EN\DemoProgram\ClientRuntime\bin\Debug\ClientRuntime.dll')
# Import the PrinterCommunication class from the ClientRuntime namespace
from ClientRuntime import BusinessHelper
# Set parameters to connect with the printer
BusinessHelper.IP = "."
BusinessHelper.Port = "EspfServer00"
BusinessHelper.CommType = "PIPE"  # Or "PIPE" depending on your communication type



# Initialize the app
root = Tk()
# Add a title
root.title("Printer Manager")
# Add icon of the app
root.iconbitmap("printer.ico")
# Change the size of the app: width X height
root.geometry("642x250")
# make a non resizable window
root.resizable(False, False)

# Create a label in the lowest of the window "Evolis Print Center service running"
frame_service = Frame(root, bg='#f0f0f0', bd=0, highlightcolor='black',
                      highlightthickness=1, highlightbackground='gray')
frame_service.place(x=0, y=230, width=700, height=100)
service_running = Label(frame_service, bg="#f0f0f0", text="Evolis Print Center service running")
service_running.place(x=0, y=0)

# Create a frame for putting the printer name and the printer status
frame_printer_status_name = Frame(root, bg='white', bd=0, highlightcolor='gray',
                                  highlightthickness=0, highlightbackground='gray')
frame_printer_status_name.place(x=10, y=5, width=350, height=220)
# Create a tree view to show the printer name and printer status
tree = ttk.Treeview(frame_printer_status_name)
tree.pack(expand=True, fill='both')
# Remove the border of the tree
tree_style = ttk.Style()
tree_style.configure('Treeview', borderwidth=0, relief='flat')
# tree_style.map('Treeview', foreground=[('selected', 'gray')], background=[('selected', 'gray')])

# Create the columns in the tree
tree['columns'] = ('Printer Name', 'Printer Status')  # You can customize the column names here
tree.column('#0', width=0, stretch=NO)  # Hide the first default column
tree.column('Printer Name', anchor=W, width=20)
tree.column('Printer Status', anchor=CENTER, width=50)

# Set column headings
tree.heading('#0', text='', anchor=W)
tree.heading('Printer Name', text='Printer Name', anchor=W)
tree.heading('Printer Status', text='Printer Status', anchor=CENTER)

data = [
    ('Evolis Elypso', 'Printer off-line'),
    ('Evolis Elypso (Copy 1)', 'Printer off-line'),
    ('Evolis Primacy', 'Printer off-line'),
    ('Evolis Primacy (Copy 1)', 'Printer off-line'),
]

for i, (name, status) in enumerate(data):
    status_printer = BusinessHelper.PrinterGetState("Evolis Primacy")
    if name == "Evolis Primacy":
        tree.insert(parent='', index='end', iid=i, text='', values=(name, status_printer))
        continue

    tree.insert(parent='', index='end', iid=i, text='', values=(name, status))

firstPrinterImg = PhotoImage(file="firstPrinter.PNG")
secondPrinterImg = PhotoImage(file="secondPrinter.PNG")

# Create a menu bar
main_menu = Menu(root)

root.config(menu=main_menu)

# Adding commands
main_menu.add_command(label="About", command=lambda: about())

# Create a tools menu
tools_menu = Menu(main_menu, tearoff="off")
main_menu.add_cascade(label="Tools", menu=tools_menu)

# Create a settings menu
settings_menu = Menu(main_menu, tearoff="off")
main_menu.add_cascade(label='Settings', menu=settings_menu)
# Adding commands to the settings menu

# Create a sub menu for language and adminstration
# add a submenu
sub_menu_lang = Menu(settings_menu, tearoff=0)
# Adding the laguages to the language menu
sub_menu_lang.add_command(label='Arabic')
sub_menu_lang.add_command(label='English')
sub_menu_lang.add_command(label='Spanish')
sub_menu_lang.add_command(label='Franch')
sub_menu_lang.add_command(label='Japanese')
sub_menu_lang.add_command(label='Russian')
sub_menu_lang.add_command(label='Portuguese')
sub_menu_lang.add_command(label='Hindi')
sub_menu_lang.add_command(label='Italian')
sub_menu_lang.add_command(label='German')
sub_menu_lang.add_command(label='Dutch')
sub_menu_lang.add_command(label='Polish')
sub_menu_lang.add_command(label='Hungarian')
sub_menu_lang.add_command(label='Afrikaans')
sub_menu_lang.add_command(label='Albanian')
sub_menu_lang.add_command(label='Greek')
sub_menu_lang.add_command(label='Finnish')
sub_menu_lang.add_command(label='Turkish')
sub_menu_lang.add_command(label='Bengali')
sub_menu_lang.add_command(label='Korean')

# add a submenu for adminstration
sub_menu_admin = Menu(settings_menu, tearoff=0)
# Add the command
# new_file_img = PhotoImage(file="art.png")

sub_menu_admin.add_command(label="Stop Manager Printer Service")  # image=new_file_img)

# add the Language menu to the menubar
settings_menu.add_cascade(
    label="Language",
    menu=sub_menu_lang
)

# add the Adminstration menu to the menubar
settings_menu.add_cascade(
    label="Adminstration",
    menu=sub_menu_admin
)

settings_menu.add_command(label="Close", command=lambda: close())

# Adding a choice to open the properties
main_menu.add_command(label="properties", command=lambda: properties())

# Adding commands to the tools menu
tools_menu.add_command(label="Network and/or WI-FI printer installation wizard")
tools_menu.add_separator()
tools_menu.add_command(label="Printer regular cleaning wizard")
tools_menu.add_command(label="Printer advanced cleaning wizard")
tools_menu.add_command(label="Lamination module cleaning wizard")
tools_menu.add_separator()
tools_menu.add_command(label="Magnatic encoding module installation wizard")
# Magnatic encoding module installation wizard")
tools_menu.add_command(label="Printer flip-over activation wizard")
tools_menu.add_separator()
tools_menu.add_command(label="Printer firmware update wizard")
tools_menu.add_command(label="LCD update wizard")
tools_menu.add_command(label="Lamination module firmware update wizard")
tools_menu.add_separator()
tools_menu.add_command(label="PC/SC encoder checking wizard")
tools_menu.add_command(label="Debug mode enable/disable wizard")
tools_menu.add_command(label="Update verification wizard")
tools_menu.add_command(label="LCD calibration wizard")
tools_menu.add_command(label="Lamination only")


# Create a function for desplaying an image on the second frame
def display_image(image_file, item):
    if item == "0":
        # Create a frame for putting the printer and the details of the ribbon
        frame_ribbon_details = Frame(root, bg="#e9e6e6", bd=0, highlightcolor='gray',
                                     highlightthickness=1, highlightbackground='gray')
        frame_ribbon_details.place(x=350, y=5, width=280, height=220)
        image_label1 = Label(frame_ribbon_details, image=image_file, bd=0)
        image_label1.pack()
    if item == "1":
        frame_ribbon_details = Frame(root, bg="#e9e6e6", bd=0, highlightcolor='gray',
                                     highlightthickness=1, highlightbackground='gray')
        frame_ribbon_details.place(x=350, y=5, width=280, height=220)
        image_label2 = Label(frame_ribbon_details, image=image_file, bd=0)
        image_label2.pack()


# Create an event for change the image if the user selects a new choice "printer"
def on_double_click(event):
    item = tree.focus()
    if item == '0':
        display_image(firstPrinterImg, item="0")
    if item == '1':
        display_image(secondPrinterImg, item="1")


# Create an about window: about the app
def about():
    about_win = Toplevel(width=250, height=200)
    # Not resizable window
    # If we put it False, True => The window resizable by width
    # If we put it True, False=> The window resizable by height
    about_win.resizable(FALSE, FALSE)
    # Add icon of the app
    about_win.iconbitmap("printer.ico")
    about_d1 = Label(about_win, text="Printer Manager", font="Arial 20 bold")
    about_d2 = Label(about_win, text="===> Version 0.0.1", font="Arial 10 bold")
    about_d3 = Label(about_win, text="===> Manage Your Printers", font="Arial 10 bold")
    about_d1.place(x=0, y=0)
    about_d2.place(x=0, y=60)
    about_d3.place(x=0, y=90)

    about_win.mainloop()


# Close the app
def close():
    # Destroying the app
    root.destroy()


# Open Properties Window When User Chooses Properties from the Menu
def properties():
    selected_item = tree.focus()
    if selected_item:
        item_text = tree.item(selected_item, "values")[0]  # Get the text of the selected item in the tree
        properties_win = Toplevel()
        properties_win.title(f"Properties for {item_text}")
        # Not resizable window  
        properties_win.resizable(FALSE, FALSE)
        # Change the geometry of the window
        properties_win.geometry("700x600")
        # Icon
        properties_win.iconbitmap("printer.ico")

        # Add a background to properties window
        # bg_img = PhotoImage(file="bg_properties.png")
        # bg_properties = Label(properties_win, image=bg_img)
        # bg_properties.place(x=0, y=0)
        properties_win.config(bg="#d3e1f5")
        # Properties Wedgets
        # Printing Label
        Label(properties_win, text="Printing", bg="#d3e1f5", fg="#528fd8", font="arial 12 bold").grid(column=1, row=4,
                                                                                                      sticky="W")
        # Create the first list "Printing"
        n = StringVar()
        printing = ttk.Combobox(properties_win, width=27, textvariable=n)

        # Adding combobox drop down list
        printing['values'] = ('Card orientation',
                              'Feeder / Hopper',
                              'Ribbon',
                              'Front side graphical settings',
                              'Back side graphical settings',
                              'Front side varnish adjustment',
                              'Back side varnish adjustment',
                              'Front side text area',
                              'Back side text area',
                              'Advanced color parameters',
                              'Advanced parameters')

        printing.grid(column=1, row=5)
        printing.configure(state="disabled")

        # Create the 2nd list "Encoding"
        # encoding Label
        Label(properties_win, text="Encoding", bg="#d3e1f5", fg="#528fd8", font="arial 12 bold").grid(column=1, row=6,
                                                                                                      sticky="W")

        n1 = StringVar()
        encoding = ttk.Combobox(properties_win, width=27, textvariable=n1)
        # Adding the list
        encoding["values"] = ("Magnetic")
        encoding.grid(column=1, row=7)
        encoding.configure(state="disabled")

        # Create the 3rd list "Cleaning"
        Label(properties_win, text="Cleaning", bg="#d3e1f5", fg="#528fd8", font="arial 12 bold").grid(column=1, row=8,
                                                                                                      sticky="W")

        n2 = StringVar()
        cleaning = ttk.Combobox(properties_win, width=27, textvariable=n2)
        # Adding the list to the cleaning combobox
        cleaning["values"] = ("Cleaning details", "Proceed with cleaning")
        cleaning.grid(column=1, row=9)
        cleaning.configure(state="disabled")

        # Create the 4th list "System Details"
        Label(properties_win, text="System Details", bg="#d3e1f5", fg="#528fd8", font="arial 12 bold").grid(column=1,
                                                                                                            row=10,
                                                                                                            sticky="W")

        n3 = StringVar()
        system_detailes = ttk.Combobox(properties_win, width=27, textvariable=n3)
        # Adding the list to the system detailes combobox
        system_detailes["values"] = ("Printer detailes", "Ribbon detailes", "System detailes", "Testing cards")
        system_detailes.grid(column=1, row=11)
        system_detailes.configure(state="disabled")

        # Create the 5th list "Maintenance"
        Label(properties_win, text="Maintenance", bg="#d3e1f5", fg="#528fd8", font="arial 12 bold").grid(column=1,
                                                                                                         row=12,
                                                                                                         sticky="W")

        n4 = StringVar()
        maintenance = ttk.Combobox(properties_win, width=27, textvariable=n4)
        # Adding the list to the maintenance combobox
        maintenance["values"] = ("Printing commands prompting", "Magnatic encoding prompting",
                                 "Printer driver settings managements", "Installable options",
                                 "Print head replacement", "Firmware update")
        maintenance.grid(column=1, row=13)
        maintenance.configure(state="disabled")

        # Create the 6th list "Adminstration"
        Label(properties_win, text="Adminstration", bg="#d3e1f5", fg="#528fd8", font="arial 12 bold").grid(column=1,
                                                                                                           row=14,
                                                                                                           sticky="W")

        n5 = StringVar()
        adminstration = ttk.Combobox(properties_win, width=27, textvariable=n5)
        # Adding the list to the adminstration combobox
        adminstration["values"] = ("Standby settings", "Network settings")
        adminstration.grid(column=1, row=15)
        adminstration.configure(state="disabled")

        framo = Frame(properties_win, bg="#bfbfbf")
        framo.place(x=200, y=0, width=28, height=600)

        bg_design = PhotoImage(file="bg_properties.png")
        Label(properties_win, image=bg_design, bg="#d3e1f5").place(x=-10, y=280)

        # Radio button to enable the list 
        valOfRadio = IntVar()  # Basically Links Any Radiobutton With The Variable=i.
        r1 = Radiobutton(properties_win, text="", value=1, variable=valOfRadio, bg="#bfbfbf",
                         cursor="hand2", activebackground="#d3e1f5")
        r1.place(x=200)
        r2 = Radiobutton(properties_win, text="", value=2, variable=valOfRadio, bg="#bfbfbf",
                         cursor="hand2", activebackground="#d3e1f5")
        r2.place(x=200, y=45)
        r3 = Radiobutton(properties_win, text="", value=3, variable=valOfRadio, bg="#bfbfbf",
                         cursor="hand2", activebackground="#d3e1f5")
        r3.place(x=200, y=90)
        r4 = Radiobutton(properties_win, text="", value=4, variable=valOfRadio, bg="#bfbfbf",
                         cursor="hand2", activebackground="#d3e1f5")
        r4.place(x=200, y=135)
        r5 = Radiobutton(properties_win, text="", value=5, variable=valOfRadio, bg="#bfbfbf",
                         cursor="hand2", activebackground="#d3e1f5")
        r5.place(x=200, y=180)
        r6 = Radiobutton(properties_win, text="", value=6, variable=valOfRadio, bg="#bfbfbf",
                         cursor="hand2", activebackground="#d3e1f5")
        r6.place(x=200, y=225)

        # Here the elements on the window will change when user choose a specific choice
        # for example if the user choose the card orientation from printing list
        # The elements will be regarding to card orientation
        # if printing.get() == "Card orientation":
        #     Label(properties_win, text="Card Orientation", bg="red").place(x=500, y=20, width=300)

        # Function to enable/disable comboboxes based on radio button selection
        def enable_comboboxes(*args):
            selected_radio = valOfRadio.get()

            # Clear the text in all comboboxes
            printing.set("")
            encoding.set("")
            cleaning.set("")
            system_detailes.set("")
            maintenance.set("")
            adminstration.set("")

            # Disable all comboboxes initially
            printing.configure(state="disabled")
            encoding.configure(state="disabled")
            cleaning.configure(state="disabled")
            system_detailes.configure(state="disabled")
            maintenance.configure(state="disabled")
            adminstration.configure(state="disabled")

            # Enable the corresponding combobox based on the selected radio button
            if selected_radio == 1:
                printing.configure(state="normal")

            elif selected_radio == 2:
                encoding.configure(state="normal")
            elif selected_radio == 3:
                cleaning.configure(state="normal")
            elif selected_radio == 4:
                system_detailes.configure(state="normal")
            elif selected_radio == 5:
                maintenance.configure(state="normal")
            elif selected_radio == 6:
                adminstration.configure(state="normal")

        # Bind the function to the radio buttons' variable
        valOfRadio.trace("w", enable_comboboxes)

        def on_combobox_select(event):
            global prt_land_value, card, rotator, card_rotated_image, \
                card_rotated_image_landscape, card_rotated_image_landscape180, typeRb, fBSet1, \
                fBSet2, resolution_index, contrast_img, brightness_img, val_adj, bitmap_value, custom_bitmap_img, checked, \
                t1, t2, t3, c, e, cleaning_card, cleaning_card2

            selected_item = printing.get()
            encoding_item = encoding.get()
            cleaning_item = cleaning.get()
            maintenance_item = maintenance.get()

            # Create a frame to show the elements of the user selection 
            # in this way we can destroy all elements of each selection
            #  when the user select new choice from the list 
            frame_for_showing_elements_selection = Frame(properties_win, bg="#d3e1f5")
            frame_for_showing_elements_selection.place(x=228, y=0, width=500, height=700)

            # Clear and destroy all widgets from the previous choice
            for widget in frame_for_showing_elements_selection.winfo_children():
                widget.destroy()

            if selected_item == "Card orientation":
                # Show additional label or element
                Label(frame_for_showing_elements_selection, text="Card orientation", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                # Landscape | Portrait | Front side | Back side | rotate 180
                prt_land_value = IntVar(value=1)
                portrait_rad = Radiobutton(frame_for_showing_elements_selection, text="Portrait", value=1,
                                           variable=prt_land_value, bg="#bfbfbf",
                                           cursor="hand2", activebackground="#d3e1f5")
                portrait_rad.place(x=20, y=100)
                landscape_rad = Radiobutton(frame_for_showing_elements_selection, text="Landscape", value=2,
                                            bg="#bfbfbf",
                                            variable=prt_land_value, cursor="hand2", activebackground="#d3e1f5")
                landscape_rad.place(x=20, y=140)

                # Front side label
                Label(frame_for_showing_elements_selection, text="Front side", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=200, width=400)  # Adjust the position

                # Back side label
                Label(frame_for_showing_elements_selection, text="Back side", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=380, width=400)  # Adjust the position

                back_side_check_button = Checkbutton(frame_for_showing_elements_selection, text="Rotate the card 180°",
                                                     activebackground="#d3e1f5", bg="#d3e1f5",
                                                     state="disabled")

                back_side_check_button.place(x=20, y=420)
                # Check box
                rotator = IntVar()
                check_180 = Checkbutton(frame_for_showing_elements_selection, text="Rotate the card 180°",
                                        activebackground="#d3e1f5", bg="#d3e1f5",
                                        variable=rotator, command=lambda: rotate_180())
                check_180.place(x=20, y=240)

                def rotate_180():
                    # Rotate the portrait image
                    if rotator.get() == 1 and prt_land_value.get() == 1:
                        card_label.config(image=card_rotated_image)

                    # Rotate the landscape image
                    elif rotator.get() == 1 and prt_land_value.get() == 2:
                        card_label.config(image=card_rotated_image_landscape180)

                    # Dont rotate the portrait image
                    elif rotator.get() == 0 and prt_land_value.get() == 1:
                        card_label.config(image=card)
                    # Dont rotate the landscape image
                    elif rotator.get() == 0 and prt_land_value.get() == 2:
                        card_label.config(image=card_rotated_image_landscape)

                def check_portrait_landscape():
                    if prt_land_value.get() == 1:
                        card_label.config(image=card)
                        rotator.set(0)  # This will uncheck the button
                    else:
                        card_label.config(image=card_rotated_image_landscape)
                        rotator.set(0)  # This will uncheck the button

                # Show the card 
                # Landscape
                card_rotated_image_landscape = PhotoImage(file="landscapIdCard.png")
                card_rotated_image_landscape180 = PhotoImage(file="landscapIdCard180D.png")
                # Portrait
                card_rotated_image = PhotoImage(file="idCard180D.png")
                card = PhotoImage(file="idCard.png")

                card_label = Label(properties_win, image=card)
                card_label.place(x=500, y=250)

            if selected_item == "Feeder / Hopper":
                Label(frame_for_showing_elements_selection, text="Feeder / Hopper", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                # Thre labels: 1. Card insertion 2. Card exit 3. Card ejected in error
                Label(frame_for_showing_elements_selection, text="Card insertion", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=100, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection, text="Card exit", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=200, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection, text="Card ejected in error", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=300, width=400)  # Adjust the position

                # Adding the lists under each Label
                n_insertion1 = StringVar()
                card_insertion = ttk.Combobox(frame_for_showing_elements_selection, width=50,
                                              textvariable=n_insertion1)
                card_insertion["values"] = ("Default Selection", "Manual feeding")
                card_insertion.set("Default Selection")
                card_insertion.place(x=50, y=140)

                n_insertion2 = StringVar()
                card_insertion = ttk.Combobox(frame_for_showing_elements_selection, width=50,
                                              textvariable=n_insertion2)
                card_insertion["values"] = ("Default Selection", "Manual reception", "Reject box")
                card_insertion.set("Default Selection")
                card_insertion.place(x=50, y=240)

                n_insertion3 = StringVar()
                card_insertion = ttk.Combobox(frame_for_showing_elements_selection, width=50,
                                              textvariable=n_insertion3)
                card_insertion["values"] = ("Default Selection", "Reject box", "Manual receptopn")
                card_insertion.set("Default Selection")
                card_insertion.place(x=50, y=340)

            if selected_item == "Ribbon":
                Label(frame_for_showing_elements_selection, text="Ribbon", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                # Show the details of the ribbon of the printer
                Label(frame_for_showing_elements_selection,
                      text="Ribbon Detailes:",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=70, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="    Identification:       Unknown",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=20, y=105, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="    Category: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=20, y=135, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="    Description: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=20, y=165, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="    Type: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=20, y=195, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="    Remaining capacity:",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=20, y=225, width=400)  # Adjust the position
                # Disabled check button
                auto_id = Checkbutton(frame_for_showing_elements_selection, text="Auto-Id",
                                      activebackground="#d3e1f5", bg="#d3e1f5",
                                      state="disabled")
                auto_id.place(x=20, y=245, width=100)

                Label(frame_for_showing_elements_selection, text="Manual settings", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=280, width=500)  # Adjust the position

                typeRb = IntVar()
                ribbon_type = Checkbutton(frame_for_showing_elements_selection, text="Select the ribbon type",
                                          activebackground="#d3e1f5", bg="#d3e1f5",
                                          variable=typeRb, command=lambda: check_type_ribbon())
                ribbon_type.place(x=20, y=310, width=200)

                # Ribbon types list
                n_ribbon_type = StringVar()
                ribbon_type_list = ttk.Combobox(frame_for_showing_elements_selection, width=60,
                                                textvariable=n_ribbon_type)
                ribbon_type_list["values"] = ("BLACK", "HOLO", "BLACK PRIME",
                                              "RED", "WHITE", "GREEN", "BLUE",
                                              "SCRATCH OFF", "METAL SILVER", "METAL GOLD",
                                              "SIGNATURE", "BLACKFLEX")
                ribbon_type_list.place(x=50, y=340)
                ribbon_type_list.configure(state="disabled")

                # Front side and back side settings 
                Label(frame_for_showing_elements_selection, text="Front side and Back side settings ", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=380, width=500)  # Adjust the position

                # front and back lists
                fBSet1 = StringVar()
                fBSet_list1 = ttk.Combobox(frame_for_showing_elements_selection, width=40,
                                           textvariable=fBSet1)
                fBSet_list1["values"] = ("Disabled", "Enabled")
                fBSet_list1.place(x=150, y=420)
                fBSet_list1.configure(state="disabled")
                fBSet_list1.set("Disabled")

                fBSet2 = StringVar()
                fBSet_list2 = ttk.Combobox(frame_for_showing_elements_selection, width=40,
                                           textvariable=fBSet2)
                fBSet_list2["values"] = ("")
                fBSet_list2.place(x=150, y=450)
                fBSet_list2.configure(state="disabled")

                Label(frame_for_showing_elements_selection, text="Duplex mode :", bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=20, y=420, width=90)  # Adjust the position

                Label(frame_for_showing_elements_selection, text="Type :", bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=20, y=450, width=90)  # Adjust the position

                # Resolution
                Label(frame_for_showing_elements_selection, text="Resolution", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=500, width=500)  # Adjust the position

                resolution_index = StringVar()
                resolution_Value = ttk.Combobox(frame_for_showing_elements_selection, width=40,
                                                textvariable=resolution_index)
                resolution_Value["values"] = ("300 dots per inch", "600 dots per inch",
                                              "1200 dots per inch")
                resolution_Value.set("300 dots per inch")
                resolution_Value.place(x=50, y=550)

                def check_type_ribbon():
                    if typeRb.get() == 1:
                        ribbon_type_list.configure(state="normal")
                    else:
                        ribbon_type_list.configure(state="disabled")

            if selected_item == "Front side graphical settings":
                Label(frame_for_showing_elements_selection, text="Front side graphical settings", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Ribbon Detailes",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=60, width=150)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="BLACK",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=100, width=100)  # Adjust the position

                Label(frame_for_showing_elements_selection, text="Colour panels adjustment", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=140, width=500)  # Adjust the position

                # Creating a slider for Brightness and Contrast 
                Label(frame_for_showing_elements_selection, text="Brightness :", bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=200, width=90)  # Adjust the position

                Label(frame_for_showing_elements_selection, text="Contrast :", bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=280, width=90)  # Adjust the position

                brightness_slider = Scale(frame_for_showing_elements_selection,
                                          from_=0, to=100, orient=HORIZONTAL,
                                          bg="#d3e1f5", )
                brightness_slider.place(x=130, y=180, width=250)

                contrast_slider = Scale(frame_for_showing_elements_selection,
                                        from_=0, to=100, orient=HORIZONTAL,
                                        bg="#d3e1f5", )
                contrast_slider.place(x=130, y=260, width=250)

                # Brightness and contrast icons for sliders
                brightness_img = PhotoImage(file="brightness.png")
                contrast_img = PhotoImage(file="contrast.png")

                Label(frame_for_showing_elements_selection, image=brightness_img, bg="#d3e1f5",
                      anchor="w").place(x=400, y=170)

                Label(frame_for_showing_elements_selection, image=contrast_img, bg="#d3e1f5",
                      anchor="w").place(x=400, y=250)

                Label(frame_for_showing_elements_selection, text="Black panel adjustment", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=320, width=500)  # Adjust the position

                # Adding a disabled list
                panelAdjust1 = ttk.Combobox(frame_for_showing_elements_selection,
                                            width=60, state="disable")
                panelAdjust1.place(x=50, y=360)

                val_adj = StringVar()
                panelAdjust2 = ttk.Combobox(frame_for_showing_elements_selection,
                                            width=60, textvariable=val_adj)
                panelAdjust2["values"] = ("Black and White", "Grayscale",
                                          "Dithering", "Clustered Dithering")
                panelAdjust2.set("Black and White")
                panelAdjust2.place(x=50, y=400)

                # Creating the monocrome resin adjustment               
                Label(frame_for_showing_elements_selection, text="Monochrome resin adjustment :", bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=480, width=190)  # Adjust the position

                monochrome_slider = Scale(frame_for_showing_elements_selection,
                                          from_=0, to=20, orient=HORIZONTAL,
                                          bg="#d3e1f5", )
                monochrome_slider.place(x=270, y=460, width=150)

            if selected_item == "Back side graphical settings":
                Label(frame_for_showing_elements_selection, text="Back side graphical settings", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Ribbon Detailes",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=60, width=150)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="BLACK",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=100, width=100)  # Adjust the position

                Label(frame_for_showing_elements_selection, text="Colour panels adjustment", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=140, width=500)  # Adjust the position

                # Creating a slider for Brightness and Contrast 
                Label(frame_for_showing_elements_selection, text="Brightness :", bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=200, width=90)  # Adjust the position

                Label(frame_for_showing_elements_selection, text="Contrast :", bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=280, width=90)  # Adjust the position

                brightness_slider = Scale(frame_for_showing_elements_selection,
                                          from_=0, to=100, orient=HORIZONTAL,
                                          bg="#d3e1f5", state="disabled")
                brightness_slider.place(x=130, y=180, width=250)

                contrast_slider = Scale(frame_for_showing_elements_selection,
                                        from_=0, to=100, orient=HORIZONTAL,
                                        bg="#d3e1f5", state="disabled")
                contrast_slider.place(x=130, y=260, width=250)

                # Brightness and contrast icons for sliders
                brightness_img = PhotoImage(file="brightness.png")
                contrast_img = PhotoImage(file="contrast.png")

                Label(frame_for_showing_elements_selection, image=brightness_img, bg="#d3e1f5",
                      anchor="w").place(x=400, y=170)

                Label(frame_for_showing_elements_selection, image=contrast_img, bg="#d3e1f5",
                      anchor="w").place(x=400, y=250)

                Label(frame_for_showing_elements_selection, text="Black panel adjustment", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=320, width=500)  # Adjust the position

                # Adding a disabled list
                panelAdjust1 = ttk.Combobox(frame_for_showing_elements_selection,
                                            width=60, state="disabled")
                panelAdjust1.place(x=50, y=360)

                val_adj = StringVar()
                panelAdjust2 = ttk.Combobox(frame_for_showing_elements_selection,
                                            width=60, textvariable=val_adj, state="disabled")
                panelAdjust2["values"] = ("Black and White", "Grayscale",
                                          "Dithering", "Clustered Dithering")

                panelAdjust2.place(x=50, y=400)

                # Creating the monocrome resin adjustment               
                Label(frame_for_showing_elements_selection, text="Monochrome resin adjustment :", bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=480, width=190)  # Adjust the position

                monochrome_slider = Scale(frame_for_showing_elements_selection,
                                          from_=0, to=20, orient=HORIZONTAL,
                                          bg="#d3e1f5", state="disabled")
                monochrome_slider.place(x=270, y=460, width=150)

            # Where I reached : Front side varnish adjustment
            if selected_item == "Front side varnish adjustment":
                Label(frame_for_showing_elements_selection, text="Front side varnish adjustment", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Ribbon Detailes",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=60, width=150)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="BLACK",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=100, width=100)  # Adjust the position

                Label(frame_for_showing_elements_selection, text="Varnish type", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=140, width=500)  # Adjust the position

                # Varnish Type
                varnish_type = StringVar()
                varnish_list = ttk.Combobox(frame_for_showing_elements_selection, width=60,
                                            textvariable=varnish_type)

                varnish_list.place(x=50, y=180)
                varnish_list.configure(state="disabled")

                Label(frame_for_showing_elements_selection, text="Custom bitmap management", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=220, width=500)  # Adjust the position

                bitmap_value = StringVar()
                bitmap_list = ttk.Combobox(frame_for_showing_elements_selection, width=60,
                                           textvariable=bitmap_value)

                bitmap_list["values"] = ("overlay", "custom_afnor", "custom_iso", "custom_mag")
                bitmap_value.set('None')
                bitmap_list.place(x=50, y=260)

                # Create a button for browsing file
                browse = Button(frame_for_showing_elements_selection, text="Browse",
                                bg="#bfbfbf", command=lambda: filedialog.askopenfile())

                browse.place(x=50, y=300, width=90)

                custom_bitmap_img = PhotoImage(file="landscapIdCard.png")

                Label(frame_for_showing_elements_selection, image=custom_bitmap_img,
                      anchor="w").place(x=170, y=300)

                Label(frame_for_showing_elements_selection, text="Varnish adjustment", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=400, width=500)  # Adjust the position

                varnish_slider = Scale(frame_for_showing_elements_selection,
                                       from_=0, to=20, orient=HORIZONTAL,
                                       bg="#d3e1f5", state="disabled")
                varnish_slider.place(x=50, y=440, width=250)

            if selected_item == "Back side varnish adjustment":
                Label(frame_for_showing_elements_selection, text="Back side varnish adjustment", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Ribbon Detailes",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=60, width=150)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="BLACK",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=100, width=100)  # Adjust the position

                Label(frame_for_showing_elements_selection, text="Varnish type", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=140, width=500)  # Adjust the position

                # Varnish Type
                varnish_type = StringVar()
                varnish_list = ttk.Combobox(frame_for_showing_elements_selection, width=60,
                                            textvariable=varnish_type)

                varnish_list.place(x=50, y=180)
                varnish_list.configure(state="disabled")

                Label(frame_for_showing_elements_selection, text="Custom bitmap management", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=220, width=500)  # Adjust the position

                bitmap_value = StringVar()
                bitmap_list = ttk.Combobox(frame_for_showing_elements_selection, width=60,
                                           textvariable=bitmap_value)

                bitmap_list["values"] = ("overlay", "custom_afnor", "custom_iso", "custom_mag")
                bitmap_value.set('None')
                bitmap_list.place(x=50, y=260)

                # Create a button for browsing file
                browse = Button(frame_for_showing_elements_selection, text="Browse",
                                bg="#bfbfbf", command=lambda: filedialog.askopenfile())

                browse.place(x=50, y=300, width=90)

                custom_bitmap_img = PhotoImage(file="landscapIdCard.png")

                Label(frame_for_showing_elements_selection, image=custom_bitmap_img,
                      anchor="w").place(x=170, y=300)

                Label(frame_for_showing_elements_selection, text="Varnish adjustment", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=400, width=500)  # Adjust the position

                varnish_slider = Scale(frame_for_showing_elements_selection,
                                       from_=0, to=20, orient=HORIZONTAL,
                                       bg="#d3e1f5", state="disabled")
                varnish_slider.place(x=50, y=440, width=250)

            if selected_item == "Front side text area":
                Label(frame_for_showing_elements_selection, text="Front side text area", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Front side",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=60, width=150)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Upper left corner coordinates (x, y)",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=100, width=230)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Lower right corner coordinates (x, y)",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=130, width=230)  # Adjust the position

                disabled_button1 = Button(frame_for_showing_elements_selection, text="",
                                          bg="#bfbfbf", state="disabled")

                disabled_button1.place(x=360, y=100, width=60)

                disabled_button2 = Button(frame_for_showing_elements_selection, text="",
                                          bg="#bfbfbf", state="disabled")
                disabled_button2.place(x=360, y=130, width=60)

                area = Text(frame_for_showing_elements_selection, state="disabled")
                area.place(x=20, y=180, width=400, height=160)

                add = Button(frame_for_showing_elements_selection, text="Add",
                             bg="#bfbfbf", state="disabled")
                add.place(x=20, y=350, width=120)

                delete = Button(frame_for_showing_elements_selection, text="Delete all",
                                bg="#bfbfbf", state="disabled")
                delete.place(x=160, y=350, width=120)

                delete_all = Button(frame_for_showing_elements_selection, text="Delete",
                                    bg="#bfbfbf", state="disabled")
                delete_all.place(x=300, y=350, width=120)

                Label(frame_for_showing_elements_selection,
                      text='Those settings allow to define the area to print in black text in the card\nusing X and Y values. Can be used only if the "Front side graphical settings"\n(respectively "Back side graphical settings") are defined with "Only black\ntext" value.',
                      fg="black", bg="#d3e1f5", justify="left").place(x=20, y=380, width=400, height=80)

            if selected_item == "Back side text area":
                Label(frame_for_showing_elements_selection, text="Back side text area", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Front side",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=60, width=150)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Upper left corner coordinates (x, y)",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=100, width=230)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Lower right corner coordinates (x, y)",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=130, width=230)  # Adjust the position

                disabled_button1 = Button(frame_for_showing_elements_selection, text="",
                                          bg="#bfbfbf", state="disabled")

                disabled_button1.place(x=360, y=100, width=60)

                disabled_button2 = Button(frame_for_showing_elements_selection, text="",
                                          bg="#bfbfbf", state="disabled")
                disabled_button2.place(x=360, y=130, width=60)

                area = Text(frame_for_showing_elements_selection, state="disabled")
                area.place(x=20, y=180, width=400, height=160)

                add = Button(frame_for_showing_elements_selection, text="Add",
                             bg="#bfbfbf", state="disabled")
                add.place(x=20, y=350, width=120)

                delete = Button(frame_for_showing_elements_selection, text="Delete all",
                                bg="#bfbfbf", state="disabled")
                delete.place(x=160, y=350, width=120)

                delete_all = Button(frame_for_showing_elements_selection, text="Delete",
                                    bg="#bfbfbf", state="disabled")
                delete_all.place(x=300, y=350, width=120)

                Label(frame_for_showing_elements_selection,
                      text='Those settings allow to define the area to print in black text in the card\nusing X and Y values. Can be used only if the "Front side graphical settings"\n(respectively "Back side graphical settings") are defined with "Only black\ntext" value.',
                      fg="black", bg="#d3e1f5", justify="left").place(x=20, y=380, width=400, height=80)

            if selected_item == "Advanced color parameters":
                Label(frame_for_showing_elements_selection, text="Advanced color parameters", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Smoothing",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=60, width=150)  # Adjust the position

                advacned_color_paramter = ttk.Combobox(frame_for_showing_elements_selection, width=60)
                advacned_color_paramter["values"] = ("Advanced", "Standard", "None")
                advacned_color_paramter.place(x=40, y=90)

                Label(frame_for_showing_elements_selection,
                      text="Short Panel Management",
                      bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=130, width=250)  # Adjust the position

                panel = ttk.Combobox(frame_for_showing_elements_selection, width=60, state="disabled")
                panel.place(x=40, y=170)

                Label(frame_for_showing_elements_selection,
                      text="First color point: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=20, y=200, width=200)  # Adjust the position

                disabled_button1 = Button(frame_for_showing_elements_selection, text="",
                                          bg="#bfbfbf", state="disabled", relief=RIDGE)

                disabled_button1.place(x=160, y=200, width=60)

                Label(frame_for_showing_elements_selection,
                      text="Color adjustment",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=20, y=250, width=200)  # Adjust the position

                checked = IntVar(value=0)
                color_controlers = Checkbutton(frame_for_showing_elements_selection, text="Enabled",
                                               activebackground="#d3e1f5", bg="#d3e1f5",
                                               variable=checked, command=lambda: enable())
                color_controlers.place(x=30, y=270)

                Label(frame_for_showing_elements_selection,
                      text="Yellow",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=50, y=310, width=200)  # Adjust the position

                # Yellow Color
                Label(frame_for_showing_elements_selection,
                      text="- Brightness: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=55, y=330, width=200)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="- Contrast: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=55, y=350, width=200)  # Adjust the position

                bright_color_slider_y = Scale(frame_for_showing_elements_selection,
                                              from_=0, to=20, orient=HORIZONTAL,
                                              bg="#528fd8", sliderrelief='raised', showvalue=False)
                bright_color_slider_y.place(x=140, y=330, width=250)

                contrast_color_slider_y = Scale(frame_for_showing_elements_selection,
                                                from_=0, to=20, orient=HORIZONTAL,
                                                bg="#528fd8", sliderrelief='raised', showvalue=False)
                contrast_color_slider_y.place(x=140, y=350, width=250)

                # Magenta Color
                Label(frame_for_showing_elements_selection,
                      text="Magenta",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=50, y=390, width=200)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="- Brightness: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=55, y=410, width=200)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="- Contrast: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=55, y=430, width=200)  # Adjust the position

                bright_color_slider_m = Scale(frame_for_showing_elements_selection,
                                              from_=0, to=20, orient=HORIZONTAL,
                                              bg="#528fd8", sliderrelief='raised', showvalue=False)
                bright_color_slider_m.place(x=140, y=410, width=250)

                contrast_color_slider_m = Scale(frame_for_showing_elements_selection,
                                                from_=0, to=20, orient=HORIZONTAL,
                                                bg="#528fd8", sliderrelief='raised', showvalue=False)
                contrast_color_slider_m.place(x=140, y=430, width=250)

                # Cyan Color
                Label(frame_for_showing_elements_selection,
                      text="Cyan",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=50, y=470, width=200)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="- Brightness: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=55, y=490, width=200)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="- Contrast: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=55, y=510, width=200)  # Adjust the position

                bright_color_slider_c = Scale(frame_for_showing_elements_selection,
                                              from_=0, to=20, orient=HORIZONTAL,
                                              bg="#528fd8", sliderrelief='raised', showvalue=False)
                bright_color_slider_c.place(x=140, y=490, width=250)

                contrast_color_slider_c = Scale(frame_for_showing_elements_selection,
                                                from_=0, to=20, orient=HORIZONTAL,
                                                bg="#528fd8", sliderrelief='raised', showvalue=False)
                contrast_color_slider_c.place(x=140, y=510, width=250)

                # Disabling the sliders
                contrast_color_slider_y.configure(state="disabled")
                bright_color_slider_y.configure(state="disabled")
                contrast_color_slider_m.configure(state="disabled")
                bright_color_slider_m.configure(state="disabled")
                contrast_color_slider_c.configure(state="disabled")
                bright_color_slider_c.configure(state="disabled")

                def enable():
                    # enable the colors sliders
                    if checked.get() == 1:
                        contrast_color_slider_y.configure(state="normal")
                        bright_color_slider_y.configure(state="normal")
                        contrast_color_slider_m.configure(state="normal")
                        bright_color_slider_m.configure(state="normal")
                        contrast_color_slider_c.configure(state="normal")
                        bright_color_slider_c.configure(state="normal")

                    else:
                        contrast_color_slider_y.configure(state="disabled")
                        bright_color_slider_y.configure(state="disabled")
                        contrast_color_slider_m.configure(state="disabled")
                        bright_color_slider_m.configure(state="disabled")
                        contrast_color_slider_c.configure(state="disabled")
                        bright_color_slider_c.configure(state="disabled")

            if selected_item == "Advanced parameters":
                Label(frame_for_showing_elements_selection, text="Advanced parameters", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Monochrome printing speed",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=60, width=320)  # Adjust the position

                monochrome_slider = Scale(frame_for_showing_elements_selection,
                                          from_=0, to=10, orient=HORIZONTAL,
                                          bg="#528fd8", sliderrelief='raised', showvalue=True)
                monochrome_slider.place(x=40, y=100, width=250)

            # Encoding...
            if encoding_item == "Magnetic":
                Label(frame_for_showing_elements_selection, text="Magnetic", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Monochrome printing speed",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 13 bold",
                      anchor="w").place(x=20, y=60, width=320)  # Adjust the position

                checked = IntVar(value=0)
                auto_id = Checkbutton(frame_for_showing_elements_selection, text="Auto-Id",
                                      activebackground="#d3e1f5", bg="#d3e1f5",
                                      variable=checked, command=lambda: enabler())
                auto_id.place(x=30, y=85)
                auto_id.select()

                # Comboboxes
                t1 = StringVar()
                t2 = StringVar()
                t3 = StringVar()

                track1 = ttk.Combobox(frame_for_showing_elements_selection, width=60, textvariable=t1)
                track1["values"] = ("ISO1", "ISO2", "ISO3", "SIPASS", "C2", "JIS2", "C4", "DISABLED")
                track1.place(x=40, y=110)

                track2 = ttk.Combobox(frame_for_showing_elements_selection, width=60, textvariable=t2)
                track2["values"] = ("ISO1", "ISO2", "ISO3", "SIPASS", "C2", "JIS2", "C4", "DISABLED")
                track2.place(x=40, y=140)

                track3 = ttk.Combobox(frame_for_showing_elements_selection, width=60, textvariable=t3)
                track3["values"] = ("ISO1", "ISO2", "ISO3", "SIPASS", "C2", "JIS2", "C4", "DISABLED")
                track3.place(x=40, y=170)

                track1.set("ISO1")
                track2.set("ISO2")
                track3.set("ISO3")

                track1.configure(state="disabled")
                track2.configure(state="disabled")
                track3.configure(state="disabled")

                Label(frame_for_showing_elements_selection,
                      text="Coercivity",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 13 bold",
                      anchor="w").place(x=20, y=200, width=320)  # Adjust the position

                c = StringVar()
                coercivity = ttk.Combobox(frame_for_showing_elements_selection, width=60, textvariable=c)
                coercivity["values"] = ("Disabled", "Low coercivity", "High coercivity")
                coercivity.set("Disabled")
                coercivity.place(x=40, y=230)

                Label(frame_for_showing_elements_selection,
                      text="Encoding through an application",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 13 bold",
                      anchor="w").place(x=20, y=260, width=320)  # Adjust the position

                e = StringVar()
                encoding_over_app = ttk.Combobox(frame_for_showing_elements_selection, width=60, textvariable=e)
                encoding_over_app["values"] = ("Disabled", "Default", "Customized")
                encoding_over_app.set("Disabled")
                encoding_over_app.place(x=40, y=290)

                Label(frame_for_showing_elements_selection,
                      text="Lead-in code: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=320, width=100)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Trail-in code: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=365, width=100)  # Adjust the position

                disabled_button1 = Button(frame_for_showing_elements_selection, text="",
                                          bg="#bfbfbf", state="disabled")

                disabled_button1.place(x=160, y=320, width=40)

                disabled_button2 = Button(frame_for_showing_elements_selection, text="",
                                          bg="#bfbfbf", state="disabled")

                disabled_button2.place(x=160, y=360, width=40)

                def enabler():
                    # enable the colors sliders
                    if checked.get() == 1:
                        track1.set("ISO1")
                        track2.set("ISO2")
                        track3.set("ISO3")

                        track1.configure(state="disabled")
                        track2.configure(state="disabled")
                        track3.configure(state="disabled")
                    else:

                        track1.configure(state="normal")
                        track2.configure(state="normal")
                        track3.configure(state="normal")

            # Cleaining...
            if cleaning_item == "Cleaning details":
                Label(frame_for_showing_elements_selection, text="Cleaning details", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Statistics",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 13 bold",
                      anchor="w").place(x=20, y=60, width=320)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Next cleaning in : ",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 10 bold",
                      anchor="w").place(x=20, y=100, width=320)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Last cleaning at : ",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 10 bold",
                      anchor="w").place(x=20, y=140, width=320)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Number of regular cleanings : ",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 10 bold",
                      anchor="w").place(x=20, y=180, width=320)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Number of advanced cleanings : ",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 10 bold",
                      anchor="w").place(x=20, y=220, width=320)  # Adjust the position

                e1 = Entry(frame_for_showing_elements_selection)
                e1.insert(0, "       0")
                e1.configure(state="disabled")
                e1.place(x=250, y=100, width=50)

                e2 = Entry(frame_for_showing_elements_selection)
                e2.insert(0, "   1083")
                e2.configure(state="disabled")
                e2.place(x=250, y=140, width=50)

                e3 = Entry(frame_for_showing_elements_selection)
                e3.insert(0, "       3")
                e3.configure(state="disabled")
                e3.place(x=250, y=180, width=50)

                e4 = Entry(frame_for_showing_elements_selection)
                e4.insert(0, "       0")
                e4.configure(state="disabled")
                e4.place(x=250, y=220, width=50)

                Label(frame_for_showing_elements_selection,
                      text="Warranty cycle",
                      bg="#bfbfbf",
                      fg="#528fd8", font="arial 13 bold",
                      anchor="w").place(x=20, y=260, width=320)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Not performed",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 10 bold",
                      anchor="w").place(x=40, y=290, width=320)  # Adjust the position

            if cleaning_item == "Proceed with cleaning":
                Label(frame_for_showing_elements_selection, text="Proceed with cleaning", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Reqular cleaning",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 13 bold",
                      anchor="w").place(x=20, y=60, width=320)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Reqular cleaning is a guarantee for\noptimal printing quality and protects\nthe warranty of your printer",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=120, width=320, height=80)  # Adjust the position

                cleaning_card = PhotoImage(file="cardco.PNG")
                Label(frame_for_showing_elements_selection,
                      image=cleaning_card, anchor="w").place(x=260, y=80)  # Adjust the position

                start_cleaning = Button(frame_for_showing_elements_selection, text="Start Cleaning",
                                bg="#bfbfbf")
                start_cleaning.place(x=20, y=260, width=420)

                cleaning_card2 = PhotoImage(file="cardco2.PNG")
                Label(frame_for_showing_elements_selection,
                      image=cleaning_card2, anchor="w").place(x=260, y=300)  # Adjust the position

                start_cleaning2 = Button(frame_for_showing_elements_selection, text="Start Cleaning",
                                bg="#bfbfbf")
                start_cleaning2.place(x=20, y=500, width=420)

                Label(frame_for_showing_elements_selection,
                      text="Advanced cleaning",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 13 bold",
                      anchor="w").place(x=20, y=300, width=200)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Advanced cleaning is required to fully\nclean all transport rollers",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=40, y=350, width=220, height=80)  # Adjust the position

            if maintenance_item == "Printing commands prompting":
                Label(frame_for_showing_elements_selection, text="Printing commands prompting", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Printer command",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 13 bold",
                      anchor="w").place(x=20, y=60, width=320)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Command: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=30, y=100, width=320)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Answer: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=30, y=140, width=320)  # Adjust the position

                e_commands = Entry(frame_for_showing_elements_selection)
                e_commands.place(x=120, y=100, width=300)

                a_commands = Entry(frame_for_showing_elements_selection)
                a_commands.place(x=120, y=140, width=300)

                import threading as th
                send_command = Button(frame_for_showing_elements_selection, text="send", bg="#bfbfbf", command=lambda: th.Thread(target=send_command()))
                send_command.place(x=30, y=180, width=80)

                checked = IntVar(value=0)
                direct_communication = Checkbutton(frame_for_showing_elements_selection, text="Direct communication",
                                      activebackground="#d3e1f5", bg="#d3e1f5",
                                      variable=checked)
                direct_communication.place(x=120, y=180)
                direct_communication.select()

                eject_card = Button(frame_for_showing_elements_selection, text="Eject card", bg="#bfbfbf", command=lambda: eject_card())
                eject_card.place(x=340, y=180, width=80)

                Label(frame_for_showing_elements_selection,
                      text="Printer information",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=30, y=240, width=200)  # Adjust the position

                def eject_card():
                    # Set parameters
                    BusinessHelper.IP = "."
                    BusinessHelper.Port = "EspfServer00"
                    BusinessHelper.CommType = "PIPE"  # Or "PIPE" depending on your communication type

                    # Call methods | Eject card
                    enter = BusinessHelper.SendCommand("Evolis Primacy", "Sis", "10")
                    eject = BusinessHelper.SendCommand("Evolis Primacy", "Se", "10")  # Eject it

                def send_command():
                    get_command = e_commands.get().strip()


                    # Import the PrinterCommunication class from the ClientRuntime namespace
                    from ClientRuntime import BusinessHelper

                    # Set parameters
                    BusinessHelper.IP = "."
                    BusinessHelper.Port = "EspfServer00"
                    BusinessHelper.CommType = "PIPE"  # Or "PIPE" depending on your communication type

                    # Call methods
                    result = BusinessHelper.SendCommand("Evolis Primacy", get_command, "10")
                    # print("Result:", result)
                    a_commands.delete(0, END)
                    a_commands.insert(0, result)

            if maintenance_item == "Magnatic encoding prompting":
                Label(frame_for_showing_elements_selection, text="Magnatic encoding prompting", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Printer command",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 13 bold",
                      anchor="w").place(x=20, y=60, width=320)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Command: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=30, y=100, width=320)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Answer: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=30, y=140, width=320)  # Adjust the position

                e_commands = Entry(frame_for_showing_elements_selection)
                e_commands.place(x=120, y=100, width=300)

                a_commands = Entry(frame_for_showing_elements_selection)
                a_commands.place(x=120, y=140, width=300)

                send_command = Button(frame_for_showing_elements_selection, text="send", bg="#bfbfbf")
                send_command.place(x=30, y=180, width=80)

                checked = IntVar(value=0)
                direct_communication = Checkbutton(frame_for_showing_elements_selection, text="Direct communication",
                                      activebackground="#d3e1f5", bg="#d3e1f5",
                                      variable=checked)
                direct_communication.place(x=120, y=180)
                direct_communication.select()

                eject_card = Button(frame_for_showing_elements_selection, text="Eject card", bg="#bfbfbf")
                eject_card.place(x=340, y=180, width=80)

                write_read_magnetic = Button(frame_for_showing_elements_selection, text="Encode and Read Tracks",
                                             bg="#bfbfbf", command=lambda: magnatic_ecoding(t1_commands.get(), int(t3_commands.get()), int(t5_commands.get())))
                write_read_magnetic.place(x=180, y=480, width=180)

                Label(frame_for_showing_elements_selection,
                      text="Magnetic encoding",
                      bg="#d3e1f5",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=30, y=240, width=200)  # Adjust the position

                direct_communication2 = Checkbutton(frame_for_showing_elements_selection, text="Direct communication",
                                      activebackground="#d3e1f5", bg="#d3e1f5")
                direct_communication2.place(x=120, y=270)
                direct_communication2.select()

                t1_commands = Entry(frame_for_showing_elements_selection)
                t1_commands.place(x=120, y=300, width=300)
                t2_commands = Entry(frame_for_showing_elements_selection, fg="red", font="arial 10 bold")
                t2_commands.place(x=120, y=325, width=300)

                t3_commands = Entry(frame_for_showing_elements_selection)
                t3_commands.place(x=120, y=350, width=300)
                t4_commands = Entry(frame_for_showing_elements_selection, fg="red", font="arial 10 bold")
                t4_commands.place(x=120, y=375, width=300)

                t5_commands = Entry(frame_for_showing_elements_selection)
                t5_commands.place(x=120, y=400, width=300)
                t6_commands = Entry(frame_for_showing_elements_selection, fg="red", font="arial 10 bold")
                t6_commands.place(x=120, y=425, width=300)

                Label(frame_for_showing_elements_selection,
                      text="Track 1: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=30, y=300, width=60)  # Adjust the position

                Label(frame_for_showing_elements_selection,
                      text="Track 2: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=30, y=350, width=60)  # Adjust the position


                Label(frame_for_showing_elements_selection,
                      text="Track 3: ",
                      bg="#d3e1f5",
                      fg="black", font="arial 10",
                      anchor="w").place(x=30, y=400, width=60)  # Adjust the position

                def magnatic_ecoding(track1: str, track2: int, track3: int, read: bool = False):
                    # Request 1: Set the encoder’s coercivity
                    coercivity = BusinessHelper.SendCommand("Evolis Primacy", "Pmc;h", "10")
                    # Request 2: Set the encoder’s track 1 format (here ISO1).
                    set_track1 = BusinessHelper.SendCommand("Evolis Primacy", "Pmt;1;1", "10")
                    # Request 3: Set the encoder’s track 2 format (here ISO2).
                    set_track2 = BusinessHelper.SendCommand("Evolis Primacy", "Pmt;2;2", "10")
                    # Request 4: Set the encoder’s track 3 format (here ISO3).
                    set_track3 = BusinessHelper.SendCommand("Evolis Primacy", "Pmt;3;3", "10")
                    # Request 5: Start the sequence (initiate printer's communication)
                    start_sequence = BusinessHelper.SendCommand("Evolis Primacy", "Ss", "10")
                    # Request 6: Download Magnetic track 1 data to the Evolis printer
                    download_magnetic_t1 = BusinessHelper.SendCommand("Evolis Primacy", f"Dm;1;{track1}", "10")
                    # Request 7: Download Magnetic track 2 data to the Evolis printer
                    download_magnetic_t2 = BusinessHelper.SendCommand("Evolis Primacy", f"Dm;2;{track2}", "10")
                    # Request 8: Download Magnetic track 3 data to the Evolis printer
                    download_magnetic_t3 = BusinessHelper.SendCommand("Evolis Primacy", f"Dm;3;{track3}", "10")
                    # Request 9: Write magnetic data to the card
                    write_magnetic = BusinessHelper.SendCommand("Evolis Primacy", "Smw", "10")
                    # Request 10: Read magnetic data of the card
                    read_magnetic_t1 = BusinessHelper.SendCommand("Evolis Primacy", "Smr;1", "10")
                    read_magnetic_t2 = BusinessHelper.SendCommand("Evolis Primacy", "Smr;2", "10")
                    read_magnetic_t3 = BusinessHelper.SendCommand("Evolis Primacy", "Smr;3", "10")
                    read_magnetic_t3 = BusinessHelper.SendCommand("Evolis Primacy", "Se", "10")

                    t2_commands.delete(0, END)
                    t4_commands.delete(0, END)
                    t6_commands.delete(0, END)

                    t2_commands.insert(0, read_magnetic_t1)
                    t4_commands.insert(0, read_magnetic_t2)
                    t6_commands.insert(0, read_magnetic_t3)

                    if read:
                        print("Result:", "Track1:", read_magnetic_t1, "Track2:", read_magnetic_t2, "Track3:",
                              read_magnetic_t3)
                    else:
                        return {"Track1": read_magnetic_t1, "Track2": read_magnetic_t2, "Track3": read_magnetic_t3}

            if maintenance_item == "Printer driver settings managements":
                Label(frame_for_showing_elements_selection, text="Printer driver settings managements", bg="#bfbfbf",
                      fg="#528fd8", font="arial 15 bold",
                      anchor="w").place(x=20, y=20, width=400)  # Adjust the position

                load_from_file = Button(frame_for_showing_elements_selection, text="Load from file", bg="#bfbfbf")
                load_from_file.place(x=20, y=100, width=400)

                save_to_file = Button(frame_for_showing_elements_selection, text="Save to file", bg="#bfbfbf")
                save_to_file.place(x=20, y=140, width=400)

                synco_to_printer = Button(frame_for_showing_elements_selection,
                                          text="Synchronisation to the printer", bg="#bfbfbf", state="disabled")
                synco_to_printer.place(x=20, y=180, width=400)

            try:
                # Bind the rotator, and landscape as well portrait
                rotator.trace("w", lambda *args: enable())
                rotator.trace("w", lambda *args: rotate_180())
                prt_land_value.trace("w", lambda *args: check_portrait_landscape())
                typeRb.trace("w", lambda *args: check_type_ribbon())

            except:
                pass

        # Bind the function to the combobox's selection event
        printing.bind("<<ComboboxSelected>>", on_combobox_select)
        encoding.bind("<<ComboboxSelected>>", on_combobox_select)
        cleaning.bind("<<ComboboxSelected>>", on_combobox_select)
        maintenance.bind("<<ComboboxSelected>>", on_combobox_select)

        # mainloop for make the window static 
        properties_win.mainloop()


# Bind the click event to the treeview
tree.bind('<Double-1>', on_double_click)
# Bind the double-click event to the treeview for showing the properties window

if __name__ == '__main__':
    root.mainloop()
