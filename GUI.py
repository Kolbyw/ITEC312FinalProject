import base64
import tkinter
import json
import urllib.request
from PIL import Image, ImageTk
from api import search  

class GUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("EPL Hub")
        self.main_window.geometry("800x500")

        # Create frames
        self.top_frame = tkinter.Frame(self.main_window, pady=10)
        self.mid_frame = tkinter.Frame(self.main_window, pady=10)
        self.mid_2_frame = tkinter.Frame(self.main_window, pady=10)
        self.bottom_frame = tkinter.Frame(self.main_window, pady=10)

        # Create the widgets for the top frame
        self.team_label = tkinter.Label(self.top_frame,
                              text = 'Enter a team:')
        self.team_entry = tkinter.Entry(self.top_frame, width = 20)
        
        self.search_button = tkinter.Button(self.top_frame,
                                  text = 'Search',
                                  command = self.search)

        # Pack the top frame widgets
        self.team_label.pack(side = 'left', padx=5)
        self.team_entry.pack(side = 'left', padx=5)
        self.search_button.pack(side = 'left', padx=5)
                 
        # Create a blank label for team logo, team info, fixtures, and recent matches
        self.crest_label = tkinter.Label(self.mid_frame, padx=10, pady=5)
        self.teamInfo = tkinter.StringVar()
        self.teamInfo_label = tkinter.Label(self.mid_frame, textvariable= self.teamInfo, padx=10, pady=5)
        
        self.fixtures = tkinter.StringVar()
        self.fixtures_label = tkinter.Label(self.mid_2_frame, textvariable= self.fixtures, padx=10, pady=5)
        
        self.recent = tkinter.StringVar()
        self.recent_label = tkinter.Label(self.mid_2_frame, textvariable= self.recent, padx=10, pady=5)
        

        # Pack the middle frame widgets
        self.crest_label.pack(side = 'left', padx='5')
        self.teamInfo_label.pack(side = 'left', padx='5')
        self.fixtures_label.pack(side = 'left', padx='5')
        self.recent_label.pack(side = 'left', padx='5')
                                                           
        # Create the two buttons in the bottom frame
        self.quit_button = tkinter.Button(self.bottom_frame,
                            text = 'Quit',
                            command = self.main_window.destroy)

        # Pack the widgets in the bottom frame
        self.quit_button.pack(padx=5)
               
        # Pack the frames
        self.top_frame.pack(expand=True)
        self.mid_frame.pack(expand=True)
        self.mid_2_frame.pack(expand=True)
        self.bottom_frame.pack(expand=True)

        # Enter the tkinter main loop
        tkinter.mainloop()

    # Define the show_info function
    def search(self):
        # call the search method from /api.py
        response = search(self.team_entry.get())
        
        # Error handling for team not found
        if not response:
            print("Team name not in list. Please try again.")
        else:
            # get the three seperate responses 
            teamInfo = response[0]
            schedule = response[1]
            recentGames = response[2]

            # parse the data and organize it for user
            info = (
                f"Team Information:\n\n"
                f"Name: {teamInfo['name']}\n"
                f"Coach: {teamInfo['coach']['name']}\n"
                f"Stadium: {teamInfo['venue']}\n"
                f"Founded: {teamInfo['founded']}\n"
                f"Colors: {teamInfo['clubColors']}"
            )
            
            # Load and display team logo
            try:
                logo_path = f"./TeamCrests/{teamInfo['id']}.png" 
                img = Image.open(logo_path)

                # Resize the image 
                img.thumbnail((150, 150))
                logo_image = ImageTk.PhotoImage(img)
                self.crest_label.image = logo_image 
                self.crest_label.config(image=logo_image)
            except Exception as e:
                self.crest_label.config(image="")
                print(f"Error loading logo: {e}")
            
            # set all the information to the labels and add a border around the info
            self.teamInfo.set(info)
            self.teamInfo_label.config(borderwidth=1, relief="solid")
            
            self.fixtures.set(schedule)
            self.fixtures_label.config(borderwidth=1, relief="solid")
            
            self.recent.set(recentGames)
            self.recent_label.config(borderwidth=1, relief="solid")
                
       
# Create an instance of teamGUI
if __name__ == '__main__':
    team = GUI()