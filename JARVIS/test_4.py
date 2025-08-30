import os
import pandas as pd
import variables as vr
import random



class MoviePlayer:
    def __init__(self,main_class,query) -> None:
        self.main  = main_class()
        self.all_hollywood_movies = (os.listdir("H:\\Movies\\Hollywood  movies\\New folder")) + (os.listdir("H:\\Movies\\Hollywood  movies\\Super heroes movies\\Dawn of Justice")) + (os.listdir("H:\\Movies\\Hollywood  movies\\Super heroes movies\\marvel movie")) + (os.listdir("H:\\Movies\\Hollywood  movies\\Super heroes movies\\marvel movie\\Ms Marvel"))
        self.all_bollywood_movies = (os.listdir("H:\\Movies\\Bollywood  movies\\Indian\\Simple  Movies")) + (os.listdir("H:\\Movies\\Bollywood  movies\\Indian\\Horor"))
        self.all_punjabi_movies = (os.listdir("H:\\Movies\\Bollywood  movies\\punjabi"))
        self.all_chinese_movies = (os.listdir("H:\\Movies\\Chinese")) + (os.listdir("H:\\Movies\\Chinese\\Squid game"))
        self.all_pakistani_movies =  (os.listdir("H:\\Movies\\pakistani"))
        self.all_movie_list = self.all_hollywood_movies + self.all_bollywood_movies + self.all_punjabi_movies + self.all_pakistani_movies + self.all_chinese_movies
        self.df = pd.read_excel(vr.movie_file_path)
        self.query = query.replace('movie','')
        self.query = self.query.replace('movies','')
        self.query = self.query.replace('play','')
        self.query = self.query.strip()
    
    # for finding movie
    def movie_finder(self,name):
        name = str(name).casefold()
        df = pd.read_excel(vr.movie_file_path)

        writeInd = list()
        movie_list = list()
        movie_name = list()
        if name != "":
            try:
                for index,item in df.iterrows():
                    full_name = (str(item["Name"])).casefold()
                    if full_name == name:
                        movie = str(item["Movie Names"])
                        if movie not in movie_list:
                            movie_list.append(movie)      
                            writeInd.append(index)
                            movie_name.append(str(item["Name"]))
                if(writeInd != []):
                    return   writeInd,movie_list,movie_name 
                for index,item in df.iterrows():
                    search_string = str(item["Search String"]).casefold()  
                    if name in search_string:
                        movie_list.append(str(item["Movie Names"]))      
                        writeInd.append(index)
                name.split()        
                for index,item in df.iterrows():
                    search_string = (str(item["Search String"]).casefold()).split(sep=',')
                    for i in search_string:
                        if i in name:
                            movie = str(item["Movie Names"])
                            if movie not in movie_list:
                                movie_list.append(movie)      
                                writeInd.append(index) 
                for index in range(len(writeInd)):
                    movie_name.append(str(df.loc[(writeInd[index]),"Name"])) 
            except:
                pass                          
        return   writeInd,movie_list,movie_name

    def movie_name_finder(self,movie):
        df = pd.read_excel(vr.movie_file_path)
        name = list()
        for index,item in df.iterrows():
            i = item["Movie Names"]
            if i in movie:
                name.append(df.loc[index,"Name"])
        return name  


    def player(self):
        query = self.query   
        i=0                   
        while(i<1):
            i=1    
            movie_index,movie_list,movie_name = self.movie_finder(query)
            if (len(movie_index) == 1) :
                path = self.df.loc[movie_index[0], "Path"]
                self.main.speak(("Playing movie " + movie_name[0]))
                os.startfile(path + movie_list[0])
                continue 
            elif(movie_index != []):
                self.main.print_list(movie_name)
                self.main.speak("Which movie you want to play.")
                query =  self.main.takeCommand()
                if query == None :
                    continue
                try:
                    choice = (self.main.nsti(query))-1   
                    if choice < len(movie_list):
                        path = self.df.loc[movie_index[choice], "Path"]
                        self.main.speak(("Playing movie " + movie_name[choice]))
                        os.startfile(path + movie_list[choice])
                        continue
                    else:
                        self.main.speak("Option not available.")
                except Exception as e:
                    query = query.replace('movie','')
                    i = 0
                    continue


            elif('random'in query):
                number = random.randrange(0,len(self.all_movie_list))
                path = self.df.loc[number, "Path"]
                random_name = str(self.df.loc[number, "Name"])
                random_fname = str(self.df.loc[number, "Movie Names"])
                self.main.speak(("Playing movie " + random_name))
                os.startfile(path + random_fname)

                                
            elif  (('total'in query) or ("number" in query))  :
                print(f"There are {len(self.all_movie_list)} movies in your computer")
                continue
            elif ('all 'in query) and ('list' in query):
                self.main.print_list(self.all_movie_list)
                self.main.speak("Which movie you want to play.")
                query=  self.main.takeCommand()
                continue
            elif (('hollywood'in query) or ('english'in query)) :
                movie_list = self.all_hollywood_movies
                self.main.print_list(self.movie_name_finder(movie_list))
                self.main.speak("Which movie you want to play.")
                query=  self.main.takeCommand()
                i=0
                continue                           
            elif (('bollywood'in query) or ('hindi'in query) or ('indian'in query)):
                movie_list = self.all_bollywood_movies + self.all_punjabi_movies
                self.main.print_list(self.movie_name_finder(movie_list))
                self.main.speak("Which movie you want to play.")
                query=  self.main.takeCommand()                            
                i=0
                continue
            elif (('punjabi'in query)):
                movie_list = self.all_punjabi_movies
                self.main.print_list(self.movie_name_finder(movie_list))
                self.main.speak("Which movie you want to play.")
                query=  self.main.takeCommand()                            
                i=0
                continue
            elif (('lollywood'in query) or ('pakistani'in query) or ('pakistan'in query)):
                movie_list = self.all_pakistani_movies
                self.main.print_list(self.movie_name_finder(movie_list))
                self.main.speak("Which movie you want to play.")
                query=  self.main.takeCommand()
                i=0
                continue
            elif (('chinese'in query)):
                movie_list = self.all_chinese_movies
                self.main.print_list(self.movie_name_finder(movie_list))
                self.main.speak("Which movie you want to play.")
                query=  self.main.takeCommand()
                i=0
                continue
            elif (('movie' in query) or ('movies'in query)):
                movie_dir = "H:\\Movies"
                movie_folders = os.listdir(movie_dir)
                self.main.print_list(movie_folders)
                self.main.speak("Which movie you want to play.")
                query=  self.main.takeCommand()
                i=0
                continue
            else:
                pass

