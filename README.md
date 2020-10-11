

# FSD Consulting

One Paragraph of project description goes here


### Requirements
* Clone this repository: 
```
https://github.com/zank0201/fsdcon.git
```
* Install postgressql locally and access the server from the terminal:
```
psql -U postgres

```

* Create a user 'postgres' with the password 'postgres'. This will be the database that will be used to create a dynamic dashboard:
* Create a database called fsdcon from the terminal:

```
CREATE DATABASE fsdcon
```

### Installing
### API
* Enter the root file and install the python dependencies from requirements.txt:
```
pip install -r requirement.txt
```
* Run the API
```
python app.py
```

* Enter the frontend folder and install the dependencies:

```
cd frontend
npm install
```

* Connect to the frontend by running:

```
npm run dev
```

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
