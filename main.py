import os
class MangaVolume:
    def __init__(self,title,mangaka,local_id):
        self.__title=title
        self.__mangaka=mangaka
        self.__local_id=local_id
    @property
    def title(self):
        return self.__title
    @property
    def mangaka(self):
        return self.__mangaka
    @property
    def local_id(self):
        return self.__local_id
    @title.setter
    def title(self,title):
        self.__title=title
    @mangaka.setter
    def mangaka(self,mangaka):
        self.__mangaka=mangaka
    @local_id.setter
    def local_id(self,local_id):
        self.__local_id=local_id
    def __str__(self):
        return f"| title:{self.title} | mangaka:{self.mangaka} | local_id:{self.local_id} "
class Library:
    def __init__(self,name,fileName):
        self.name=name
        self.fileName=fileName
        self.collection=[]
        self.load_data()
    def save_data(self):
        with open(self.fileName,"w",encoding="utf-8") as f:
            for i in self.collection:
                line=f"{i.title}|{i.mangaka}|{i.local_id}\n"
                f.write(line)
    def load_data(self):
        if not os.path.exists(self.fileName):
            return
        with open(self.fileName,"r",encoding="utf-8") as f:
            for line in f:
                try:
                    data=line.strip().split("|")
                    if len(data)==3:
                        vol=MangaVolume(data[0],data[1],data[2])
                        self.collection.append(vol)
                except:
                    continue

    def addition(self,vol):
        for i in self.collection:
            if i.local_id==vol.local_id:
                return False
        self.collection.append(vol)
        self.save_data()
        return True
    def __str__(self):
        x=f"\n___ {self.name} ___"
        if not self.collection:
           x+= "  (empty)"
        for vol in self.collection:
           x+="  \n"+str(vol)
        return x
    def search(self,x):
        for i in self.collection:
            if x==i.local_id:
                return i
        return None
    def modify(self,v):
        for i in self.collection:
            if v.local_id==i.local_id:
                i.title=v.title
                i.mangaka=v.mangaka
                self.save_data()
                return True
        return False
    def remove(self,x):
        for i in self.collection:
            if x==i.local_id:
                self.collection.remove(i)
                self.save_data()
                return True
        return False
        
Manga=Library("Manga","manga.txt")
Manhua=Library("Manhua","manhua.txt")
Manhwa=Library("Manhwa","Manhwa.txt")
def library_choice():
    print("\nSelect Section: 1.Manga | 2.Manhua | 3.Manhwa")
    choice = input("Type: ")
    if choice == "1":
        return Manga
    elif choice == "2":
        return Manhua
    elif choice == "3":
        return Manhwa
    else:
        return None
while True:
    print("""
  __  __                         
 |  \/  | __ _ _ __   __ _  __ _ 
 | |\/| |/ _` | '_ \ / _` |/ _` |
 | |  | | (_| | | | | (_| | (_| |
 |_|  |_|\__,_|_| |_|\__, |\__,_|
                     |___/       
      LIBRARY MANAGER v1.0
""")
    print("\n1. addition")
    print("2. Show")
    print("3. research")
    print("4. Modify")
    print("5. Remove")
    print("0. Exit")
    x=input("Choose: ")
    if x=="1":    
        lib=library_choice()
        if lib:
            title=input("Title: ").strip()
            mangaka=input("mangaka: ").strip()
            local_id=input("local_id: ").strip()
            if title == "" or  mangaka == "" or local_id == "":
                print("Error: you cannot leave fields empty!")
            else:
                vol=MangaVolume(title,mangaka,local_id)
                if lib.addition(vol):
                    print(f"success : Added {title} to library.")
                else:
                    print("Error: A book with this local_id already exists!")
        else:
            print("Error. Please respect the data.")
    elif x=="2":
        print(Manga)
        print(Manhua)
        print(Manhwa)
    elif x=="3":
        lib=library_choice()
        if lib:
            local_id=input("local_id: ")
            vol=lib.search(local_id)
            if vol:
                print(f"found it : \n{vol}")
            else:
                print("No Books found matching this name.")

        else:
            print("Error. Please respect the data.")
    elif x=="4":
        lib=library_choice()
        if lib:
            local_id=input("local_id: ")
            title=input("New Title: ").strip()
            mangaka=input("New mangaka: ").strip()
            if title == "" or  mangaka == "" :
                print("Error: you cannot leave fields empty!")
            else:
                vol=MangaVolume(title,mangaka,local_id)
                if lib.modify(vol):
                    print("Success: Modification done")
                else:
                    print("Error: Modification not done.")
        else:
            print("Error. Please respect the data.")
    elif x=="5":
        lib=library_choice()
        if lib:
            local_id=input("local_id: ")
            if lib.remove(local_id):
                print("Success: Delete done.")
            else:
                print("Error:  Delete not done.")
        else:
            print("Error. Please respect the data.")
    elif x=="0":
        print("Goodbye.")
        break
    else:
        print("Error. Please respect the data.")




