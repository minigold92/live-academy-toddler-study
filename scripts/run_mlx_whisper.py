#!/usr/bin/env python
import json, sys, time
import mlx_whisper

audio = sys.argv[1]
out_json = sys.argv[2]
out_txt = sys.argv[3]

t0 = time.time()
result = mlx_whisper.transcribe(
    audio,
    path_or_hf_repo="mlx-community/whisper-large-v3-turbo",
    word_timestamps=False,
    verbose=False,
)
elapsed = time.time() - t0

with open(out_json, "w") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

with open(out_txt, "w") as f:
    f.write(f"# mlx-whisper large-v3-turbo | {elapsed:.1f}s | detected={result.get('language')}\n\n")
    for seg in result["segments"]:
        f.write(f"[{seg['start']:7.2f} -> {seg['end']:7.2f}] {seg['text'].strip()}\n")

print(f"DONE in {elapsed:.1f}s, language={result.get('language')}, {len(result['segments'])} segments")
