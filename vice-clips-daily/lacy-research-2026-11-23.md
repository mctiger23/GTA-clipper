# Lacy GTA 6 marathon: funny-moment research (2026-11-23)

Campaign: LACY GTA VI Marathon Pool (Reach), $12,500 pool, 1M approved views needed for a share, caption needs Lacy's name + #LACY. Rules file: rules/lacy.md.
Searched 151 Lacy clips (Nov 17–23) across 5 VODs; downloaded and transcribed 17 moments.

## Cut (all rule-check PASS)

| # | File | Length | Source | On-screen title |
|---|---|---|---|---|
| 1 | media/edits/2026-11-23-lacy/01-lacy-pet-the-dog.mp4 | 30.3 s | VOD 2932194507 @ 2:02:51 | Lacy tried to PET the dog in GTA 6 |
| 2 | media/edits/2026-11-23-lacy/02-lacy-saves-furry.mp4 | 36.6 s | VOD 2935059680 @ 0:39:58 | Lacy SAVED a furry from the GTA 6 cops |
| 3 | media/edits/2026-11-23-lacy/03-lacy-brokie-fridge.mp4 | 22.5 s | VOD 2932194507 @ 1:55:08 | Lacy is a BROKIE in GTA 6 |

Note on #1: Lacy kicks the dog by accident (in-game). It was Lacy's 2nd most-viewed clip (47K), but platforms can limit animal-harm videos. Post it after the other two, or skip it.

## Captions

1. Lacy just wanted to pet the dog in GTA 6 😭 / 🎥 Lacy on Twitch (twitch.tv/lacy) / #LACY #GTA6 #GTAVI
2. Lacy saved a furry from the GTA 6 cops 🦊 / 🎥 Lacy on Twitch (twitch.tv/lacy) / #LACY #GTA6 #GTAVI
3. Lacy opened the fridge in GTA 6 and found beer, a protein shake and water 💀 / 🎥 Lacy on Twitch (twitch.tv/lacy) / #LACY #GTA6 #GTAVI

## Skipped

- Sexual / nudity: "LUCIA" (77K), "OMG / this guy / lacy falls", "wtf" shower bit, "mandy", Lucia shower, strip club ("no more money"), stripper.
- Story spoilers: "I just shot Lucia / RPG" (finale-day precinct mission), "L driver" (cutscene), "crack attack" (cutscene).
- Slur: "lacy saying n word".
- Audio muted by Twitch: "got caught".
- Not GTA: mute-fail moment, Twitter/bisexual-theory talk.

## Backups if you want more

- "I'll restart the whole game for you… you restart it now" (sarcastic reply to chat) VOD 2936518555 @ 1:08:34.

## Full-story versions (stitched, 2026-11-23)

Made with `tools/stitch.py`: the whole scene is skimmed (transcript + a frame every 6 s), the key beats are picked, the dead air between them is cut, and the beats are joined with hard cuts. Captions and title stay the same across beats. All PASS rules/lacy.md.

| File | Length | Beats (seconds in the downloaded window) |
|---|---|---|
| media/edits/2026-11-23-lacy/01-lacy-pet-the-dog-FULL.mp4 | 38.7 s | meets dog 102.6–110.6 · follows, kneels by cop, kick, "what did I do" 144.9–173.4 · "I was just trying to play with the dog" 189.0–191.1 (window = VOD 2932194507 from 2:00:27) |
| media/edits/2026-11-23-lacy/02-lacy-saves-furry-FULL.mp4 | 56.4 s | cops on the fox 74.0–82.5 · "get in… saving my fuzzy ass" 99.5–114.9 · the no-paws law 137.4–147.8 · "so many cops for a furry" 161.3–172.4 · furry crew "they're one of us" 222.7–233.1 (window = VOD 2935059680 from 0:38:20) |
| media/edits/2026-11-23-lacy/03-lacy-brokie-fridge-FULL.mp4 | 32.5 s | "$2,000… brokie", fridge, "starve to death" 52.6–73.8 · the view from the deck 107.0–118.2 (window = VOD 2932194507 from 1:54:17) |

Re-run example:
`CLIP_TOOLKIT=<gtavi-claudecode>/scripts python tools/stitch.py jobs/<id> --cam 0.002:0.002:0.252:0.252 --title "TEXT" --seg 102.6-110.6 --seg 144.9-173.4`
