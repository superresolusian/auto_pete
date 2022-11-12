# Auto Pete

Code for automated team selection for Tuesday night 7v7 football.

_DISCLAIMER: Auto Pete is in no way to replace the real pete and should be used at one's own risk.
auto-pete cannot be held liable for any poor results resulting from its match plans._

---
## Web App Installation for Developers

In your preferred code folder, clone the auto_pete Git repo:

```
cd ~/code
git clone https://github.com/superresolusian/auto_pete.git
```

In your preferred venv folder, create and source a new Python virtual environment:

```
cd ~/venv
python3 -m venv ~/venv/auto_pete
source ~/venv/auto_pete/bin/activate
```

Once running the auto_pete venv, install the required Python dependencies:

```
cd ~/code/auto_pete
pip install --upgrade pip
pip install -r requirements.txt
```

Run the Flask web app:

```
cd ~/code/auto_pete
python run.py
```

Load Auto Pete in your browser: [http://localhost:5000/](http://localhost:5000/)

---

## Contributors
Sian Culley
Tom Roberts
Islington Roses
