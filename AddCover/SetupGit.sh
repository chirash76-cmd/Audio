cd "storage/music"
git clone https://github.com/chirash76-cmd/Audio.git
echo 'alias musicd="cd storage/music/Audio && git pull origin main"' >> ~/.bashrc
source ~/.bashrc
