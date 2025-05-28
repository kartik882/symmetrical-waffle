import os

if __name__ == "__main__":
    while True:
        try:
            speech = input("Please type the speech you would like to say: ")
            if speech == "exit":
                break
                """Using Powershell command to say whatever is entered by user in speech"""
                
            os.system(f"powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{speech}')\"")
        except Exception as e:
            print(e)
