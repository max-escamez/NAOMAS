# NAOMAS : Nao Messenger

## Principe

Le robot Nao est placé dans un couloir où les gens circulent. Il a pour mission de porter un, ou des
messages à différentes personnes préalablement définies. Il connaît évidemment les visages de ses cibles
et également une liste des connaissances de chacune de ses cibles.
Pour mener à bien sa mission, Nao sondera le visage des gens qui évoluent sur son chemin.
Lorsqu’il reconnaît une de ses cibles ou une de ses connaissances, il l’interpelle,
puis se déplace jusqu’à elle pour lui délivrer le message.

## Fonctionnement

Nao Messenger emploie l'apprentissage et la reconnaissance de visage de Nao ainsi que
la notion de mouvement vers une cible préalablement détectée à l'aide de son tracker.
De plus, le modèle BDI (Beliefs, Desires, Intentions) est utilisé pour modéliser
la gestion des cibles, de leurs connaissances et des messages que Nao doit transmettre.
