# Audio Processing Pipeline – Projet d’une journée

Par **Arailym Pernebay** • **Chaimae Mehdaoui** • **Jawad Berrhili**

## Présentation du projet

Ce projet a été réalisé dans le cadre d’un **brief d’une journée**.  
L’objectif : **construire un pipeline simple et reproductible de traitement audio**, configurable grâce à un fichier YAML.  
Le pipeline charge un ou plusieurs fichiers audio, applique une série d’effets (définis dans le YAML) puis génère une version augmentée de ces fichiers dans plusieurs formats (WAV, MP3, etc.).  
Le rendu final est **simple, pédagogique, modulaire**, et facilement réutilisable.

## Objectifs pédagogiques

- Construire un pipeline de données audio
- Utiliser un fichier YAML pour configurer les transformations
- Appliquer plusieurs effets audio
- Générer des fichiers audio augmentés
- Garantir la reproductibilité du traitement
- Travailler efficacement en équipe (groupe de 3)

## Technologies utilisées
- Python
- pydub
- PyYAML
- ffmpeg (nécessaire pour la lecture/écriture MP3)
- Git & GitHub

## Structure du projet

```bash
audio-pipeline/
│
├── config.yaml            # Configuration du pipeline
├── audio_pipeline.py      # Script principal (pipeline)
│
├── data/
│   ├── input/             # Fichiers audio originaux
│   └── output/            # Fichiers audio générés (wav + mp3)
│
└── README.md
```

## Fonctionnement du pipeline
Le pipeline exécute les étapes suivantes :
1. Lecture du fichier `config.yaml`
2. Chargement des fichiers audio depuis `data/input`
3. Application des effets dans l’ordre défini dans le YAML :
- Bandpass → filtrage des fréquences (effet radio / téléphone)
- Mixnoise → ajout de bruit blanc contrôlé
- Pitchshift → voix plus aiguë ou plus grave
4. Génération de nouvelles versions audio dans les formats choisis (`wav`, `mp3`, etc.)


## Description des effets
1. Bandpass (passe-bande)
Filtre les graves et les aigus pour ne garder qu’une plage de fréquences.
Effet typique "radio" ou "téléphone".

2. Mixnoise
Ajoute un bruit blanc (“sssshhhhh”), contrôlé par snr_db.
- `snr_db` faible = bruit fort
- `snr_db` élevé = bruit léger

3. Pitchshift
Modifie la hauteur du son sans changer la durée.
- positif → voix plus aiguë
- négatif → voix plus grave
- très audible et parfait pour une démonstration.

## Utilisation du pipeline
1. Installer les dépendances

```bash
pip install pydub pyyaml
```

2. Ajouter les fichiers audio originaux dans :

```bash
data/input/
```

3. Configurer les effets dans `config.yaml`

4. Lancer le pipeline

```bash
python audio_pipeline.py
```

5. Récupérer les fichiers générés dans :

```bash
data/output/
```
Les fichiers seront créés en fonction des formats spécifiés dans `output_formats`.

## Équipe

Ce projet a été réalisé par :
- Arailym Pernebay
- Chaimae Mehdaoui
- Jawad Berrhili
Travail collaboratif accompli dans un délai très court, avec une répartition claire, une bonne communication, et une volonté de produire un pipeline simple, propre et efficace.

## Conclusion

Ce projet remplit parfaitement les objectifs du brief :
- pipeline configurable via YAML
- effets audio enchaînés
- export multi-formats
- code simple, clair et reproductible
- travail d’équipe structuré et efficace

Il constitue une base solide pour tout futur projet de traitement ou d’enrichissement audio.
