Simple stupid webservice around `winsound.beep`.

```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```
server:
```
$ FLASK_APP=beeper/server.py flask run -p 8339 -h 0.0.0.0
```
client:
```
$ ./beeper/client.py --server localhost:1337 --cnt 3
```

stupid usage example:
```bash
function bm {
  ~/bin/wait-for-jenkins $1
  (cd ~/git/beeper && . venv/bin/activate && python3 beeper/client.py --server 192.168.1.60:8339 --beeps 500,1000 2000,500)
  exit
}
```
