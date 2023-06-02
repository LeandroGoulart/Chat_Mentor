import pyttsx3

def listar_vozes():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    print("Vozes disponíveis:")
    for index, voice in enumerate(voices):
        print(f"{index+1}. ID: {voice.id}")
        print(f"   Name: {voice.name}")
        print(f"   Languages: {voice.languages}")
        print(f"   Gender: {voice.gender}")
        print()

def selecionar_voz_masculina():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    vozes_masculinas = []
    for voice in voices:
        if voice.gender == "male" or "masculine" in voice.name.lower():
            vozes_masculinas.append(voice)

    if not vozes_masculinas:
        print("Nenhuma voz masculina encontrada.")
        return None

    print("Vozes masculinas disponíveis:")
    for index, voz in enumerate(vozes_masculinas):
        print(f"{index+1}. ID: {voz.id}")
        print(f"   Name: {voz.name}")
        print(f"   Languages: {voz.languages}")
        print()

    while True:
        try:
            indice_voz = int(input("Digite o índice da voz masculina desejada: "))
            if 1 <= indice_voz <= len(vozes_masculinas):
                return vozes_masculinas[indice_voz - 1]
            else:
                print("Índice inválido. Tente novamente.")
        except ValueError:
            print("Valor inválido. Tente novamente.")

def falar(texto):
    voz_masculina = selecionar_voz_masculina()
    if voz_masculina is None:
        return

    engine = pyttsx3.init()
    engine.setProperty('voice', voz_masculina.id)
    engine.say(texto)
    engine.runAndWait()

if __name__ == "__main__":
    listar_vozes()
    texto = input("Digite o texto a ser falado: ")
    falar(texto)
