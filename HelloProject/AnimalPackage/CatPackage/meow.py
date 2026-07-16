def speak_direct():
    print("meow direct ")

def speak_imported():
    print("meow imported")

if __name__ == '__main__': #ne olursa olsun tanımlamasak bile bu kodu çalıştırır
    speak_direct()
else:
    speak_imported()
