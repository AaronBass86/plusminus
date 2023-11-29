import random
import pandas as pd
import openpyxl
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

# Load data from Excel
dfloc = pd.read_excel(r'/USA2009_Transformed.xlsx')
df = dfloc
team_names = sorted(df['Name'].unique().tolist())
state_names = sorted(df['State'].unique().tolist())

# Function to show team data
def show_teams_data():
    # Get selected team names
    team_one_name = team_select_combobox1.get()
    team_two_name = team_select_combobox2.get()

    # Retrieve and display data for team one
    if team_one_name:
        team_one_data = df[df['Name'] == team_one_name].iloc[0]
        team_one_info = (f"{team_one_data['Name']}\n"
                         f"Record: {team_one_data['Record']}\n"
                         f"Rating: {team_one_data['Rating']}\n"
                         f"Goal Differential: {team_one_data['AGD']}\n"
                         f"Schedule Rating: {team_one_data['Schedule']}")
        team_one_label.config(text=team_one_info)
    else:
        team_one_label.config(text="Team 1 not selected")

    # Retrieve and display data for team two
    if team_two_name:
        team_two_data = df[df['Name'] == team_two_name].iloc[0]
        team_two_info = (f"{team_two_data['Name']}\n"
                         f"Record: {team_two_data['Record']}\n"
                         f"Rating: {team_two_data['Rating']}\n"
                         f"Goal Differential: {team_two_data['AGD']}\n"
                         f"Schedule Rating: {team_two_data['Schedule']}")
        team_two_label.config(text=team_two_info)
    else:
        team_two_label.config(text="Team 2 not selected")

def update_team_combobox1(event):
    selected_state = state_select_combobox1.get()
    filtered_teams = sorted(df[df['State'] == selected_state]['Name'].unique().tolist())
    team_select_combobox1.config(values=filtered_teams)

def update_team_combobox2(event):
    selected_state = state_select_combobox2.get()
    filtered_teams = sorted(df[df['State'] == selected_state]['Name'].unique().tolist())
    team_select_combobox2.config(values=filtered_teams)

# Tkinter GUI setup
root = tk.Tk()
root.title("Team Comparison App")
root.geometry("600x800+2000+200")
root.configure(bg='darkblue')

customFont = tkFont.Font(family='Verdana', size=18, weight='bold')
customFont2 = tkFont.Font(family = 'Verdana', size=16)

# Labels for Combobox
label1 = tk.Label(root, text="Select Team", bg='darkblue', fg='white', font=customFont)
label1.pack(fill='x', pady=15)

# Comboboxes for team selection
state_select_combobox1 = ttk.Combobox(root, values=state_names, width=5, font=customFont)
state_select_combobox1.pack(pady=10)
state_select_combobox1.bind('<<ComboboxSelected>>', update_team_combobox1)
team_select_combobox1 = ttk.Combobox(root, values=team_names, width=20, font=customFont)
team_select_combobox1.pack(fill='x', pady=10)
# Labels for Combobox
label2 = tk.Label(root, text="Select Team", bg='darkblue', fg='white', font=customFont)
label2.pack(fill='x', pady=10)
# Comboboxes for team selection
state_select_combobox2 = ttk.Combobox(root, values=state_names, width=5, font=customFont)
state_select_combobox2.pack(pady=10)
state_select_combobox2.bind('<<ComboboxSelected>>', update_team_combobox2)
team_select_combobox2 = ttk.Combobox(root, values=team_names, width=20, font=customFont)
team_select_combobox2.pack(fill='x', pady=10)
# Button to trigger data display
show_data_button = tk.Button(root, text="Get Stats", command=show_teams_data, bg='blue', fg='white', font=customFont)
show_data_button.pack(fill='x', pady=10)

# Labels to display team data
team_one_label = tk.Label(root, text="", bg='darkblue', fg='white', font=customFont2)
#team_one_label.place(x=50, y=300)
team_one_label.pack(fill='x', pady=15)

team_two_label = tk.Label(root, text="", bg='darkblue', fg='white', font=customFont2)
#team_two_label.place(x=50, y=450)
team_two_label.pack(fill='x', pady=15)

root.mainloop()







