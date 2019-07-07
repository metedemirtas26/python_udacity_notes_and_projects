# Once, run these codes:
# sudo apt-get update
# sudo apt-get install python-wxgtk-media3.0

#from pygraphics import media
import media
# That library is not working in my computer now, I will write, when I find the solving

toy_story = media.Movie("Toy Story",
                        "A story of..", 
                        "http://upl",
                        "youtubelink..")

print(toy_story.storyline)

avatar = media.Movie("Avatar",
                        "A story of avatar..", 
                        "http://upl",
                        "youtubelink..")

print(avatar.storyline)
avatar.show_trailer()
