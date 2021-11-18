from __future__ import print_function
from pptx import Presentation
import argparse
import liturgyParser
import re

def parse_args():
    """ Setup the input and output arguments for the script
    Return the parsed input and output files
    """
    parser = argparse.ArgumentParser(description='Analyze powerpoint file structure and create chuch presentation with it')
    parser.add_argument('infile',
                        type=argparse.FileType('r'),
                        help='Powerpoint file to be analyzed')
    parser.add_argument('outfile',
                        type=argparse.FileType('w'),
                        help='Output powerpoint')
    parser.add_argument('liturgieFile',
                        type=argparse.FileType('r'),
                        help='Liturgie invoer bestand')
    parser.add_argument('analyze',
                        type=str,
                        help='"true" voor analyze/"false" voor presentatie genereren')
    return parser.parse_args()

def readInputFile(inputFile):
    f = open(inputFile, 'r')
    # loop over lines to filter empty lines
    for line in f.readlines():
        # remove unwanted spaces and newlines
        line = line.strip()
        if not line:
            continue
        getLiturgyLineContent(line, liturgyParser.getLiturgyPartTypeFromLiturgyLine(line))

def getLiturgyLineContent(line, type):
    print("Slides maken voor: {}".format(line))
    if type == 'song':
        source = line[0:line.find(' ')]
        source_path = "bronnen/liederen/{}.txt".format(source)
        print("Als bron wordt gebruikt: {}".format(source_path))
        # uitgangspunt: verzen worden altijd meegegeven als komma-gescheiden lijst.
        # voorbeeld:
        #   psalm 4: 1
        #   gezang 14: 3, 6
        songNumber = line[line.find(' '):line.find(':')].strip()
        verses = line[line.find(':')+1:].split(',')
        print("Liednummer {} verzen {}".format(songNumber, verses))
        # haal liedtekst op
        f = open(source_path, 'r')
        zoekstring = "^{} {}:".format(source, songNumber)
        liedGevonden = False
        versGevonden = False
        currentVerse = -1
        
        max_num_lines = 4
        curr_num_lines = 0
        
        # gevonden regels opslaan in 2d array
        liederen = {}
        # for verse in verses:
        #     liederen[verse] = []
            
        for regel in f.readlines():
            regel = regel.strip()
            # zoek het juiste lied op
            if(re.search(zoekstring, regel)):
                liedGevonden = True
                continue
            # bij het volgende lied stoppen
            if(re.search("^{} ".format(source), regel)):
                if liedGevonden:
                    break
            if liedGevonden:
                if(regel in verses):
                    currentVerse = regel
                    versGevonden = True
                    liederen[currentVerse] = []
                    curr_num_lines = 0
                    continue
                elif("" == regel):
                    versGevonden = False
                if(versGevonden):
                    if curr_num_lines == max_num_lines:
                        currentVerse = currentVerse + 'a'
                        curr_num_lines = 0
                        # add the new subverse to the dictionary
                        liederen[currentVerse] = []
                    liederen[currentVerse].append(regel)
                    curr_num_lines += 1
        
        maak_lied_slide(liederen)
        
    elif type == 'scripture':
        source = line[0:line.find(' ')]
    else:
        print("Dit type slide wordt (nog) niet ondersteund")
        
def maak_lied_slide(inhoud):
    for liednummer, regels in inhoud.items():
        textslide = prs.slides.add_slide(prs.slide_layouts[0])
        for shape in textslide.placeholders:
            if shape.is_placeholder:
                phf = shape.placeholder_format
                # print("placholder format {} met shapenaam {}".format(phf.idx, shape.name))
                if shape.name == "Text Placeholder 1":
                    try:
                        shape.text = "\n".join(regels)
                    except AttributeError:
                        print("{} has no text attribute".format(phf.type))

def initialize_pptx(input):
    """ Take the input file and analyze the structure.
    The output file contains marked up information to make it easier
    for generating future powerpoint templates.
    """
    global prs
    prs = Presentation(input)

def analyze_presentation(output):
    """ Take the input file and analyze the structure.
    The output file contains marked up information to make it easier
    for generating future powerpoint templates.
    """
    # Each powerpoint file has multiple layouts
    # Loop through them all and  see where the various elements are
    for index, _ in enumerate(prs.slide_layouts):
        slide = prs.slides.add_slide(prs.slide_layouts[index])
        # Not every slide has to have a title
        try:
            title = slide.shapes.title
            title.text = 'Title for Layout {}'.format(index)
        except AttributeError:
            print("No Title for Layout {}".format(index))
        # Go through all the placeholders and identify them by index and type
        for shape in slide.placeholders:
            if shape.is_placeholder:
                phf = shape.placeholder_format
                # Do not overwrite the title which is just a special placeholder
                try:
                    if 'Title' not in shape.text:
                        shape.text = 'Placeholder index:{} type:{}'.format(phf.idx, shape.name)
                except AttributeError:
                    print("{} has no text attribute".format(phf.type))
                print('{} {}'.format(phf.idx, shape.name))
    prs.save(output)

def save_pptx(filename):
    prs.save(filename)

if __name__ == "__main__":
    args = parse_args()
    initialize_pptx(args.infile.name)
    if args.analyze == 'true':
        print("analyseer het template")
        analyze_presentation(args.outfile.name)
    else:
        readInputFile(args.liturgieFile.name)
        save_pptx(args.outfile.name)