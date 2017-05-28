read -p "Are you sure you want to deploy to Heroku [production] [y/n]? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    git push heroku master
    heroku run --app willsnetwork python src/manage.py migrate
    heroku open --app willsnetwork
fi
