#!/usr/bin/env python
"""Batch transcribe audio/*.wav with mlx-whisper.
Watches for new files until --target count reached or --once mode."""
import json, os, sys, time, glob, argparse
import mlx_whisper

AUDIO_DIR = "audio"
OUT_DIR = "transcripts/whisper"
MODEL = "mlx-community/whisper-large-v3-turbo"

ap = argparse.ArgumentParser()
ap.add_argument("--target", type=int, default=96)
ap.add_argument("--once", action="store_true")
ap.add_argument("--poll", type=int, default=20)
args = ap.parse_args()

os.makedirs(OUT_DIR, exist_ok=True)
total_start = time.time()
done_count = 0

def is_done(audio):
    base = os.path.splitext(os.path.basename(audio))[0]
    j = os.path.join(OUT_DIR, base + ".json")
    t = os.path.join(OUT_DIR, base + ".txt")
    return os.path.exists(j) and os.path.exists(t)

while True:
    files = sorted(glob.glob(os.path.join(AUDIO_DIR, "*.wav")))
    pending = [f for f in files if not is_done(f)]
    done_on_disk = len(files) - len(pending)
    print(f"[batch] files={len(files)}, done_on_disk={done_on_disk}, pending={len(pending)}", flush=True)

    if not pending:
        if args.once or done_on_disk >= args.target:
            break
        time.sleep(args.poll)
        continue

    for i, audio in enumerate(pending, 1):
        base = os.path.splitext(os.path.basename(audio))[0]
        out_json = os.path.join(OUT_DIR, base + ".json")
        out_txt = os.path.join(OUT_DIR, base + ".txt")
        t0 = time.time()
        try:
            result = mlx_whisper.transcribe(
                audio, path_or_hf_repo=MODEL, word_timestamps=False, verbose=False,
            )
        except Exception as e:
            print(f"[err] {base}: {e}", flush=True)
            continue
        elapsed = time.time() - t0
        with open(out_json, "w") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        with open(out_txt, "w") as f:
            f.write(f"# {base} | mlx-whisper large-v3-turbo | {elapsed:.1f}s | lang={result.get('language')}\n\n")
            for seg in result["segments"]:
                f.write(f"[{seg['start']:7.2f} -> {seg['end']:7.2f}] {seg['text'].strip()}\n")
        done_count += 1
        print(f"[{i}/{len(pending)}] {base}: {elapsed:.1f}s, {len(result['segments'])} seg", flush=True)

    if args.once:
        break

total_elapsed = time.time() - total_start
print(f"\n[batch] DONE. transcribed_this_run={done_count}, total={total_elapsed:.1f}s", flush=True)
