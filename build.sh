# rm -rf .venv
# uv venv .venv --seed --python 3.10
source .venv/bin/activate
# uv pip install --upgrade pip
# uv pip install setuptools wheel
# uv pip install -r requirements.txt
# uv pip install git+ssh://git@github.com/EleutherAI/lm-evaluation-harness.git
cd lm-evaluation-harness
uv pip install -e .
