import pyfzf
import pydantic
from pathlib import Path
import os
import yaml
from rich import print


class Config(pydantic.BaseModel):
    fps: list[Path]


CONFIG_FP = Path(os.environ["HOME"]) / ".config/kb_cli.yaml"
if not CONFIG_FP.exists():
    CONFIG_FP.write_text("fps: []")
with open(CONFIG_FP, "r") as f:
    CONFIG = Config.model_validate(yaml.load(f, Loader=yaml.FullLoader))


def app():
    kb = {}
    for fp in CONFIG.fps:
        with open(fp, "r") as f:
            kb.update(yaml.load(f, Loader=yaml.FullLoader))
    if not kb:
        print("No knowledge base found")
        return

    fzf = pyfzf.FzfPrompt()
    choice = fzf.prompt(kb.keys())
    if len(choice) == 0:
        print("No choice made")
        return
    result = kb[choice[0]]
    print("-" * 20)
    print("choice:", choice[0])
    print("-" * 20)
    print(result)


if __name__ == "__main__":
    app()
