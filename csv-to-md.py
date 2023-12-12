import csv
# preface must be edited here for changes to stick
PREFACE = """# attested-conjectures
A Database of Greek and Latin Conjectural Emendations Attested in MSS

<details>
    <summary>Bibliography</summary>
    <h3>Papyri</h3>
    <ul>
        <li>P.Oxy.I,II,IV,V,VI,VII,VIII,X,XI,XIII,LXXXI</li>
        <li>P.Louvre ed. Weil = Austin 42</li>
        <li>P.Münch.II.40 = Pap.graec.mon.89</li>
        <li>Papyrus Massiliensis</li>        
        <li>P.Ryl.54</li>
        <li><em>Berl. klasse Texte</em></li>
        <li>P. Hibeh 24,26</li>
    </ul>
    <h3>Secondary Literature</h3>
    <ul>
        <li>James, Patrick. ‘Review of The Oxyrhynchus Papyri. Volume LXXXI.’ <em>The Classical Review</em> 68, no. 2 (2018): 395-398.</li>
        <li>Kenyon, Frederic George. <em>The Evidence of Greek Papyri with Regard to Textual Criticism.</em> London: Hernry Frowde, 1904.</li>
        <li>Grenfell, B. P. ‘The Value of Papyri for the Textual Criticism of Extant Greek Authors.’ <em>The Journal of Hellenic Studies</em> 39 (1919): 16-36.</li>
    </ul>
</details>

"""

with open("attested-conjectures.csv", "r", encoding="utf8") as conj_csv:
    conj_reader = csv.reader(conj_csv)
    with open("README.md", "w", encoding="utf8") as conj_md: # WARNING: rewrites the file!
        conj_md.write(PREFACE)
        #first line is headers
        first_row = True
        for row in conj_reader:
            new_row = "".join(col + "|" for col in row)[:-1] +"\n" # [:-1] to remove the unneeded | at the end
            conj_md.write(new_row)
            if first_row:
                delimiter_row = "---|" * (len(new_row.split("|")))  
                delimiter_row = delimiter_row[:-1] + "\n" # [:-1] as above
                conj_md.write(delimiter_row)
                first_row = False # delimiter needs to be written after headers (which are the first row)
