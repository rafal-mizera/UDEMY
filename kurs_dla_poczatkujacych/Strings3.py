article = '''Monty Python (also collectively known as the Pythons)[2][3] were a British surreal comedy troupe 
who created the sketch comedy television show Monty Python's Flying Circus, which first aired on the BBC in 1969. 
Forty-five episodes were made over four series. The Python phenomenon developed from the television series into 
something larger in scope and impact, including touring stage shows, films, albums, books and musicals. 
The Pythons' influence on comedy has been compared to the Beatles' influence on music.
[4][5][6] Regarded as an enduring icon of 1970s pop culture, their sketch show has been referred to
 as being “an important moment in the evolution of television comedy".[7]'''

print(article.upper())

print((article.lower().replace("monty","flying")))
print(article.split(" "))
print(f"word python appears {article.lower().count('python')} times ")

print("to print the \\ you need to put \\ twice in your text like this: \\\\")

print('The best hits of \'80s!!!')
print("The best hits of '80s!!!")


# Teraz zrobisz "mini kalkulator" do kantoru wymiany walut.
amountPLN = 234
kursUSD = 3.65
kursEuro = 4.23

print("cur  exchange amount")
print(f"USD   {kursUSD}    {amountPLN/kursUSD}")
print(f"EUR   {kursEuro}     {amountPLN/kursEuro}")

ValueAsText = 123.45
factor = 1.23
print(f"Value is: {ValueAsText} factor is: {factor} value*factor = {float(ValueAsText) * factor}")
