#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import re

# Lesson 11.1: Regular Expressions

# Example
x="Paco <paco.garcia@alugandia.es> para: Departamento Técnico <tecnico@alugandia.es> carpeta: tecnico@alugandia.es POP3/Bandeja de entrada fecha: Tue, 28 Feb 2017 17:19:19 +0100 user-agent: Type for Android asunto: Fwd: PRESUPUESTO REF. ANATOLY un adjunto: PRESUPUESTO REF. ANATOLY.pdf (48,0 KB)"
# print x
y = re.findall('@([^ ]*)',x)
print y

# search returns True or False, depending if it finds the string or not.
# if re.search('para:',x) :
#     print "Match Found"


# Lesson 11.2: Extracting Data

y2 = re.findall('.+:',x)
print y2
