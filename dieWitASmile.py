import sys
import time 
def print_lyrics():
    line = [
        "So i'ma love you every last night",
        "like it's the last night",
        "if the world was ending",
        "I'd wanna be next to you",
        "if the party was over",
        "and our time of earth was through",
        "I'd wanna hold you just for a while",
        "And die with a smile",
        "If the world was ending",
        "I'd wanna be next to you",
        "right next to you",
    ]

    delays = [0.6,0.6,1.0,2.6,1.0,2.6,1.7,2.0,0.9,1.2,0.5]
    for i,line in enumerate(lines):
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.1)
            time.sleep(delays[i])
            print()
            print_lyrics()
