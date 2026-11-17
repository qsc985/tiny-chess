# Tiny Chess — the strongest chess engine in 4 KB of Python

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/qsc985/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/qsc985/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in **3,571 bytes** of Python 3.13 (standard library only), entered in make.fun's [`tiny-chess-01` bounty](https://make.fun/bounty/tiny-chess-01).

## The engine

`main.py` is a self-extracting stub: an lzma-compressed payload plus a tiny unpacker. The engine itself is a 0x88 board with:

- negamax + alpha-beta search with a fixed 150,000-node budget per move (~3–5 seconds, under the 10 s limit)
- static exchange evaluation: material + Michniewski piece-square tables + bishop pair
- quiescence search (captures and promotions, all replies when in check)
- transposition table (500k entries), two killer moves, history-heuristic move ordering
- deterministic: Zobrist keys from `random.Random(0)`, no wall clock, no unseeded randomness

## Results

Official 6-game gauntlet (local env): **3.0/6** — 1 win, 4 draws, 1 loss. Estimated Elo **~1270**, well above the 1154 cutoff.

- Beat depth-2, drew depth-3, depth-4, nodes-100k and nodes-250k, lost only to nodes-500k.

## Correctness

- perft: start position 20/400/8902/197281/4865609, Kiwipete and 4 complex positions all match the standard values
- 40 random games vs python-chess: move generation, en passant, castling, make/unmake, incremental Zobrist hash — 0 differences
- Checkmate correct: Qxf7# scores 99999; start position's top move is Nc3

## Run

```sh
python3 main.py
```

The engine reads a position and plays under the harness protocol defined by the competition kit.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
