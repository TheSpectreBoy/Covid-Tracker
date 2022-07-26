import requests
import bs4
import tkinter as tk


#defining get_html_data function to collect data from url.
def get_html_data(url):
    data = requests.get(url)
    return data

#defining get_covid_data function to get covid data from given url.
def get_covid_data():
    url = "https://www.worldometers.info/coronavirus/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data = ""

#using 'for' loop for getting all 3 data "CoronaVirus Cases:", "Deaths:", "Recovered:".
    for block in info_div:
        text = block.find("h1", class_=None).get_text()

        count = block.find("span", class_=None).get_text()

        all_data = all_data + text + " " + count + "\n"
    return all_data

#defining Function get_country_data() to get data for specific country.
def get_country_data():
    name = textfield.get()
    url = "https://www.worldometers.info/coronavirus/country/"+name
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data = ""


    for i in range(3):
        text = info_div[i].find("h1", class_ = None).get_text()

        count = info_div[i].find("span", class_ = None).get_text()

        all_data = all_data + text + " " + count + "\n"
        

        mainlabel['text']=all_data




#defining reload function to reload/refresh data
def reload():
    new_data = get_covid_data()
    mainlabel['text']=new_data


get_covid_data()

#using tkinter for UI
root = tk.Tk()
root.geometry("900x700")
root.title("Covid Tracker")
f = ("poppins", 25, "bold")

#importing "covid.png" in UI
banner = tk.PhotoImage(file="covid.png")
bannerlabel = tk.Label(root, image=banner)
bannerlabel.pack()

#creating text field for searching country data
textfield = tk.Entry(root, width = 50)
textfield.pack()


mainlabel = tk.Label(root, text=get_covid_data(), font=f)
mainlabel.pack()


#creating a button to get country data from function get_country_data()
gbtn = tk.Button(root, text="Get Data", font=f, relief='solid', command=get_country_data)
gbtn.pack()

#creating a button to reload from reload function
rbtn = tk.Button(root, text="Reload", font=f, relief='solid', command=reload)
rbtn.pack()

root.mainloop()

