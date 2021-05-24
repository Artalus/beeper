from __future__ import annotations

import sys
if sys.platform == "win32":
    import winsound
from typing import Any

from flask import Flask, request

def do_beep(freq: int, len: int) -> None:
    if sys.platform == "win32":
        winsound.Beep(freq, len)
    else:
        print(f'beep was {freq},{len}')

app = Flask(__name__)

@app.route('/beep', methods=['POST'])
def beep() -> dict[str, Any]:
    req: dict[str, Any] = request.get_json()
    beeps = req.get('beeps')
    for b in beeps:
        freq = b['freq']
        len = b['len']
        do_beep(freq, len)
    return dict(result='ok')
