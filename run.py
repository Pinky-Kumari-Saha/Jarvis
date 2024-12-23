# import multiprocessing

# # def startJarvis():
# #     try:
# #         print("Process 1 is running.")
# #         from main import start
# #         start()
# #     except Exception as e:
# #         print(f"Error in startJarvis: {e}")
        
# # def listenHotword():
# #     try:
# #         print("Process 2 is running.")  
# #         from engine.features import hotword
# #         hotword()
# #     except Exception as e:
# #         print(f"Error in listenHotword: {e}")

# # if __name__ == '__main__':
# #     p1 = multiprocessing.Process(target=startJarvis)
# #     p2 = multiprocessing.Process(target=listenHotword)

# #     try:
# #         p1.start()
# #         p2.start()
# #         p1.join()

# #         if p2.is_alive():
# #             print("Terminating Process 2.")
# #             p2.terminate()
# #             p2.join()
# #     except KeyboardInterrupt:
# #         print("Keyboard interrupt received, stopping processes.")
# #         p1.terminate()
# #         p2.terminate()
# #     finally:
# #         print("System stop")






# # import multiprocessing

# # to run jarvis
# def startJarvis():
    
#     print("Process 1 is running.")
#     from main import start
#     start()
# # to run hotword

# def listenHotword():
    
#     print("Process 2 is running.")  
#     from engine.features import hotword
#     hotword() 
    
    
# # start both process
# if __name__ =='__main__':
#     p1 = multiprocessing.Process(target=startJarvis)
#     p2 = multiprocessing.Process(target=listenHotword)
    
            
#     p1.start()
#     p2.start()
#     p1.join()
                
#     if p2.is_alive():
#         p2.terminate()
#         p2.join()
                        
#     print("system stop")      