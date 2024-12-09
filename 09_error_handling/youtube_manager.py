import json

f_name = 'youtube.txt'

def load_data():
    try:
        with open(f_name, 'r') as file:
            test = json.load(file) ## json goto the file then load and convert to json
            print(test)
            print(type(test)) ##type-list of json
            return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open(f_name, 'w') as file:
        json.dump(videos, file) ##json.dump(what, where) helps to add(write) 

def list_all_video(videos):
    for index , value in enumerate(videos,start=1 ):
        pass

def add_video(videos):
    name = input("Enter the video name:")
    time = input("Enter the video time:")
    videos.append({'name':name, 'time':time})
    save_data_helper(videos)

def update_video(videos):
    pass

def delete_video(videos):
    pass

##main entry point:-  
def main():
        videos =  load_data()

        while True:
            print("\nYoutube Manager | Choose an option")
            print("1.List all youtube videos")
            print("2.add a youtube video")
            print("3.Update youtube video details.")
            print("4.Delete a youtube video ")
            print("5.Exit the app")

            choice=input("Enter your choice:")
            print(videos)

            match choice:
                case "1":
                    list_all_video(videos)
                case "2":
                    add_video(videos)
                case "3":
                    update_video(videos)
                case "4":
                    delete_video(videos)
                case "5":
                    break
                case _:
                    print("invalid choice!!")

# main()
if __name__ == "__main__":
    main()                