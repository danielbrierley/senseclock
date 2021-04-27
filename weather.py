import json
import urllib.request
import urllib.parse
import urllib.error
from displayStuff import displayNumber

CYAN = [0,255,255]



class Weather:
    def __init__(self, sense):
        try:
            f = open('token.txt')
        except:
            print('No token found. Please place an OpenWeatherMap API token in token.txt')
            self.token = ''
        else:
            self.token = f.read().splitlines()[0]
            f.close()
            try:
                f = open('loc.txt')
            except:
                print('No location found. Please place a location in loc.txt')
                self.loc = ''
            else:
                contents = f.read().splitlines()
                #print(contents)
                if len(contents) > 0:
                    self.loc = contents[0]
                else:
                    self.loc = ''
                f.close()
        self.updateWeather(sense)
        
    def get_temperature(self):
        return self.temp
        
    def updateWeather(self, sense):
        try:
            weatherUrl  = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+urllib.parse.quote(self.loc)+'&appid='+self.token).read()
            weatherData = json.loads(weatherUrl)
            self.weatherData = weatherData
        except urllib.error.HTTPError:
            self.code = '0'
            self.iconID = 'q'
            self.icon = sense.load_image('images/'+self.iconID+'.png', redraw=False)
            self.temp = '??'
        else:
            #print(weatherData)
            self.code = weatherData['cod']
            try:
                self.code = weatherData['cod']
                self.iconID = weatherData['weather'][0]['icon']
                #self.iconID = '09d'
                self.icon = sense.load_image('images/'+self.iconID+'.png', redraw=False)
                self.temp = weatherData['main']['temp']-273.15
            except:
                if 'message' in weatherData:
                    print(weatherData['cod']+': '+weatherData['message'])
                else:
                    print(weatherData['cod'])

    def updateLocation(self,loc,sense):
        f = open('loc.txt','w')
        f.write(loc)
        f.close()
        self.loc = loc
        self.updateWeather(sense)

def calcColour(temp):
    # CYAN      -> Yellow    -> RED
    # 0,255,255 -> 255,255,0 -> 255,0,0
    # 512 iterations
    # 64 variance in temperature
    if '?' in str(temp):
        colour = [255,0,255]
    else:
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
    temp = weather.get_temperature()
    if not '?' in str(temp):
        temp = round(temp)
    colour = calcColour(temp)
    if not '?' in str(temp):
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
