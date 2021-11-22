import re

""" 
Bij alle regels met een verwijzing naar een bijbelboek is de aanname dat 
altijd de verzen gespecificeerd worden. Ook al wordt een geheel bijbelboek 
gevraagd.
"""

def get_chapter(line):
    if (line.contains(":")):
        s = StringUtils.substringBefore(line, ":")
        return Integer.parseInt(StringUtils.substringBefore(StringUtils.substringAfterLast(s, " "), ":").trim())
     