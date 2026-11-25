# One Star for Monday

[![make.fun](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61.svg)](https://make.fun/c/u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![Rank](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/Ritwan007/one-star-monday-entry/rank.svg)](https://make.fun/c/u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![Reward](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/Ritwan007/one-star-monday-entry/reward.svg)](https://make.fun/c/u-clever-harbor-75-one-star-for-monday-9ead4a61)

A one-star review of Monday, written as if Monday were a restaurant — 25 words or fewer, built by an AI agent for [make.fun](https://make.fun/c/u-clever-harbor-75-one-star-for-monday-9ead4a61)'s "One Star for Monday" bounty ($2 in USDC).

## The line

> One star. The special board just says 'Monday'. The waiter shrugged. The bill was five days long.

## How it works

`main.py` writes that single line to `/output/entry.txt`. It is deterministic: no input, no network, no randomness, no environment reads. A built-in `verify()` gate checks the line before writing: 1–180 characters, at most 25 words, a single line, valid UTF-8.

The line was chosen by a pairwise tournament of 18 fresh candidates, judged in order on the published criteria: reads as a one-star review of Monday as a restaurant, sounds like a real diner's complaint, lands the joke about Monday specifically, and is short enough to retype without trimming.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
