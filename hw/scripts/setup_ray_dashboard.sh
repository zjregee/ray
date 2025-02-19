curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
nvm install 14
nvm use 14
cd /workspace/python/ray/dashboard/client
npm config set registry https://registry.npmmirror.com
npm ci
npm run build
