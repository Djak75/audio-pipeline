import yaml
from pathlib import Path
from pydub import AudioSegment


def load_config(path):
    """
    Charge le fichier YAML et renvoie un dictionnaire Python.
    """
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_audio(file_path: Path):
    """
    Charge un fichier audio avec pydub et le renvoie.
    """
    return AudioSegment.from_file(file_path)


def apply_bandpass(audio, low_cutoff, high_cutoff):
    """
    Applique un effet passe-bande simple : on utilise un filtre passe-haut suivi d'un filtre passe-bas.
    """
    audio = audio.high_pass_filter(low_cutoff)
    audio = audio.low_pass_filter(high_cutoff)
    return audio


def main():
    # On charge la configuration
    config = load_config("config.yaml")

    input_dir = Path(config["input_dir"])
    output_dir = Path(config["output_dir"])
    files = config["files"]
    pipeline = config["pipeline"]  # On récupère la liste des effets

    output_dir.mkdir(parents=True, exist_ok=True)

    # On charge chaque fichier audio
    for filename in files:
        audio_path = input_dir / filename
        print(f"[INFO] Chargement de : {audio_path}")

        audio = load_audio(audio_path)

        # Informations sur la durée de l'audio
        print(f" - Durée (ms) : {len(audio)}")

        # On applique les effets du pipeline, un par un
        for step in pipeline:
            if step["name"] == "bandpass":
                low = step.get("low_cutoff", 1000)
                high = step.get("high_cutoff", 4000)
                audio = apply_bandpass(audio, low, high)

        # On exporte le fichier final
        output_file = output_dir / f"{audio_path.stem}_augmented.wav"
        audio.export(output_file, format="wav")

        print(f" -> Fichier généré dans : {output_file}")


if __name__ == "__main__":
    main()
