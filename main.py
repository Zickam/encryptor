from my_exceptions import *

MAX_CHR = 0x110000

class Master:
    def __init__(self, password: int = None):
        self._password = password

    def setMasterPassword(self, password: int):
        self._password = password

    def getMasterPassword(self) -> int:
        if self._password is None:
            raise PasswordIsNotSet

        return self._password

    def cypher(self, string: str) -> bytearray:
        string_bytes = []
        for symbol in string:
            bytes = ord(symbol)
            string_bytes.append(bytes)

        cyphered_bytes = []

        for byte in string_bytes:
            cyphered_byte = byte ^ self.getMasterPassword()
            cyphered_bytes.append(cyphered_byte)

        return cyphered_bytes

    def decypher(self, bytes: bytearray) -> str:
        decyphered_bytes = []

        for byte in bytes:
            decyphered_byte = byte ^ self.getMasterPassword()
            decyphered_bytes.append(decyphered_byte)
        
        decyphered_string = ""
        for decyphered_byte in decyphered_bytes:
            if 0 <= decyphered_byte < MAX_CHR:
                decyphered_string += chr(decyphered_byte)   
            else:
                decyphered_string += chr(0)

        return decyphered_string


def main():
    password = None
    while not (type(password) is int):
        try:
            password = int(input("Введите пароль для шифрования > "))
        except:
            continue
        
    cypher_master = Master(password)
    
    string = input("Введите текст для шифрования > ")
    cyphered_bytes = cypher_master.cypher(string)


    password = None
    while not (type(password) is int):
        try:
            password = int(input("Введите пароль для ДЕшифрования > "))
        except:
            continue

    decypher_master = Master(password)

    decyphered_string = decypher_master.decypher(cyphered_bytes)
    print("Дешифрованная строка:", decyphered_string)


if __name__ == "__main__":
    main()
    # master = Master()

    # password = 228118371837131738917389719837918378917389173897138971893
    # master.setMasterPassword(password)

    # my_string = "Жопа арслана"
    # print("initial string:", my_string)

    # cyphered_bytes = master.cypher(my_string)
    # print("cyphered string as byte array:", cyphered_bytes)
    # cyphered_string = ""
    # for i in cyphered_bytes:
    #     # cyphered_string += chr(i)
    #     if 0 <= i < 0x110000:
    #         cyphered_string += chr(i)
    #     else:
    #         cyphered_string += chr(0)

    # print("cyphered string as string:", cyphered_string)

    # decyphered_string = master.decypher(cyphered_bytes)
    # with open("decyphered", "w") as file:
    #     file.write(decyphered_string)
    # print("decyphered string:", decyphered_string)
    
