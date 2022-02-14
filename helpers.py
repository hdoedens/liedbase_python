import re

def validate_line(line):
    
    if get_bijbelboek(line):
        #validaeer bijbeltekst
        if re.search(r"^\d", line):
            if re.fullmatch(r"^(\d?\s)\w+\s?\d+\s?:\s?\d+\s?-\s?\d+$", line):
                return True
        elif re.fullmatch(r"^\w+\s?\d+\s?:\s?\d+\s?-\s?\d+$", line):
            return True
        
    else:
        # valideer lied
        if re.fullmatch(r"^\w+\s?\d+\s?:\s?\d+[,\d+]*$", line):
            return True
    
    print("!!! Regel is niet volgens verwachte formaat: {}".format(line))
    return False

def get_bijbelboek(line):
    # get rid of unwanted spaces
    line = line.strip()

    if re.search("^gen", line.lower()):
        return "Genesis"
    
    if re.search("exod", line.lower()):
        return "Exodus"
    
    if re.search("levi", line.lower()):
        return "Leviticus"
    
    if re.search("nume", line.lower()):
        return "Numeri"
    
    if re.search("deut", line.lower()):
        return "Deuteronomium"
    
    if re.search("jozu", line.lower()):
        return "Jozua"
    
    if re.search("rech", line.lower()):
        return "Rechters"
    
    if re.search("ruth", line.lower()):
        return "Ruth"
    
    if re.search("^1 ?sam.*", line.lower()):
        return "1 Samuël"
    
    if re.search("^2 ?sam.*", line.lower()):
        return "2 Samuël"
    
    if re.search("^1 ?kon.*", line.lower()):
        return "1 Koningen"
    
    if re.search("^2 ?kon.*", line.lower()):
        return "2 Koningen"
    
    if re.search("^1 ?kro.*", line.lower()):
        return "1 Kronieken"
    
    if re.search("^2 ?kro.*", line.lower()):
        return "2 Kronieken"
    
    if re.search("ezra", line.lower()):
        return "Ezra"
    
    if re.search("nehe", line.lower()):
        return "Nehemia"
    
    if re.search("este", line.lower()):
        return "Ester"
    
    if re.search("job", line.lower()):
        return "Job"
    
    if re.search("psalmen", line.lower()):
        return "Psalmen"
    
    if re.search("spre", line.lower()):
        return "Spreuken"
    
    if re.search("pred", line.lower()):
        return "Prediker"
    
    if re.search("hoog", line.lower()):
        return "Hooglied"
    
    if re.search("jesa", line.lower()):
        return "Jesaja"
    
    if re.search("jere", line.lower()):
        return "Jeremia"
    
    if re.search("klaa", line.lower()):
        return "Klaagliederen"
    
    if re.search("ezec", line.lower()):
        return "Ezechiël"
    
    if re.search("dani", line.lower()):
        return "Daniël"
    
    if re.search("hose", line.lower()):
        return "Hosea"
    
    if re.search("joel", line.lower()):
        return "Joël"
    
    if re.search("amos", line.lower()):
        return "Amos"
    
    if re.search("obad", line.lower()):
        return "Obadja"
    
    if re.search("jona", line.lower()):
        return "Jona"
    
    if re.search("mich", line.lower()):
        return "Micha"
    
    if re.search("nahu", line.lower()):
        return "Nahum"
    
    if re.search("haba", line.lower()):
        return "Habakuk"
    
    if re.search("sefa", line.lower()):
        return "Sefanja"
    
    if re.search("hagg", line.lower()):
        return "Haggai"
    
    if re.search("zach", line.lower()):
        return "Zacharia"
    
    if re.search("male", line.lower()):
        return "Maleachi"
    
    if re.search("matt?h?e.*", line.lower()):
        return "Matteüs"
    
    if re.search("marcu", line.lower()):
        return "Marcus"
    
    if re.search("lucas", line.lower()):
        return "Lucas"
    
    if re.search("johan", line.lower()):
        return "Johannes"
    
    if re.search("hande", line.lower()):
        return "Handelingen"
    
    if re.search("romei", line.lower()):
        return "Romeinen"
    
    if re.search("^1 ?kor.*", line.lower()):
        return "1 Korintiërs"
    
    if re.search("^2 ?kor.*", line.lower()):
        return "2 Korintiërs"
    
    if re.search("galat", line.lower()):
        return "Galaten"
    
    if re.search("efezi", line.lower()):
        return "Efeziërs"
    
    if re.search("filip", line.lower()):
        return "Filippenzen"
    
    if re.search("kolos", line.lower()):
        return "Kolossenzen"
    
    if re.search("^1 ?tes.*", line.lower()):
        return "1 Tessalonicenzen"
    
    if re.search("^2 ?tes.*", line.lower()):
        return "2 Tessalonicenzen"
    
    if re.search("^1 ?tim.*", line.lower()):
        return "1 Timoteüs"
    
    if re.search("^2 ?tim.*", line.lower()):
        return "2 Timoteüs"
    
    if re.search("titus", line.lower()):
        return "Titus"
    
    if re.search("filem", line.lower()):
        return "Filemon"
    
    if re.search("hebre", line.lower()):
        return "Hebreeën"
    
    if re.search("jakob", line.lower()):
        return "Jakobus"
    
    if re.search("^1 ?pet.*", line.lower()):
        return "1 Petrus"
    
    if re.search("^2 ?pet.*", line.lower()):
        return "2 Petrus"
    
    if re.search("^1 ?joh.*", line.lower()):
        return "1 Johannes"
    
    if re.search("^2 ?joh.*", line.lower()):
        return "2 Johannes"
    
    if re.search("^3 ?joh.*", line.lower()):
        return "3 Johannes"
    
    if re.search("judas", line.lower()):
        return "Judas"
    
    if re.search("openb", line.lower()):
        return "Openbaring"
    
    # als het eerste deel van 'line' niet met een bijbelboek overeenkomt
    return None

def get_chapter(line):
    parts = line.split(':')
    chapter = parts[0][parts[0].rfind(' '):]
    return chapter.strip()

def get_source(line):
    parts = line.split(':')
    source = parts[0][:parts[0].rfind(' ')]
    return source.replace(' ', '_').lower().strip()
    
def get_van_vers(line):
    parts = line.split(':')
    return parts[1][:parts[1].find('-')].strip()
    
def get_tot_vers(line):
    parts = line.split(':')
    return parts[1][parts[1].find('-')+1:].strip()

def get_text_from_bible(translation, source, chapter, van, tot):

    translation = translation.upper()

    source = source.replace("ë", "e")
    source = source.replace("ï", "i")
    source = source.replace("ü", "u")
    
    lines = []

    chapterFound = False
    startCopy = False
    stopCopy = False

    with open("./bronnen/bijbels/{}/{}.txt".format(translation, source), 'r') as f:
        for line in f.readlines():
            line = line.strip()

            if (re.search("^#{}$".format(chapter), line)):
                chapterFound = True
                continue
            
            # we have the line number on which the book starts
            # continue reading from that line, char by char, until we end up on
            # the right verse
            if(chapterFound):
                
                #regels die beginne met '=' zijn kopteksten (titels) die negeren we nu nog
                if line[0:1] == '=':
                    continue
                
                # check to see if we are reading the next chapter, if so, return the BiblePartFragment List
                if (re.search("^#{}$".format(int(chapter) + 1), line)):
                    break
                
                # deel de regel op in versnummers met de vers tekst er aan vast
                parts = re.findall(r'(\d+)?(\D+)', line)
                # doel
                targetParts = []
                for index, part in parts:
                    # start copieren vanaf hier
                    if index == van:
                        startCopy = True
                        # gecombineerde verzen zien er zo uit '5-6'
                        # filter de '-' er uit
                        if part != '-':
                            targetParts.append(part)
                    elif startCopy and not index == "{}".format(int(tot) + 1):
                        if part != '-':
                            targetParts.append(part)
                    elif index == "{}".format(int(tot) + 1):
                        stopCopy = True
                        break
                        
                # alleen toevoegen als er ook echt iets in staat
                if targetParts:
                    lines.append("".join(targetParts))
                
                if stopCopy:
                    break
                    
    f.close()
    return lines