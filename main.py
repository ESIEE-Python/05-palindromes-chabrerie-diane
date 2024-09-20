"""exercice palindrome"""
#### Fonction secondaire


def ispalindrome(p):
    """verifie si palindrome"""
    p = p.lower()
    t = [['é','e'], ['è','e'], ['à','a'], ['ù','u'], ['ç','c'], ['ê','e'],
    ['â','a'],['î','i'], ['ï', 'i'], ['ô', 'o'], ['ë', 'e']]
    for couple in t:
        mytable = str.maketrans(couple[0],couple[1])
        p=p.translate(mytable)
    p = p.replace(" ", "")
    p = p.replace(",", "")
    p = p.replace(".", "")
    p = p.replace("'", "")
    p = p.replace("!", "")
    p = p.replace(":", "")
    p = p.replace("?", "")
    p = p.replace("-", "")

    lenth = len(p)
    for i in range(lenth//2):
        if p[i] != p[lenth -i -1]:
            return False
    return True

#### Fonction principale


def main():
    """quelques tests"""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie", "énorme"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
