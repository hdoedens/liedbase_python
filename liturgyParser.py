import re


def getLiturgyPartTypeFromLiturgyLine(line):

    regex_psalm = "([pP]salm )"
    regex_gezang = "([gG]ezang(en)?)"
    regex_lied = "([lL]ied([bB]oek)?)"
    regex_opwekking = "([oO]pwekking?)"
    regex_levenslied = "([lL]evenslied?)"
    regex_voorganger = "([vV]oorganger|[dD]ominee|[wW]el[ck]om)"
    regex_video = "([Vv]ideo)"
    regex_schoonmaak = "([Ss]choonmaak)"
    regex_extended_scripture = "bijbeltekst vervolg"
    regex_empty_with_logo = "leeg met logo"
    regex_end_of_morning_service = "(([eE]inde)?.*[mM]orgendienst)"
    regex_end_of_afternoon_service = "(([eE]inde)?.*[mM]iddagdienst)"
    regex_amen = "(([gG]ezongen)?.*[aA]men)"
    regex_votum = "([vV]otum)"
    regex_gebed = "(([gG]ebed)|([bB]idden)|([dD]anken))"
    regex_collecte = "(([cC]|[kK])olle[ck]te)"
    regex_law = "([wW]et)"
    regex_lecture = "([pP]reek)"
    regex_agenda = "([aA]genda)"
    regex = "^[ ]*({}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}|{}).*".format(regex_schoonmaak, regex_extended_scripture, regex_empty_with_logo,
        regex_agenda, regex_end_of_morning_service, regex_end_of_afternoon_service, regex_amen, regex_votum, regex_psalm, regex_gezang, regex_lied, regex_opwekking,
        regex_levenslied, regex_gebed, regex_collecte, regex_voorganger, regex_law, regex_lecture)

    # check liturgy part type
    x = re.search(regex, line)
    if(x == None):
        return 'scripture'

    if re.search(regex_psalm, line):
        return 'song'
    elif re.search(regex_video, line):
        return 'video'
    elif re.search(regex_schoonmaak, line):
        return 'schoonmaak'
    elif re.search(regex_gezang, line):
        return 'song'
    elif re.search(regex_lied, line):
        return 'song'
    elif re.search(regex_opwekking, line):
        return 'song'
    elif re.search(regex_levenslied, line):
        return 'song'
    elif re.search(regex_gebed, line):
        return 'prair'
    elif re.search(regex_collecte, line):
        return 'gathering'
    elif re.search(regex_agenda, line):
        return 'agenda'
    elif re.search(regex_voorganger, line):
        return 'welcome'
    elif re.search(regex_law, line):
        return 'law'
    elif re.search(regex_lecture, line):
        return 'lecture'
    elif re.search(regex_votum, line):
        return 'votum'
    elif re.search(regex_amen, line):
        return 'amen'
    elif re.search(regex_end_of_morning_service, line):
        return 'endOfMorningService'
    elif re.search(regex_end_of_afternoon_service, line):
        return 'endOfAfternoonService'
    elif re.search(regex_extended_scripture, line):
        return 'extendedScripture'
    elif re.search(regex_empty_with_logo, line):
        return 'emptyWithLogo'
    
    # Dit zou nooit voor moeten kunnen komen
    else:
        return 'Onbekend'