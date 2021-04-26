import json
import urllib.request
from displayStuff import displayNumber

CYAN = [0,255,255]

class Weather:
    def __init__(self, sense):
        try:
            f = open('token.txt')
        except:
            print('No token found. Please place an OpenWeatherMap API token in token.txt')
        else:
            self.token = f.read().splitlines()[0]
            f.close()
            try:
                f = open('loc.txt')
            except:
                print('No location found. Please place a location in loc.txt')
            else:
                self.loc = f.read().splitlines()[0]
                f.close()
                self.updateWeather(sense)
        
    def get_temperature(self):
        return self.temp
        
    def updateWeather(self, sense):
        #try:
            print('Updating Weather')
            weatherUrl  = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+self.loc+'&appid='+self.token).read()
            weatherData = json.loads(weatherUrl)
        #except:
        #    weatherData = None
        #else:
            #print(weatherData)
            self.iconID = weatherData['weather'][0]['icon']
            #self.iconID = '50n'
            self.icon = sense.load_image('images/'+self.iconID+'.png', redraw=False)
            self.temp = weatherData['main']['temp']-273.15

def calcColour(temp):
    # CYAN      -> Yellow    -> RED
    # 0,255,255 -> 255,255,0 -> 255,0,0
    # 512 iterations
    # 64 variance in temperature
    
    colourCycle = temp# + 10
    colourCycle = colourCycle * 8
    if colourCycle in range(128):
        colour = [colourCycle*2, 255, 255-colourCycle*2]
    elif colourCycle in range(128,256+128):
        colourCycle -= 128
        colour = [255, 255-colourCycle, 0]
    elif colourCycle < 0:
        colour = [0,255,255]
    else:
        colour = [255,0,0]
    return colour

    
    
    

def drawTemp(pixels, weather):
    temp = round(weather.get_temperature())
    colour = calcColour(temp)
    if temp < 0:
        temp = int(str(temp)[1:])
        pixels[3*8] = colour
    pixels = displayNumber(pixels, temp, [1,1],colour)
    return pixels

def main():
    weather = Weather()
    print(weather.temp)
    print(weather.icon)

if __name__ == '__main__':
    import main
    main.main()
