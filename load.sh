directorio=/home/aaron/Desarrollo/chatbots/compramexBot/botMessengerFacebook

rm -r $directorio/app/customModules/replies_bot/__pycache__

pip install app/src/pymessenger/. --upgrade
pip install $directorio/app/customModules/replies_bot/. --upgrade

#---------------------------------------------------------------------------------------------------------------------------------
