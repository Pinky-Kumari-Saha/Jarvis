# import multiprocessing


# def startJarvis():
#         # Code for process 1
#         print("Process 1 is running.")
#         from main import start
#         start()
    
#     # To run hotword
# def listenHotword():
#         # Code for process 2
#         print("Process 2 is running.")
#         from engine.features import hotword
#         hotword()



#     # Start both processes
# if __name__ == '__main__':
#         p1 = multiprocessing.Process(target=startJarvis)
#         p2 = multiprocessing.Process(target=listenHotword)
#         p1.start()
#         p2.start()
#         p1.join()

#         if p2.is_alive():
#             p2.terminate()
#             p2.join()

#         print("system stop")   
# import multiprocessing
import multiprocessing




def startJarvis():
    """Run the Jarvis main process."""
    print("Process 1 is running.")
    from main import start  # Import here to avoid issues with multiprocessing
    start()


def listenHotword():
    """Run the hotword listening process."""
    print("Process 2 is running.")
    from engine.features import hotword  # Import here to avoid issues with multiprocessing
    hotword()


if __name__ == '__main__':
    # Create processes
    p1 = multiprocessing.Process(target=startJarvis, name="JarvisProcess")
    p2 = multiprocessing.Process(target=listenHotword, name="HotwordProcess")

    # Start processes
    p1.start()
    p2.start()

    # Wait for the first process to finish
    p1.join()

    # Check if the second process is still running and terminate if necessary
    if p2.is_alive():
        print("Terminating Process 2...")
        p2.terminate()
        p2.join()

    print("System stop.")
