
import turtle

wn = turtle.Screen()
wn.title("Translator")
wn.bgcolor("black")
wn.setup(width=800, height=600)


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation +"G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


