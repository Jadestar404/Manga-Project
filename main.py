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
    def __init__(self,name):
        self.name=name
        self.collection=[]
    def addition(self,vol):
        for i in self.collection:
            if i.local_id==vol.local_id:
                print("This i a previously existing book.")
                return
        self.collection.append(vol)
        print(f"Added to {self.name} :{vol.title}")
    def __str__(self):
        x=f"\n___ {self.name} ___"
        if not self.collection:
           x+= "  (empty)"
        for vol in self.collection:
           x+="  \n"+str(vol)
        return x
    def research(self,x):
        for i in self.collection:
            if x==i.local_id:
                print(i)
                return
        print("This is an unregistered Local_id.")
    def modify(self,id,t,m):
        for i in self.collection:
            if id==i.local_id:
                i.title=t
                i.mangaka=m
                print("it has been modfier.")
                return
        print("This is an unregistered Local_id.")
    def remove(self,x):
        for i in self.collection:
            if x==i.local_id:
                self.collection.remove(i)
                print("Done to delete.")
                return
        print("This is an unregistered Local_id.")
Manga=Library("Manga")
Manhua=Library("Manhua")
Manhwa=Library("Manhwa")
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
        title=input("Title: ").strip()
        mangaka=input("mangaka: ").strip()
        local_id=input("local_id: ").strip()
        if title == "" or  mangaka == "" or local_id == "":
            print("Error: you cannot leave fields empty!")
        else:
            lib=library_choice()
            if lib:
                lib.addition(MangaVolume(title,mangaka,local_id))
            else:
                print("Error. Pleas respect the data.")
    elif x=="2":
        print(Manga)
        print(Manhua)
        print(Manhwa)
    elif x=="3":
        local_id=input("local_id: ")
        lib=library_choice()
        if lib:
            lib.research(local_id)
        else:
            print("Error. Pleas respect the data.")
    elif x=="4":
        local_id=input("local_id: ")
        title=input("New Title: ").strip()
        mangaka=input("New mangaka: ").strip()
        if title == "" or  mangaka == "" :
            print("Error: you cannot leave fields empty!")
        else:
            lib=library_choice()
            if lib:
                lib.modify(local_id,title,mangaka)
            else:
                print("Error. Pleas respect the data.")
    elif x=="5":
        local_id=input("local_id: ")
        lib=library_choice()
        if lib:
            lib.remove(local_id)
        else:
            print("Error. Pleas respect the data.")
    elif x=="0":
        print("Goodbye.")
        break
    else:
        print("Error. Pleas respect the data.")




