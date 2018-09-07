#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import re

# Part 1

# Part 2
# Parentheses
x="Paco <paco.garcia@alugandia.es> para: Departamento Técnico <tecnico@alugandia.es> carpeta: tecnico@alugandia.es POP3/Bandeja de entrada fecha: Tue, 28 Feb 2017 17:19:19 +0100 user-agent: Type for Android asunto: Fwd: PRESUPUESTO REF. ANATOLY un adjunto: PRESUPUESTO REF. ANATOLY.pdf (48,0 KB)"
print x
y = re.findall('@([^ ]*)',x)
print y
