import pyfzf
from rich import print

kb = {
    "sensitivity": {
        "description": (
            "True positive rate (TPR),\n"
            "recall,\n"
            "sensitivity (SEN),\n"
            "probability of detection, hit rate"
        ),
        "formula": "TP/P = 1 - FNR",
    },
    "specificity": {
        "description": (
            "True negative rate (TNR),\n"
            "specificity (SPC),\n"
        ),
        "formula": "TN/N = 1 - FPR",

    },
}

def app():
    fzf = pyfzf.FzfPrompt()
    choice = fzf.prompt(kb.keys())
    result = kb[choice[0]]
    print("-" * 20)
    print("choice:", choice[0])
    print("-" * 20)
    print("description:", result["description"])
    print("formula:", result["formula"])


if __name__ == "__main__":
    app()
