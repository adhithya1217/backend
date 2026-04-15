gesture_map = {
    "A": "Hello",
    "B": "Thank You",
    "C": "Yes",
    "D": "No",
    "E": "Please",
    "F": "Sorry",
    "G": "Good",
    "H": "Help",
    "I": "I",
    "J": "Friend",
    "K": "Love",
    "L": "Learn",
    "M": "Me",
    "N": "Name",
    "O": "Okay",
    "P": "Please Help",
    "Q": "Question",
    "R": "Respect",
    "S": "Stop",
    "T": "Thank You Very Much",
    "U": "Understand",
    "V": "Victory",
    "W": "Welcome",
    "X": "Excuse Me",
    "Y": "You",
    "Z": "Goodbye"
}

def get_text(label):
    return gesture_map.get(label, "Unknown Gesture")