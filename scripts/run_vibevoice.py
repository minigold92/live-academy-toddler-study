#!/usr/bin/env python
"""Run VibeVoice-ASR on a single audio file using MPS."""
import json, sys, time
import torch
import librosa
from vibevoice.modular.modeling_vibevoice_asr import VibeVoiceASRForConditionalGeneration
from vibevoice.processor.vibevoice_asr_processor import VibeVoiceASRProcessor

MODEL = "microsoft/VibeVoice-ASR"
audio_path = sys.argv[1]
out_json = sys.argv[2]
out_txt = sys.argv[3]
hotwords = sys.argv[4] if len(sys.argv) > 4 else None  # comma-separated

device = "mps" if torch.backends.mps.is_available() else "cpu"
dtype = torch.float32  # MPS prefers float32 per official demo

print(f"[load] device={device}, dtype={dtype}, model={MODEL}", flush=True)
t0 = time.time()
processor = VibeVoiceASRProcessor.from_pretrained(
    MODEL, language_model_pretrained_name="Qwen/Qwen2.5-7B"
)
model = VibeVoiceASRForConditionalGeneration.from_pretrained(
    MODEL, dtype=dtype, attn_implementation="sdpa", trust_remote_code=True
).to(device)
model.eval()
print(f"[load] done in {time.time()-t0:.1f}s", flush=True)

# Load audio at 24kHz (VibeVoice uses 24kHz internally per the dataset loader)
audio, sr = librosa.load(audio_path, sr=24000, mono=True)
print(f"[audio] {len(audio)/sr:.1f}s at {sr}Hz", flush=True)

inputs = processor(
    audio=[audio_path],
    sampling_rate=None,
    return_tensors="pt",
    padding=True,
    add_generation_prompt=True,
)
inputs = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in inputs.items()}

gen_cfg = dict(
    max_new_tokens=32768,
    pad_token_id=processor.pad_id,
    eos_token_id=processor.tokenizer.eos_token_id,
    do_sample=False,
    num_beams=1,
)

print(f"[gen] starting...", flush=True)
t0 = time.time()
with torch.no_grad():
    out_ids = model.generate(**inputs, **gen_cfg)
elapsed = time.time() - t0
print(f"[gen] done in {elapsed:.1f}s", flush=True)

input_len = inputs["input_ids"].shape[1]
gen_ids = out_ids[0, input_len:]
eos_pos = (gen_ids == processor.tokenizer.eos_token_id).nonzero(as_tuple=True)[0]
if len(eos_pos) > 0:
    gen_ids = gen_ids[: eos_pos[0] + 1]
text = processor.decode(gen_ids, skip_special_tokens=True)

try:
    segments = processor.post_process_transcription(text)
except Exception as e:
    print(f"[warn] parse failed: {e}", flush=True)
    segments = []

with open(out_json, "w") as f:
    json.dump({"raw": text, "segments": segments, "elapsed": elapsed}, f, ensure_ascii=False, indent=2)

with open(out_txt, "w") as f:
    f.write(f"# VibeVoice-ASR | {elapsed:.1f}s | {len(segments)} segments\n\n")
    if segments:
        for seg in segments:
            f.write(f"[{seg.get('start_time','?')} -> {seg.get('end_time','?')}] "
                    f"S{seg.get('speaker_id','?')}: {seg.get('text','').strip()}\n")
    else:
        f.write("# (parsing failed, raw output below)\n\n")
        f.write(text)

print(f"DONE: {len(segments)} segments, {elapsed:.1f}s", flush=True)
