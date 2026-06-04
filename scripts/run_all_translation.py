import json
import pathlib
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT / "scripts"))

# Import translation functions
from translate_ipynb_markdown_zh_tw import translate_notebook, translate_markdown_file

PROGRESS_FILE = ROOT / "scripts" / "translation_progress.json"

def run_cmd(args, cwd=ROOT):
    result = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {' '.join(args)}\nError: {result.stderr}")
    return result.stdout.strip()

def get_targets():
    # Get all .md and .ipynb files from origin/main
    stdout = run_cmd(["git", "ls-tree", "-r", "origin/main", "--name-only"])
    files = stdout.splitlines()
    targets = [f for f in files if f.endswith(".md") or f.endswith(".ipynb")]
    return sorted(targets)

def load_progress():
    if PROGRESS_FILE.exists():
        try:
            return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"completed": [], "failed": {}, "skipped": []}

def save_progress(progress):
    PROGRESS_FILE.write_text(json.dumps(progress, indent=2, ensure_ascii=False), encoding="utf-8")

def main():
    print("Starting translation job...")
    targets = get_targets()
    print(f"Found {len(targets)} total target files in origin/main branch.")
    
    progress = load_progress()
    completed_set = set(progress.get("completed", []))
    skipped_set = set(progress.get("skipped", []))
    failed_dict = progress.get("failed", {})
    
    to_process = [t for f in targets if (t := str(f)) not in completed_set and t not in skipped_set]
    print(f"Already processed: {len(completed_set) + len(skipped_set)} files.")
    print(f"Remaining to process: {len(to_process)} files.")
    
    for idx, rel_path in enumerate(to_process, 1):
        print(f"\n[{idx}/{len(to_process)}] Processing: {rel_path}")
        path = ROOT / rel_path
        
        # 1. Checkout origin/main version of the file
        try:
            run_cmd(["git", "checkout", "origin/main", "--", rel_path])
        except Exception as e:
            print(f"Error checking out {rel_path}: {e}")
            failed_dict[rel_path] = f"checkout_error: {str(e)}"
            progress["failed"] = failed_dict
            save_progress(progress)
            continue
            
        # 2. Translate
        start_time = time.time()
        try:
            if path.suffix == ".ipynb":
                changed = translate_notebook(path)
            elif path.suffix == ".md":
                changed = translate_markdown_file(path)
            else:
                print(f"Unsupported extension for {rel_path}")
                continue
                
            elapsed = time.time() - start_time
            print(f"Translation completed in {elapsed:.2f}s. Changed: {changed}")
            
            # 3. Handle state and git commit
            if changed:
                run_cmd(["git", "add", rel_path])
                # Commit individual translated file to keep a clear log and allow safe resuming
                commit_msg = f"Translate {rel_path} to zh-tw"
                run_cmd(["git", "commit", "-m", commit_msg])
                print(f"Committed: {rel_path}")
                progress["completed"].append(rel_path)
            else:
                # If there were no translation changes (e.g. empty or only protected code blocks)
                progress["skipped"].append(rel_path)
                
            if rel_path in failed_dict:
                del failed_dict[rel_path]
                
        except Exception as e:
            print(f"Exception during translation of {rel_path}: {e}")
            failed_dict[rel_path] = f"translation_error: {str(e)}"
            
        # Save progress after each file
        progress["failed"] = failed_dict
        save_progress(progress)
        
        # A tiny sleep to be polite to the translation API
        time.sleep(0.5)

    print("\nTranslation run completed!")
    print(f"Total Completed: {len(progress['completed'])}")
    print(f"Total Skipped: {len(progress['skipped'])}")
    print(f"Total Failed: {len(progress['failed'])}")

if __name__ == "__main__":
    main()
