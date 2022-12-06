# This program will read the weather code from the weather station of the city searched by the user
# It will then display the weather conditions for that city
# The user can search for another city or quit the program
# Final project -- SDEV140 -- 12/05/2022 -- weatherCode.py

# Import the necessary modules
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox,ttk
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz 
from PIL import ImageTk, Image 

# Create the main window
root = Tk() 
root.title("Weather Application") # Set the title of the window
root.geometry("890x470+300+200") # Set the size of the window
root.configure(bg="#57adff") # Set the background color to blue
root.resizable(False, False) # Prevent the user from resizing the window

# Define the function to get the weather code and time zone along with the city and coordinates
# Function also displays the seven day forecast in seven different cells 
def getWeather():
    city = textField.get()
# Get the coordinates of the city
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
# Get the latitude and longitude of the city
    result = obj.timezone_at(lng = location.longitude, lat = location.latitude)
    timezone.config(text = result)
    long_lat.config(text = f"{round(location.longitude, 4)}°N,{round(location.latitude, 4)}°E")
# Get the time zone of the city
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text = current_time)
# Get the weather of the city using an API
    api_key = "https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=fd04a5fd70c750e643a6ef3400f27431"
    json_data = requests.get(api_key).json()
# Current weather
    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']
# Display conditions
    t.config(text = (temp, "°C"))
    h.config(text = (humidity, "%"))
    p.config(text = (pressure, "hPa"))
    w.config(text = (wind, "m/s"))
    d.config(text = description)

    #first cell that displays the day and night temperatures along with the weather icon
    firstdayimage = json_data['daily'][0]['weather'][0]['icon']
    
    photo1 = ImageTk.PhotoImage(file=f"icons/{firstdayimage}@2x.png")
    firstimage.config(image=photo1)
    firstimage.image = photo1

    tempday1 = json_data['daily'][0]['temp']['day']
    tempnight1 = json_data['daily'][0]['temp']['night']

    day1temp.config(text=f"Day:{tempday1}\n Night: {tempnight1}")

    #second cell that displays the day and night temperatures along with the weather icon
    seconddayimage = json_data['daily'][1]['weather'][0]['icon']

    img=(Image.open(f"icons/{seconddayimage}@2x.png"))
    resized_image = img.resize((30, 30))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image = photo2

    tempday2 = json_data['daily'][1]['temp']['day']
    tempnight2 = json_data['daily'][1]['temp']['night']

    day2temp.config(text=f"Day:{tempday2}\n Night: {tempnight2}")

    #third cell that displays the day and night temperatures along with the weather icon
    thirddayimage = json_data['daily'][2]['weather'][0]['icon']

    img=(Image.open(f"icons/{thirddayimage}@2x.png"))
    resized_image = img.resize((30, 30))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image = photo3

    tempday3 = json_data['daily'][2]['temp']['day']
    tempnight3 = json_data['daily'][2]['temp']['night']

    day3temp.config(text=f"Day:{tempday3}\n Night: {tempnight3}")


    #fourth cell that displays the day and night temperatures along with the weather icon
    fourthdayimage = json_data['daily'][3]['weather'][0]['icon']

    img=(Image.open(f"icons/{fourthdayimage}@2x.png"))
    resized_image = img.resize((30, 30))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image = photo4

    tempday4 = json_data['daily'][3]['temp']['day']
    tempnight4 = json_data['daily'][3]['temp']['night']

    day4temp.config(text=f"Day:{tempday4}\n Night: {tempnight4}")


    #fifth cell that displays the day and night temperatures along with the weather icon
    fifthdayimage = json_data['daily'][4]['weather'][0]['icon']

    img=(Image.open(f"icons/{fifthdayimage}@2x.png"))
    resized_image = img.resize((30, 30))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image = photo5

    tempday5 = json_data['daily'][4]['temp']['day']
    tempnight5 = json_data['daily'][4]['temp']['night']

    day5temp.config(text=f"Day:{tempday5}\n Night: {tempnight5}")


    #sixth cell that displays the day and night temperatures along with the weather icon
    sixthdayimage = json_data['daily'][5]['weather'][0]['icon']

    img=(Image.open(f"icons/{sixthdayimage}@2x.png"))
    resized_image = img.resize((30, 30))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image = photo6

    tempday6 = json_data['daily'][5]['temp']['day']
    tempnight6 = json_data['daily'][5]['temp']['night']

    day6temp.config(text=f"Day:{tempday6}\n Night: {tempnight6}")


    #seventh cell that displays the day and night temperatures along with the weather icon
    seventhdayimage = json_data['daily'][6]['weather'][0]['icon']

    img=(Image.open(f"icons/{seventhdayimage}@2x.png"))
    resized_image = img.resize((30, 30))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image = photo7

    tempday7 = json_data['daily'][6]['temp']['day']
    tempnight7 = json_data['daily'][6]['temp']['night']

    day7temp.config(text=f"Day:{tempday7}\n Night: {tempnight7}")


    #displays the days of the week
    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))



# Create the icon for the window
image_icons = PhotoImage(file="images/logo.png")
# Set the icon for the window
root.iconphoto(False, image_icons) 

# Create the frame for the window
roundBox = PhotoImage(file="images/Rounded Rectangle 1.png")
# Set the frame for the window
Label(root, image=roundBox,bg="#57adff").place(x=30,y=110)


#Labels for the window
# Label for temperature
label_temp = Label(root, text="Temperature", font=("Arial", 11), bg="#203243", fg="white")
label_temp.place(x=50, y=120) # Place the label on the window

# Label for humidity
label_humidity = Label(root, text="Humidity", font=("Arial", 11), bg="#203243", fg="white")
label_humidity.place(x=50, y=140) # Place the label on the window

# Label for pressure 
label_pressure = Label(root, text="Pressure", font=("Arial", 11), bg="#203243", fg="white")
label_pressure.place(x=50, y=160) # Place the label on the window

# Label for wind speed
label_windSpeed = Label(root, text="Wind Speed", font=("Arial", 11), bg="#203243", fg="white")
label_windSpeed.place(x=50, y=180) # Place the label on the window

# Label for description 
label_descript = Label(root, text="Description", font=("Arial", 11), bg="#203243", fg="white")
label_descript.place(x=50, y=200) # Place the label on the window

# Search Box 
searchImage = PhotoImage(file="images/Rounded Rectangle 3.png") # Create the search box with rounded corners
myimage = Label(image=searchImage, bg="#57adff") # set background color to blue
myimage.place(x=270, y=120) # Place the search box on the window

# Create the weather image
weatherImage = PhotoImage(file="images/Layer 7.png") 
weatherImageLabel = Label(root, image=weatherImage, bg="#203243") # Set the background color
weatherImageLabel.place(x=290, y=127) # Place the weather image on the window

# Create the search button
textField = Entry(root, justify="center", width=15, font=("poppins",25,"bold"), bg="#203243", border=0, fg="white") 
textField.place(x=370, y=130) # Place the search button on the window
textField.focus() # Set the focus on the search button

# Create the search icon
searchIcon = PhotoImage(file="images/Layer 6.png") 
SearchIconButton = Button(root, image=searchIcon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather) # create search icon button
SearchIconButton.place(x=645, y=125) # Place the search icon on the window

# Bottom box
frame=Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

# Bottom boxes for the window
firstBox = PhotoImage(file="images/Rounded Rectangle 2.png") # Create the first box with rounded corners
secondBox = PhotoImage(file="images/Rounded Rectangle 2 copy.png") # Create the second box with rounded corners

# Place the first box on the window
Label(frame, image=firstBox, bg="#212120").place(x=30, y=20)
# Place the second box on the window
Label(frame, image=secondBox, bg="#212120").place(x=300, y=30)

# Create the boxes for the labels
Label(frame, image=secondBox, bg="#212120").place(x=400, y=30)
Label(frame, image=secondBox, bg="#212120").place(x=500, y=30)
Label(frame, image=secondBox, bg="#212120").place(x=600, y=30)
Label(frame, image=secondBox, bg="#212120").place(x=700, y=30)
Label(frame, image=secondBox, bg="#212120").place(x=800, y=30)

# Create the clock for the window
clock = Label(root,font=("Helvetica", 30, "bold"), bg="#57adff", fg="white")
clock.place(x=30, y=20) # Place the clock on the window

# Create the timezone for the window
timezone = Label(root,font=("Helvetica", 20), bg="#57adff", fg="white")
timezone.place(x=700, y=20) # Place the timezone on the window

# Create the longitude and latitude for the window
long_lat = Label(root,font=("Helvetica", 10), bg="#57adff", fg="white")
long_lat.place(x=700, y=50)

# code to display weather details associated with labels
# Temperature
t =Label(root, font=("Helvetica", 11), bg="#203243", fg="white")
t.place(x=150, y=120)
# Humidity
h =Label(root, font=("Helvetica", 11), bg="#203243", fg="white")
h.place(x=150, y=140)
# Pressure
p =Label(root, font=("Helvetica", 11), bg="#203243", fg="white")
p.place(x=150, y=160)
# Wind Speed
w =Label(root, font=("Helvetica", 11), bg="#203243", fg="white")
w.place(x=150, y=180)
# Description
d =Label(root, font=("Helvetica", 11), bg="#203243", fg="white")
d.place(x=150, y=200)


# First cell configuration
firstframe = Frame(root, width=230, height=132, bg="#282829")
firstframe.place(x=35, y=315)

day1 = Label(firstframe, font="arial 20", bg="#282829", fg="#fff")
day1.place(x=100, y=5)

firstimage = Label(firstframe, bg="#282829")
firstimage.place(x=1, y=15)

day1temp = Label(firstframe, font="arial 15 bold", bg="#282829", fg="#57adff")
day1temp.place(x=100, y=50)


# Second cell configuration
secondframe = Frame(root, width=70, height=115, bg="#282829")
secondframe.place(x=305, y=325)

day2 = Label(secondframe, bg="#282829", fg="#fff")
day2.place(x=10, y=1)

secondimage = Label(secondframe, bg="#282829")
secondimage.place(x=7, y=20)

day2temp = Label(secondframe, bg="#282829", fg="#fff")
day2temp.place(x=2, y=70)

# Third cell configuration
thirdframe = Frame(root, width=70, height=115, bg="#282829")
thirdframe.place(x=405, y=325)

day3 = Label(thirdframe,  bg="#282829", fg="#fff")
day3.place(x=10, y=1)

thirdimage = Label(thirdframe, bg="#282829")
thirdimage.place(x=7, y=20)

day3temp = Label(thirdframe, bg="#282829", fg="#fff")
day3temp.place(x=2, y=70)

# Fourth cell configuration
fourthframe = Frame(root, width=70, height=115, bg="#282829")
fourthframe.place(x=505, y=325)

day4 = Label(fourthframe, bg="#282829", fg="#fff")
day4.place(x=10, y=1)

fourthimage = Label(fourthframe, bg="#282829")
fourthimage.place(x=7, y=20)

day4temp = Label(fourthframe, bg="#282829", fg="#fff")
day4temp.place(x=2, y=70)

# Fifth cell configuration
fifthframe = Frame(root, width=70, height=115, bg="#282829")
fifthframe.place(x=605, y=325)

day5 = Label(fifthframe, bg="#282829", fg="#fff")
day5.place(x=10, y=1)

fifthimage = Label(fifthframe, bg="#282829")
fifthimage.place(x=7, y=20)

day5temp = Label(fifthframe, bg="#282829", fg="#fff")
day5temp.place(x=2, y=70)

# Sixth cell configuration
sixthframe = Frame(root, width=70, height=115, bg="#282829")
sixthframe.place(x=705, y=325)

day6 = Label(sixthframe, bg="#282829", fg="#fff")
day6.place(x=10, y=1)

sixthimage = Label(sixthframe, bg="#282829")
sixthimage.place(x=7, y=20)

day6temp = Label(sixthframe, bg="#282829", fg="#fff")
day6temp.place(x=2, y=70)

# Seventh cell configuration
seventhframe = Frame(root, width=70, height=115, bg="#282829")
seventhframe.place(x=805, y=325)

day7 = Label(seventhframe, bg="#282829", fg="#fff")
day7.place(x=10, y=1)

seventhimage = Label(seventhframe, bg="#282829")
seventhimage.place(x=7, y=20)

day7temp = Label(seventhframe, bg="#282829", fg="#fff")
day7temp.place(x=2, y=70)


# Days of the week configuration
first = datetime.now()
day1.config(text=first.strftime("%A"))

second = first + timedelta(days=1)
day2.config(text=second.strftime("%A"))

third = first + timedelta(days=2)   
day3.config(text=third.strftime("%A"))

fourth = first + timedelta(days=3)
day4.config(text=fourth.strftime("%A"))

fifth = first + timedelta(days=4)
day5.config(text=fifth.strftime("%A"))

sixth = first + timedelta(days=5)
day6.config(text=sixth.strftime("%A"))

seventh = first + timedelta(days=6)
day7.config(text=seventh.strftime("%A"))


# Start the main loop for the window
root.mainloop()


