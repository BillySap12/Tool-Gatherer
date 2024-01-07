from tkinter import *
from tkinter import messagebox
import subprocess
import time

class Main:
    def __init__(self) -> None:
        self.window = Tk()

        self.window.title("Login")
        self.window.geometry("200x200")
        self.window.config(bg='black')

        self.user_string_var = StringVar()
        self.pass_string_var = StringVar()

        self.label = Label(self.window, text="Username", font=('Arial', 15), fg='green', bg='black')
        self.label.pack()

        self.user_entry = Entry(self.window, fg='green', bg='black', textvariable=self.user_string_var, show="*")
        self.user_entry.pack()

        self.label = Label(self.window, text="Password", font=('Arial', 15), fg='green', bg='black')
        self.label.pack()

        self.pass_entry = Entry(self.window, fg='green', bg='black', textvariable=self.pass_string_var, show='*')
        self.pass_entry.pack()

        self.button = Button(self.window, text="Submit", font=('Arial', 15), fg='green', bg='black', command=self.login)
        self.button.pack(padx=10, pady=20)

        self.window.mainloop()

    def login(self):
        self.password = self.pass_entry.get()
        self.username = self.user_entry.get()

        if self.password != "Bre@kFree" and self.username != "admin5":
            messagebox.showerror("Error", "Invalid Password/and/or Username!")
        else:
            self.window.destroy()
            self.root = Tk()

            self.root.title("Dashboard")
            self.root.geometry("540x450")
            self.root.config(bg='black')

            self.label = Label(self.root, text="Click the corresponding button\naccording to your needs.", font=('Arial', 20), fg='green', bg='black')
            self.label.pack()

            self.osint_button = Button(self.root, text="OSINT", font=('Arial', 15), fg='green', bg='black', command=self.osint)
            self.osint_button.pack(padx=10, pady=20)

            self.ddos_button = Button(self.root, text="DDoS", font=('Arial', 15), fg='green', bg='black', command=self.ddos)
            self.ddos_button.pack(padx=10, pady=20)

            self.phish_button = Button(self.root, text="Phishing", font=('Arial', 15), fg='green', bg='black', command=self.phish)
            self.phish_button.pack(padx=10, pady=20)

            self.notice_text = """

__________________________________________________________________________________

 Warning! We are not responsible for any mess you might\ncause with these tools!
__________________________________________________________________________________                                                              

"""

            self.notice = Label(self.root, text=self.notice_text, font=('Arial', 15), fg='green', bg='black')
            self.notice.pack()

            self.root.mainloop()

    def osint(self):
        self.response = messagebox.askyesno("Question", "Would you like to see a list of tools?")

        if self.response:
            self.window = Tk()

            self.window.title("List")
            self.window.geometry("300x300")
            self.window.config(bg='black')

            self.label = Label(self.window, text="LIST OF OSINT TOOLS:", font=('Arial', 15), fg='green', bg='black')
            self.label.pack(padx=10, pady=20)

            self.label = Label(self.window, text="• Sherlock", font=('Arial', 15), fg='green', bg='black')
            self.label.pack(padx=10, pady=20)

            self.label = Label(self.window, text="• Maigret", font=('Arial', 15), fg='green', bg='black')
            self.label.pack()

            self.label = Label(self.window, text="• Harvester", font=('Arial', 15), fg='green', bg='black')
            self.label.pack(padx=10, pady=20)

            self.button = Button(self.window, text="Download", font=('Arial', 15), fg='green', bg='black', command=self.download_osint)
            self.button.pack(padx=10, pady=20)

            self.window.mainloop()
        

    def ddos(self):
        self.response = messagebox.askyesno("Question", "Would you like to see a list of tools?")

        if self.response:
            self.window = Tk()

            self.window.title("List")
            self.window.geometry("300x300")
            self.window.config(bg='black')

            self.label = Label(self.window, text="LIST OF DDoS TOOLS:", font=('Arial', 15), fg='green', bg='black')
            self.label.pack(padx=10, pady=20)

            self.label = Label(self.window, text="• MHDDoS", font=('Arial', 15), fg='green', bg='black')
            self.label.pack(padx=10, pady=20)

            self.label = Label(self.window, text="• CC-attack", font=('Arial', 15), fg='green', bg='black')
            self.label.pack()

            self.label = Label(self.window, text="• DDoS Ripper", font=('Arial', 15), fg='green', bg='black')
            self.label.pack(padx=10, pady=20)

            self.button = Button(self.window, text="Download", font=('Arial', 15), fg='green', bg='black', command=self.download_ddos)
            self.button.pack(padx=10, pady=20)

            self.window.mainloop()

    def phish(self):
        self.response = messagebox.askyesno("Question", "Would you like to see a list of tools?")

        if self.response:
            self.window = Tk()

            self.window.title("List")
            self.window.geometry("300x300")
            self.window.config(bg='black')

            self.label = Label(self.window, text="LIST OF PHISHING TOOLS:", font=('Arial', 15), fg='green', bg='black')
            self.label.pack(padx=10, pady=20)

            self.label = Label(self.window, text="• ZPhisher", font=('Arial', 15), fg='green', bg='black')
            self.label.pack(padx=10, pady=20)

            self.label = Label(self.window, text="• Maxphisher", font=('Arial', 15), fg='green', bg='black')
            self.label.pack()

            self.label = Label(self.window, text="• Camphish", font=('Arial', 15), fg='green', bg='black')
            self.label.pack(padx=10, pady=20)

            self.button = Button(self.window, text="Download", font=('Arial', 15), fg='green', bg='black', command=self.download_phish)
            self.button.pack(padx=10, pady=20)

            self.window.mainloop()

    def download_ddos(self):
        self.window = Tk()

        self.window.title("Download DDoS")
        self.window.config(bg='black')

        self.list = Listbox(self.window, font=('Arial', 15), fg='green', bg='black', width=50, height=3)
        self.list.pack()
        
        self.middle_index = len(self.list.get(0, END)) // 2

        self.list.insert(self.middle_index, "• MHDDoS")
        self.list.insert(self.middle_index, "• CC-attack")
        self.list.insert(self.middle_index, "• DDoS Ripper")

        self.list.see(self.middle_index)

        self.button = Button(self.window, text="Submit", font=('Arial', 15), fg='green', bg='black', command=self.submit_ddos)
        self.button.pack()
        
        self.window.mainloop()

    def download_osint(self):
        self.window = Tk()

        self.window.title("Download OSINT")
        self.window.config(bg='black')

        self.list = Listbox(self.window, font=('Arial', 15), fg='green', bg='black', width=50, height=3)
        self.list.pack()
        
        self.middle_index = len(self.list.get(0, END)) // 2

        self.list.insert(self.middle_index, "• SHERLOCK")
        self.list.insert(self.middle_index, "• MAIGRET")
        self.list.insert(self.middle_index, "• HARVESTER")

        self.list.see(self.middle_index)

        self.button = Button(self.window, text="Submit", font=('Arial', 15), fg='green', bg='black', command=self.submit_osint)
        self.button.pack()
        
        self.window.mainloop()


    def download_phish(self):
        self.window = Tk()

        self.window.title("Download Phish")
        self.window.config(bg='black')

        self.list = Listbox(self.window, font=('Arial', 15), fg='green', bg='black', width=50, height=3)
        self.list.pack()
        
        self.middle_index = len(self.list.get(0, END)) // 2

        self.list.insert(self.middle_index, "• ZPHISHER")
        self.list.insert(self.middle_index, "• MAXPHISHER")
        self.list.insert(self.middle_index, "• CAMPHISHER")

        self.list.see(self.middle_index)

        self.button = Button(self.window, text="Submit", font=('Arial', 15), fg='green', bg='black', command=self.submit_phish)
        self.button.pack()
        
        self.window.mainloop()

    def submit_osint(self):
        self.selected_item_index = self.list.curselection()

           
        if self.selected_item_index:
            self.selected_item = self.list.get(self.selected_item_index)

            if self.selected_item == "• SHERLOCK":
                self.response = messagebox.askyesno("Question", "Are you on Linux?")
                if self.response:
                    self.response2 = messagebox.askyesno("Question", "Do you have git installed?")
                    if self.response2:
                        self.clone_sherlock_repository()

                    else:
                        self.install_git_and_clone_sherlock_repository()

                else:
                    messagebox.showinfo("Info", "We're sorry, but you need to be on Linux to download Sherlock!")

            elif self.selected_item == "• MAIGRET":
                self.response = messagebox.askyesno("Question", "Are you on Linux?")
                if self.response:
                    self.response2 = messagebox.askyesno("Question", "Do you have git installed?")
                    if self.response2:
                        self.clone_maigret_repository()

                    else:
                        self.install_git_and_clone_maigret_repository()

                else:
                    messagebox.showinfo("Info", "We're sorry, but you need to be on Linux to download Maigret!")

            elif self.selected_item == "• HARVESTER":
                self.response = messagebox.askyesno("Question", "Are you on Linux?")
                if self.response:
                    self.response2 = messagebox.askyesno("Question", "Do you have git installed?")
                    if self.response2:
                        self.clone_harvester_repository()

                    else:
                        self.install_git_and_clone_harvester_repository()

        else:
            messagebox.showerror("Error", "Please select a tool first!")

    def submit_ddos(self):
        self.selected_item_index = self.list.curselection()

           
        if self.selected_item_index:
            self.selected_item = self.list.get(self.selected_item_index)

            if self.selected_item == "• MHDDoS":
                self.response = messagebox.askyesno("Question", "Are you on Linux?")
                if self.response:
                    self.response2 = messagebox.askyesno("Question", "Do you have git installed?")
                    if self.response2:
                        self.clone_mhddos_repository()

                    else:
                        self.install_git_and_clone_mhddos_repository()

                else:
                    messagebox.showinfo("Info", "We're sorry, but you need to be on Linux to download Sherlock!")

            elif self.selected_item == "• CC-attack":
                self.response = messagebox.askyesno("Question", "Are you on Linux?")
                if self.response:
                    self.response2 = messagebox.askyesno("Question", "Do you have git installed?")
                    if self.response2:
                        self.clone_ccattack_repository()

                    else:
                        self.install_git_and_clone_ccattack_repository()

                else:
                    messagebox.showinfo("Info", "We're sorry, but you need to be on Linux to download Maigret!")

            elif self.selected_item == "• DDoS Ripper":
                self.response = messagebox.askyesno("Question", "Are you on Linux?")
                if self.response:
                    self.response2 = messagebox.askyesno("Question", "Do you have git installed?")
                    if self.response2:
                        self.clone_ddosripper_repository()

                    else:
                        self.install_git_and_clone_ddosripper_repository()

        else:
            messagebox.showerror("Error", "Please select a tool first!")

    def submit_phish(self):
        self.selected_item_index = self.list.curselection()

           
        if self.selected_item_index:
            self.selected_item = self.list.get(self.selected_item_index)

            if self.selected_item == "• ZPHISHER":
                self.response = messagebox.askyesno("Question", "Are you on Linux?")
                if self.response:
                    self.response2 = messagebox.askyesno("Question", "Do you have git installed?")
                    if self.response2:
                        self.clone_zphisher_repository()

                    else:
                        self.install_git_and_clone_mhddos_repository()

                else:
                    messagebox.showinfo("Info", "We're sorry, but you need to be on Linux to download Sherlock!")

            elif self.selected_item == "• MAXPHISHER":
                self.response = messagebox.askyesno("Question", "Are you on Linux?")
                if self.response:
                    self.response2 = messagebox.askyesno("Question", "Do you have git installed?")
                    if self.response2:
                        self.clone_maxphisher_repository()

                    else:
                        self.install_git_and_clone_ccattack_repository()

                else:
                    messagebox.showinfo("Info", "We're sorry, but you need to be on Linux to download Maigret!")

            elif self.selected_item == "• CAMPHISHER":
                self.response = messagebox.askyesno("Question", "Are you on Linux?")
                if self.response:
                    self.response2 = messagebox.askyesno("Question", "Do you have git installed?")
                    if self.response2:
                        self.clone_camphisher_repository()

                    else:
                        self.install_git_and_clone_ddosripper_repository()

        else:
            messagebox.showerror("Error", "Please select a tool first!")


    def clone_sherlock_repository(self):
        try:
            subprocess.run(["git", "clone", "https://github.com/sherlock-project/sherlock.git"], check=True)
            self.sherlock_instructions()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to clone Sherlock repository/or it already exists!")
        except FileExistsError:
            messagebox.showerror("Error", "Sherlock repo already exists!")

    def clone_maigret_repository(self):
        try:
            subprocess.run(["git", "clone", "https://github.com/soxoj/maigret.git"], check=True)
            self.maigret_instructions()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to clone Maigret repository/or it already exists!")
        except FileExistsError:
            messagebox.showerror("Error", "Maigret repo already exists!")

    def clone_harvester_repository(self):
        try:
            subprocess.run(["git", "clone", "https://github.com/laramies/theHarvester.git"], check=True)
            self.harvester_instructions()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to clone Harvester repository/or it already exists!")
        except FileExistsError:
            messagebox.showerror("Error", "Harvester repo already exists!")

    def clone_mhddos_repository(self):
        try:
            subprocess.run(["git", "clone", "https://github.com/MatrixTM/MHDDoS"], check=True)
            self.mhddos_instructions()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to clone MHDDoS repository/or it already exists!")
        except FileExistsError:
            messagebox.showerror("Error", "MHDDoS repo already exists!")

    def clone_ccattack_repository(self):
        try:
            subprocess.run(["git", "clone", "https://github.com/Leeon123/CC-attack"], check=True)
            self.ccattack_instructions()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to clone CC-attack repository/or it already exists!")
        except FileExistsError:
            messagebox.showerror("Error", "CC-attack repo already exists!")

    def clone_ddosripper_repository(self):
        try:
            subprocess.run(["git", "clone", "https://github.com/palahsu/DDoS-Ripper"], check=True)
            self.ddosripper_instructions()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to clone DDoS Ripper repository/or it already exists!")
        except FileExistsError:
            messagebox.showerror("Error", "DDoS Ripper repo already exists!")

    def clone_zphisher_repository(self):
        try:
            subprocess.run(["git", "clone", "--depth=1", "https://github.com/htr-tech/zphisher.git"], check=True)
            self.zphisher_instructions()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to clone ZPhisher repository/or it already exists!")
        except FileExistsError:
            messagebox.showerror("Error", "ZPhisher repo already exists!")

    def clone_maxphisher_repository(self):
        try:
            subprocess.run(["git", "clone", "https://github.com/KasRoudra/MaxPhisher"], check=True)
            self.maxphisher_instructions()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to clone MaxPhisher repository/or it already exists!")
        except FileExistsError:
            messagebox.showerror("Error", "MaxPhisher repo already exists!")

    def clone_camphisher_repository(self):
        try:
            subprocess.run(["git", "clone", "https://github.com/techchipnet/CamPhish"], check=True)
            self.camphisher_instructions()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to clone CamPhisher repository/or it already exists!")
        except FileExistsError:
            messagebox.showerror("Error", "Camphisher repo already exists!")

    def install_git_and_clone_sherlock_repository(self):
        try:
            messagebox.showinfo("Info", "Enter your user password in the terminal.")
            time.sleep(0.5)
            subprocess.run(["sudo", "apt-get", "install", "git-all"], check=True)
            self.clone_sherlock_repository()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to install Git and clone Sherlock repository")

    def install_git_and_clone_maigret_repository(self):
        try:
            messagebox.showinfo("Info", "Enter your user password in the terminal.")
            time.sleep(0.5)
            subprocess.run(["sudo", "apt-get", "install", "git-all"], check=True)
            self.clone_maigret_repository()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to install Git and clone Maigret repository")

    def install_git_and_clone_harvester_repository(self):
        try:
            messagebox.showinfo("Info", "Enter your user password in the terminal.")
            time.sleep(0.5)
            subprocess.run(["sudo", "apt-get", "install", "git-all"], check=True)
            self.clone_harvester_repository()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to install Git and clone Harvester repository")

    def install_git_and_clone_mhddos_repository(self):
        try:
            messagebox.showinfo("Info", "Enter your user password in the terminal.")
            time.sleep(0.5)
            subprocess.run(["sudo", "apt-get", "install", "git-all"], check=True)
            self.clone_mhddos_repository()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to install Git and clone MHDDoS repository")

    def install_git_and_clone_ccattack_repository(self):
        try:
            messagebox.showinfo("Info", "Enter your user password in the terminal.")
            time.sleep(0.5)
            subprocess.run(["sudo", "apt-get", "install", "git-all"], check=True)
            self.clone_ccattack_repository()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to install Git and clone CC-attack repository")

    def install_git_and_clone_ddosripper_repository(self):
        try:
            messagebox.showinfo("Info", "Enter your user password in the terminal.")
            time.sleep(0.5)
            subprocess.run(["sudo", "apt-get", "install", "git-all"], check=True)
            self.clone_ddosripper_repository()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to install Git and clone DDoS Ripper repository")

    def install_git_and_clone_zphisher_repository(self):
        try:
            messagebox.showinfo("Info", "Enter your user password in the terminal.")
            time.sleep(0.5)
            subprocess.run(["sudo", "apt-get", "install", "git-all"], check=True)
            self.clone_zphisher_repository()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to install Git and clone ZPhisher repository")

    def install_git_and_clone_maxphisher_repository(self):
        try:
            messagebox.showinfo("Info", "Enter your user password in the terminal.")
            time.sleep(0.5)
            subprocess.run(["sudo", "apt-get", "install", "git-all"], check=True)
            self.clone_maxphisher_repository()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to install Git and clone MaxPhisher repository")

    def install_git_and_clone_camphisher_repository(self):
        try:
            messagebox.showinfo("Info", "Enter your user password in the terminal.")
            time.sleep(0.5)
            subprocess.run(["sudo", "apt-get", "install", "git-all"], check=True)
            self.clone_camphisher_repository()
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to install Git and clone CamPhisher repository")

    def sherlock_instructions(self):
        self.response = messagebox.askyesno("Question", "Would you like to see the instructions?")
        if self.response:
            self.show_sherlock_instructions()  

    def maigret_instructions(self):
        self.response = messagebox.askyesno("Question", "Would you like to see the instructions?")
        if self.response:
            self.show_maigret_instructions() 

    def harvester_instructions(self):
        self.response = messagebox.askyesno("Question", "Would you like to see the instructions?")
        if self.response:
            self.show_harvester_instructions()

    def mhddos_instructions(self):
        self.response = messagebox.askyesno("Question", "Would you like to see the instructions?")
        if self.response:
            self.show_mhddos_instructions()

    def ccattack_instructions(self):
        self.response = messagebox.askyesno("Question", "Would you like to see the instructions?")
        if self.response:
            self.show_ccattack_instructions() 

    def ddosripper_instructions(self):
        self.response = messagebox.askyesno("Question", "Would you like to see the instructions?")
        if self.response:
            self.show_ddosripper_instructions() 

    def zphisher_instructions(self):
        self.response = messagebox.askyesno("Question", "Would you like to see the instructions?")
        if self.response:
            self.show_zphisher_instructions() 

    def maxphisher_instructions(self):
        self.response = messagebox.askyesno("Question", "Would you like to see the instructions?")
        if self.response:
            self.show_maxphisher_instructions() 

    def camphisher_instructions(self):
        self.response = messagebox.askyesno("Question", "Would you like to see the instructions?")
        if self.response:
            self.show_camphisher_instructions() 
            
    def show_sherlock_instructions(self):
        instructions_window = Toplevel()
        instructions_window.title("Sherlock Instructions")
        instructions_window.geometry("540x450")
        instructions_window.config(bg='black')

        label = Label(instructions_window, text="Step 1: Change your current working\ndirectory to Sherlock using 'cd sherlock'.\n\nStep 2: Install the requirements using\n'python3 -m pip install -r requirements.txt'.\n\n\nUSAGE:\n\nWrite 'python3 sherlock.py -h'\nto get a list of all commands.", font=('Arial', 15), fg='green', bg='black')
        label.pack(padx=10, pady=10)

        button = Button(instructions_window, text="Exit", font=('Arial', 15), fg='green', bg='black', command=self.exit_window)
        button.pack(padx=10, pady=20)

        instructions_window.mainloop()

    def show_maigret_instructions(self):
        instructions_window = Toplevel()
        instructions_window.title("Maigret Instructions")
        instructions_window.geometry("540x450")
        instructions_window.config(bg='black')

        label = Label(instructions_window, text="Step 1: Change your current working\ndirectory to Maigret using 'cd maigret'.\n\nStep 2: Install the requirements using\n'pip3 install -r requirements.txt'.\n\n\nUSAGE:\n\nWrite 'maigret --help'\nto get a list of all commands.", font=('Arial', 15), fg='green', bg='black')
        label.pack(padx=10, pady=10)

        button = Button(instructions_window, text="Exit", font=('Arial', 15), fg='green', bg='black', command=self.exit_window)
        button.pack(padx=10, pady=20)

        instructions_window.mainloop()

    def show_harvester_instructions(self):
        instructions_window = Toplevel()
        instructions_window.title("Harvester Instructions")
        instructions_window.geometry("540x450")
        instructions_window.config(bg='black')

        label = Label(instructions_window, text="Step 1: Change your current working\ndirectory to Harvester using 'cd theHarvester'.\n\nStep 2: Install the requirements using\n'python3 -m pip install -r requirements/base.txt'.\n\n\nUSAGE:\n\nWrite 'python3 theHarvester -h'\nto get a list of all commands.", font=('Arial', 15), fg='green', bg='black')
        label.pack(padx=10, pady=10)

        button = Button(instructions_window, text="Exit", font=('Arial', 15), fg='green', bg='black', command=self.exit_window)
        button.pack(padx=10, pady=20)

        instructions_window.mainloop()

    def show_mhddos_instructions(self):
        instructions_window = Toplevel()
        instructions_window.title("MHDDoS Instructions")
        instructions_window.geometry("540x450")
        instructions_window.config(bg='black')

        label = Label(instructions_window, text="Step 1: Change your current working\ndirectory to MHDDoS using 'cd MHDDoS'.\n\nStep 2: Install the requirements using\n'pip install -r requirements.txt'.\n\n\nUSAGE:\n\nWrite 'python3 start.py -h'\nto get a list of all commands.", font=('Arial', 15), fg='green', bg='black')
        label.pack(padx=10, pady=10)

        button = Button(instructions_window, text="Exit", font=('Arial', 15), fg='green', bg='black', command=self.exit_window)
        button.pack(padx=10, pady=20)

        instructions_window.mainloop()

    def show_ccattack_instructions(self):
        instructions_window = Toplevel()
        instructions_window.title("CC-attack Instructions")
        instructions_window.geometry("540x450")
        instructions_window.config(bg='black')

        label = Label(instructions_window, text="Step 1: Change your current working\ndirectory to CC-attack using 'cd CC-attack'.\n\nStep 2: Install the requirements using\n'pip3 install requests pysocks'.\n\n\nUSAGE:\n\nWrite 'python3 cc.py -h'\nto get a list of all commands.", font=('Arial', 15), fg='green', bg='black')
        label.pack(padx=10, pady=10)

        button = Button(instructions_window, text="Exit", font=('Arial', 15), fg='green', bg='black', command=self.exit_window)
        button.pack(padx=10, pady=20)

        instructions_window.mainloop()

    def show_ddosripper_instructions(self):
        instructions_window = Toplevel()
        instructions_window.title("DDoS Ripper Instructions")
        instructions_window.geometry("540x450")
        instructions_window.config(bg='black')

        label = Label(instructions_window, text="Step 1: Change your current working\ndirectory to DDos Ripper using 'cd DDoS-Ripper'.\n\n\nUSAGE:\n\nWrite 'python3 DRipper.py -h'\nto get a list of all commands.", font=('Arial', 15), fg='green', bg='black')
        label.pack(padx=10, pady=10)

        button = Button(instructions_window, text="Exit", font=('Arial', 15), fg='green', bg='black', command=self.exit_window)
        button.pack(padx=10, pady=20)

        instructions_window.mainloop()

    def show_zphisher_instructions(self):
        instructions_window = Toplevel()
        instructions_window.title("ZPhisher Instructions")
        instructions_window.geometry("540x450")
        instructions_window.config(bg='black')

        label = Label(instructions_window, text="Step 1: Change your current working\ndirectory to ZPhisher using 'cd zphisher'.\n\n\nUSAGE:\n\nWrite 'bash zphisher.sh'\nto start ZPhisher.", font=('Arial', 15), fg='green', bg='black')
        label.pack(padx=10, pady=10)

        button = Button(instructions_window, text="Exit", font=('Arial', 15), fg='green', bg='black', command=self.exit_window)
        button.pack(padx=10, pady=20)

        instructions_window.mainloop()

    def show_maxphisher_instructions(self):
        instructions_window = Toplevel()
        instructions_window.title("MaxPhisher Instructions")
        instructions_window.geometry("600x650")
        instructions_window.config(bg='black')

        label = Label(instructions_window, text="Step 1: Change your current working\ndirectory to MaxPhisher using 'cd MaxPhisher'.\n\nStep 2: Install the requirements;\nDebian Based distros:\n'sudo apt install git python3 python3-pip php openssh-client -y'\n\nFor Arch based distros:\n'sudo pacman -S git python3 python-pip php openssh --noconfirm'\n\nFor Redhat based distros:\n'sudo dnf install git python3 php openssh -y'\n\nFor Termux:\n'pkg install git python3 python-pip php openssh -y'\n\nTHIS GOES FOR ALL DISTROS:\npip3 install -r files/requirements.txt --break-system-packages\n\nUSAGE:\n\nWrite 'python3 maxphisher.py -h'\nto get a list of all commands.", font=('Arial', 15), fg='green', bg='black')
        label.pack(padx=10, pady=10)

        button = Button(instructions_window, text="Exit", font=('Arial', 15), fg='green', bg='black', command=self.exit_window)
        button.pack(padx=10, pady=20)

        instructions_window.mainloop()

    def show_camphisher_instructions(self):
        instructions_window = Toplevel()
        instructions_window.title("Camphisher Instructions")
        instructions_window.geometry("540x450")
        instructions_window.config(bg='black')

        label = Label(instructions_window, text="Step 1: Change your current working\ndirectory to CamPhisher using 'cd CamPhish'.\n\nStep 2: Install the requirements; Download them using 'apt-get -y install php openssh git wget'\n\n\nUSAGE:\n\nWrite 'bash camphish.sh -h'\nto get a list of all commands.", font=('Arial', 15), fg='green', bg='black')
        label.pack(padx=10, pady=10)

        button = Button(instructions_window, text="Exit", font=('Arial', 15), fg='green', bg='black', command=self.exit_window)
        button.pack(padx=10, pady=20)

        instructions_window.mainloop()

    def exit_window(self):
        self.response = messagebox.askyesno("Question", "Are you sure you want to exit?")
        if self.response:
            exit()

if __name__ == "__main__":
    Main()
