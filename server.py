import connexion

# create application instance
app = connexion.App(__name__)

# read swagger.yml file to configure endpoints
app.add_api('swagger.yml')


if __name__=="__main__":
    app.run(debug=True)