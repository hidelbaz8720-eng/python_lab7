def sauvegarder(notes, fichier):
    with open(fichier, "w", encoding="utf-8") as f:
        for n in notes:
            f.write(str(n) + "\n")
def moyenne(notes):
    """Calcule la moyenne d'une liste de notes (retourne 0 si vide)."""
    if not notes:
        return 0
    return sum(notes) / len(notes)

def appliquer_bonus(notes, bonus=1):
    """Renvoie une nouvelle liste avec un bonus, limité à 20."""
    return [min(note + bonus, 20) for note in notes]

def filtrer_notes(notes, seuil):
    """Conserve uniquement les notes ≥ seuil."""
    return [note for note in notes if note >= seuil]

def min_max(notes):
    if not notes:   
        return None
    return (min(notes), max(notes))

def normaliser(notes, sur=20):
    if not notes:
         return []
    return [(note / sur) * 20 for note in notes]


def rapport(notes, bonus=1, seuil=12, titre="Rapport des notes"):
    """Génère un rapport texte regroupant les infos principales."""
    notes_bonus = appliquer_bonus(notes, bonus)
    notes_valides = filtrer_notes(notes, seuil)

    lignes = [
        f"=== {titre} ===",
        f"Notes originales : {notes}",
        f"le max et le min des notes est :{min_max}",
        f"Notes bonus (+{bonus}) : {notes_bonus}",
        f"Moyenne initiale : {moyenne(notes):.2f}",
        f"Moyenne bonus : {moyenne(notes_bonus):.2f}",
        f"Notes ≥ {seuil} : {notes_valides} (total {len(notes_valides)})"
    ]
    return "\n".join(lignes)




if __name__ == "__main__":
    notes = [12, 9, 15, 8, 17, 13, 19, 10]
    print(rapport(notes))
    print(rapport(notes, bonus=2, seuil=14, titre="Rapport avancé"))
    print(min_max(notes)) 
    print(normaliser([50, 80, 100], sur=100))
    sauvegarder(notes,  "notes.txt")
    