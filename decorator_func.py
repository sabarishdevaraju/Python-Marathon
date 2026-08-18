

lang = "sp"

translations = {
       "samosa_buy" : {
         "ta" : "எனக்கு சமோசா வாங்கித் தருவீர்களா?",
         "en" : "can you buy me samosa?",
         "hi" : "क्या आप मेरे लिए समोसा खरीद सकते हैं?",
         "sp" : "¿Me puedes comprar una samosa?"
       }
}





def translate(function):
    global lang
    def wrapper(*args, **kwargs):
        msg = function(*args, **kwargs)
        return translations[msg][lang]
    return wrapper

@translate
def say():
    msg = "samosa_buy"
    return msg

lang = input("Enter the your language? (English=en, Hindi=hi, Spanish=sp, Tamil= ta)\n")
print(say())