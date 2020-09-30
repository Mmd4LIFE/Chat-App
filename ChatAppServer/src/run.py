

from core.startup import StartUp


def main():
    StartUp().start()




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        SystemExit, print("[-] somebody killed this server")
        
    
