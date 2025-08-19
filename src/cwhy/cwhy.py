import argparse
import subprocess
import sys
import time

def main(args: argparse.Namespace) -> None:
    print(f"__LOG__ {time.time()}: Executing user command")
    process = subprocess.run(
        args.command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    print(f"__LOG__ {time.time()}: Finished executing user command")
    if process.returncode == 0:
        return

    stdin = process.stdout

    if args.show_prompt:
        from . import prompts

        print("===================== Prompt =====================")
        print(prompts.explain_prompt(args, stdin))
        print("==================================================")
        sys.exit(0)

    print(process.stdout)
    print("==================================================")
    print(f"CWhy ({args.llm})")
    print("==================================================")

    print(f"__INFO__ {time.time()}: Importing explain")
    from . import explain

    print(f"__INFO__ {time.time()}: Starting explain")
    explain.explain(args, stdin)

    print("==================================================")
    print(f"__LOG__ {time.time()}: Processed reply")
    sys.exit(process.returncode)
