#!/usr/bin/env python3
from __future__ import annotations

import argparse
from dataclasses import dataclass

import requests


def parse_args() -> Args:
    p = argparse.ArgumentParser()
    p.add_argument('--server', default='')
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument('--beeps', type=Beep.fromstr, nargs='+')
    g.add_argument('--cnt', type=int)
    p.add_argument('--retries', default=3)
    a = p.parse_args()
    r = Args(a.server, a.beeps, a.retries)
    if not r.beeps:
        r.beeps = [Beep(i*1000, 100) for i in range(1, a.cnt+1)]
    return r


def main() -> None:
    a = parse_args()
    for _ in range(a.retries):
        requests.post(f'http://{a.server}/beep', json={'beeps': [beep_to_json(b) for b in a.beeps]})


@dataclass
class Args:
    server: str
    beeps: list[Beep]
    retries: int

@dataclass
class Beep:
    freq: int
    len: int

    @staticmethod
    def fromstr(s: str) -> Beep:
        return Beep(*[int(x) for x in s.split(',')])


def beep_to_json(b: Beep) -> dict[str, int]:
    return b.__dict__


if __name__ == '__main__':
    main()
