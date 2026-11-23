"""Stitch several beats of one scene into a single vertical clip, so the clip tells the whole story.

usage: python tools/stitch.py jobs/<id> --seg 102.6-110.6 --seg 144.9-173.4 ... --title "TEXT" --cam x:y:w:h
       [--layout react|facecam|blur|fill] [--out name] [--toolkit <gtavi-claudecode>/scripts]

Each --seg is cut with the toolkit's cut.py (same captions, title, layout), then the pieces are joined with a
hard cut and re-encoded once (1080x1920, 30 fps, -14 LUFS). Writes jobs/<id>/edits/<out>.mp4 + .json (for check.py).
Pick segments that start and end between sentences; keep the total 7-60 s.
"""
import argparse, json, os, shutil, subprocess, sys, tempfile
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("job"); ap.add_argument("--seg", action="append", required=True)
ap.add_argument("--title", default=""); ap.add_argument("--hook", default="")
ap.add_argument("--cam", default="auto"); ap.add_argument("--layout", default="react")
ap.add_argument("--out", default="story"); ap.add_argument("--pick", default="1")
ap.add_argument("--toolkit", default=os.environ.get("CLIP_TOOLKIT", str(Path.home() / "bodila51/gtavi-claudecode/scripts")))
a = ap.parse_args()
job = Path(a.job); edits = job / "edits"; edits.mkdir(exist_ok=True)
segs = [tuple(map(float, s.split("-"))) for s in a.seg]
tmp = Path(tempfile.mkdtemp(dir=edits)); parts = []
for i, (s, e) in enumerate(segs):
    cmd = [sys.executable, str(Path(a.toolkit) / "cut.py"), str(job), "--pick", a.pick, "--start", str(s), "--end", str(e),
           "--layout", a.layout, "--cam", a.cam]
    if a.title: cmd += ["--title", a.title]
    if a.hook and i == 0: cmd += ["--hook", a.hook]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    p = tmp / f"part{i}.mp4"; shutil.move(edits / f"clip_{a.pick}.mp4", p); parts.append(p)
n = len(parts)
inputs = sum([["-i", str(p)] for p in parts], [])
fc = "".join(f"[{i}:v][{i}:a]" for i in range(n)) + f"concat=n={n}:v=1:a=1[v][a0];[a0]loudnorm=I=-14:TP=-1.5:LRA=11[a]"
out = edits / f"{a.out}.mp4"
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", fc, "-map", "[v]", "-map", "[a]", "-r", "30",
                "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
                "-ar", "48000", "-movflags", "+faststart", str(out)], check=True)
meta = json.loads((edits / f"clip_{a.pick}.json").read_text()) if (edits / f"clip_{a.pick}.json").exists() else {}
meta.update({"file": str(out), "segments": segs, "start": segs[0][0], "end": segs[-1][1],
             "length": round(sum(e - s for s, e in segs), 1), "hook": a.hook or a.title, "title": a.title})
(edits / f"{a.out}.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1))
shutil.rmtree(tmp)
print(out, f"{meta['length']}s from {n} beats")
