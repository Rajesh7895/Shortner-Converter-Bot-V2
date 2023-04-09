echo "Cloning Repo...."
git clone https://github.com/Mdisksite/Mdisk-Site-Bot-V2.git /Mdisk-Site-Bot-V2
cd /Mdisk-Site-Bot-V2
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 bot.py
