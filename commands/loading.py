# import time, sys
# def loading():
#     print ("Loading...")
#     for i in range(0, 100):
#         time.sleep(0.1)
#         sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
#         sys.stdout.flush()
#     print
    
# loading()

# import time, sys
# def loading():
#     print ("Loading...")
#     for i in range(0, 100):
#         time.sleep(1)
#         sys.stdout.write(u"\u001b[1000D")
#         sys.stdout.flush()
#         time.sleep(1)
#         sys.stdout.write(str(i + 1) + "%")
#         sys.stdout.flush()
#     print
    
# loading()

import time, sys
def loading():
    print("Loading...")
    for i in range(0, 100):
        time.sleep(0.1)
        width = (i+1) / 4
        length = int(25 - width)
        bar = "[" + "#" * int(width) + " "*length + "]"
        sys.stdout.write(u"\u001b[1000D" +  bar)
        sys.stdout.flush()
    print
    
loading()

# import time, sys, random
# def loading(count):
#     all_progress = [0] * count
#     sys.stdout.write("\n" * count) # Make sure we have space to draw the bars
#     while any(x < 100 for x in all_progress):
#         time.sleep(0.01)
#         # Randomly increment one of our progress values
#         unfinished = [(i, v) for (i, v) in enumerate(all_progress) if v < 100]
#         index, _ = random.choice(unfinished)
#         all_progress[index] += 1
        
#         # Draw the progress bars
#         sys.stdout.write(u"\u001b[1000D") # Move left
#         sys.stdout.write(u"\u001b[" + str(count) + "A") # Move up
#         for progress in all_progress: 
#             width = progress / 4
#             print ("[" + "#" * int(width) + " " * (25 - int(width)) + "]")
        
# loading(4)

