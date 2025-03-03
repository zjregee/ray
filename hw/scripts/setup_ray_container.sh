cd /
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip wheel
pip install -U https://s3-us-west-2.amazonaws.com/ray-wheels/latest/ray-3.0.0.dev0-cp310-cp310-manylinux2014_aarch64.whl
python /workspace/python/ray/setup-dev.py -y
cd /workspace/python
pip install -r requirements.txt
pip install tqdm
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
