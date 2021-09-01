colors = ["red", "orange", "green", "violet", "blue", "yellow"]

def ColorChooser(color_list,n):
    chosen_colors = color_list[:n]
    return chosen_colors


#
# for color in colors:
#     print(ColorChooser(colors, color))
#

for i in range(1,len(colors)+1):
    print(ColorChooser(colors, i))

################################################################

text = """Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo.
 Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."""

print(text[text.index('(')+1:text.index(')')])


