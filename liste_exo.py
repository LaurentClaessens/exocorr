#! /usr/bin/python
# -*- coding: utf8 -*-

###########################################################################
#	This is the program liste_exo.py
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
###########################################################################

# copyright (c) Laurent Claessens, 2010
# email: moky.math@gmail.com

import os, sys
import manip

r"""
This program is intended to be used in coordination with the LaTeX package SystemeCorr.sty

Invoking 
	./liste_exo XXX 1 20
creates the files exoXXX0001.tex up to exoXXX-0020.tex and corrXXX-0001.tex up to corrXXX-0020.tex

The files are pre-filled as follows :

-------------- file exoXXX-0001.tex --------
\begin{exercice}\label{exoXXX0001}

<+ExoXXX-0001+>

\corrref{XXX0001}
\end{exercice}

---------end ----------------

File corrXXX-0001.tex contains 
-------------- file corrXXX-0001.tex --------
\begin{corrige}{XXX-0001}

<+CorrXXX-0001+>

\end{corrige}
---------end ----------------

Notice that XXX is used in order to produce LaTeX's label, thus you have to only use legal LaTeX characters.
As an example, if you want to create a list of exercises about general topology, you may be tempted to invoke
	./liste_exo.py General_topology 1 10
Do not do so because the character «_» is not a legal character in LaTeX's labels. Use instead
	./liste_exo.py GeneralTopology 1 10
or
	./liste_exo.py General-Topology 1 10

Moreover the content of fdl-notice.txt is added at the top of each file. An example file is provided.
YOU SHOULD CHANGE fdf-notice.txt BEFORE USE : PUT YOUR INFORMATIONS.

After creating the files, diplay the lines to be copy-pasted in you LaTeX file and the ones which add all these files in you local git repository.
"""

# Avant d'utiliser ce script, voir si il ne faut pas ajouter une mention de FDL au début des fichiers.
#  Par défaut, il met le fichier fdl-notice.txt.  En cas d'oubli, les lignes suivantes peuvent sauver la vie.
# for f in corrINGE1114-00* ; do (cat fdl-notice.txt $f)>$f.tmp  ;done
# for f in corrINGE1114-00*; do mv $f.tmp $f ;done

notice_fdl = manip.Fichier("fdl-notice.txt").texte()
print notice_fdl

def AjouteZero(n):
	N = str(n)
	a = []
	for i in range(len(N),4): a.append("0")
	a.append(N)
	return "".join(a)

args = sys.argv[1:]
NomGene = args[0]
deb = int(args[1])
fin = int(args[2])

liste_fichier_exo =[]
liste_fichier_corr =[]

for i in range(deb,fin+1) :
	label = NomGene+"-"+AjouteZero(i)
	fCorr = manip.Fichier("corr"+label+".tex")
	fExo = manip.Fichier("exo"+label+".tex")
	liste_fichier_exo.append(fExo)
	liste_fichier_corr.append(fCorr)

	texte = notice_fdl+"\\begin{exercice}\label{exo"+label+"}\n\n<+Exo"+label+"+>\n\n\corrref{"+label+"}\n\end{exercice}"
	fExo.write(texte,"w")

	texte = notice_fdl+"\\begin{corrige}{"+label+"}\n\n<+Corr"+label+"+>\n\n\end{corrige}"
	fCorr.write(texte,"w")

	print "\Exo{"+label+"}"

print "git add ",
for f in liste_fichier_exo :
	print f.basename,
for f in liste_fichier_corr :
	print f.basename,
