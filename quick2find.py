from PyDictionary import PyDictionary
from vosk import Model, KaldiRecognizer
import pyaudio

dictionary = PyDictionary

model = Model(r"C:\Users\jacks\Desktop\Visual Studio Code\Projects\Quick-To-Find\vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def get_word():
    text = None
    word = None
    print("Speak Word: \n")
    while text == None:
        data = stream.read(4096, exception_on_overflow = False)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            word = text[14:-3]
            if(len(word.split()) == 1):
                wordValidate = input(word + "? y/n: ")
        
        if(word != None and not word.isspace() and len(word.split()) == 1 and wordValidate == 'y'):
            get_definition(word)
        else:
            text = None

def get_definition(word):  
    definitions = str(dictionary.meaning(word))[2:-3]
    splitDefs, types = reformat_types(definitions)
    splitDefs.remove(splitDefs[0])

    for i in range(len(splitDefs)):
        if("Noun" in splitDefs[i] or "Verb" in splitDefs[i]): 
            splitDefs[i] = splitDefs[i][8:]                       
        if("Adjective" in splitDefs[i]):
            splitDefs[i] = splitDefs[i][13:]
        if("Adverb" in splitDefs[i]):
            splitDefs[i] = splitDefs[i][9:]

    #print (splitDefs)
    array1 = []
    array2 = []
    array3 = []
    array4 = []

    if(len(types) == 1):
        array1 = splitDefs[0].split(" '")
    elif(len(types) == 2):
        array1 = splitDefs[0].split(" '")
        array2 = splitDefs[1].split(" '")
    elif(len(types) == 3):
        array1 = splitDefs[0].split(" '")
        array2 = splitDefs[1].split(" '")
        array3 = splitDefs[2].split(" '")
    elif(len(types) == 4):
        array1 = splitDefs[0].split(" '")
        array2 = splitDefs[1].split(" '")
        array3 = splitDefs[2].split(" '")
        array4 = splitDefs[3].split(" '")
    
    array1, array2, array3, array4 = remove_apos(array1, array2, array3, array4)
    

    active = True
    while active:
        for i in range(len(array1)):        
            print(f'{word} - {types[0]}')
            print(array1[i])
            nextDef = input("")
            if(nextDef != ""):
                active = False
                break
        if array2 != None:
            for i in range(len(array2)):
                if(nextDef != ""):
                    active = False
                    break
                print(f'{word} - {types[1]}')
                print(array2[i])
                nextDef = input("")            
        if array3 != None:
            for i in range(len(array3)):
                if(nextDef != ""):
                    active = False
                    break
                print(f'{word} - {types[2]}')
                print(array3[i])
                nextDef = input("")              
        if array4 != None:
            for i in range(len(array4)):
                if(nextDef != ""):
                    active = False
                    break
                print(f'{word} - {types[3]}')
                print(array4[i])
                nextDef = input("")                

def reformat_types(definitions):  
    types = []
    if "Noun" in definitions:
        definitions = definitions.replace("Noun", "#Noun")
    if "Adjective" in definitions:
        definitions = definitions.replace("Adjective", "#Adjective")
    if "Verb" in definitions:
        definitions = definitions.replace("Verb", "#Verb")
    if "Adverb" in definitions:
        definitions = definitions.replace("Adverb", "#Adverb")
  
    splitDefs = clean_definitions(definitions)
    types = get_type_array(splitDefs)

    return splitDefs, types

def clean_definitions(definitions):
    definitions = definitions.replace(",", "")
    definitions = definitions.replace("(", "")
    definitions = definitions.replace(")", "")
    definitions = definitions.replace("[", "")
    definitions = definitions.replace("]", "")

    splitDefs = definitions
    splitDefs = splitDefs.split("#")
    return splitDefs

def get_type_array(splitDefs):
    types = []
    for i in range(len(splitDefs)):
        if("Noun" in splitDefs[i]):
            types.append("Noun")
        if("Verb" in splitDefs[i]):
            types.append("Verb")
        if("Adjective" in splitDefs[i]):
            types.append("Adjective")
        if("Adverb" in splitDefs[i]):
            types.append("Adverb")
    return types

def remove_apos(array1, array2, array3, array4):
    for i in range(len(array1)):
        array1[i] = array1[i].replace("'", "")
    for i in range(len(array2)):
        array2[i] = array2[i].replace("'", "")
    for i in range(len(array3)):
        array3[i] = array3[i].replace("'", "")
    for i in range(len(array4)):
        array4[i] = array4[i].replace("'", "")

        array1, array2, array3, array4 = remove_empty_def(array1, array2, array3, array4)
    return array1, array2, array3, array4

def remove_empty_def(array1, array2, array3, array4):
    if(len(array1) > 1):
        array1.pop(len(array1) - 1)
    if(len(array2) > 1):
        array2.pop(len(array2) - 1)
    if(len(array3) > 1):
        array3.pop(len(array3) - 1)
    if(len(array4) > 1):
        array4.pop(len(array4) - 1)
    
    return array1, array2, array3, array4

get_word()


            

            
            
