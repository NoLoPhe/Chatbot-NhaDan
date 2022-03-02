import wikipedia
import webbrowser


def wiki(str):
    try:
        wikipedia.set_lang("vi")
        result = wikipedia.summary(str, sentences=2)
        url = "http://vi.wikipedia.org/w/index.php?title="
        #webbrowser.open_new_tab(url+str)
        return result
    
    except wikipedia.exceptions.PageError:
        url1 = "http://www.google.com/?#q="
        webbrowser.open_new_tab(url1+str)
        return "I did not find any information regarding that query, here the related search results"
        

