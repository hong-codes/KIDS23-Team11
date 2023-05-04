# KIDS23-Team11
# JudeGPT
<!-- ABOUT THE PROJECT -->
## About The Project

This is St. Jude KIDS23 Biohackathon project forTeam11. </br>
Goal of this project is to customize GPT models for biomedical researchers at St. Jude, evaluate different commercial and open-source models and find the one that meets high grade research standards without worrying about leaking of confidential data.

<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

* [Docker](https://www.docker.com/)
* [Django](https://www.djangoproject.com/)
* [Vue.js](https://vuejs.org/)
* HuggingFace [Transformers](https://huggingface.co/transformers/) and [Datasets](https://huggingface.co/docs/datasets/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps:

### Prerequisites

* Docker Installation - Download apporpirate Docker installtion file for your OS: https://docs.docker.com/get-docker/

### Installation and setup

1. Once docker is installed, clone the repo on you local folder:

   ```sh
   git clone https://github.com/stjude-biohackathon/KIDS23-Team11.git
   ```
2. Go to the repo root and run this docker commands to build image (will take few minute for first time, should be faster on sunsequent run): 

   ```sh
   docker-compose build
   ```
3. Start database container first using following command:

   ```sh
   docker-compose up db
   ```
   Once you see following LOG in terminal, go to next step:

   ```sh
   kids23-team11-db-1   | LOG:  database system is ready to accept connections
   ```
4. Open new terminal tab and start Django app container using following command:

   ```sh 
   docker-compose up backend
   ```
   Once you see following LOG in terminal, the app is ready!
   ```sh
   kids23-team11-backend-1  | Starting development server at http://0.0.0.0:8000/
   kids23-team11-backend-1  | Quit the server with CONTROL-C.
   ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

To test the app, go to the homepage: http://localhost:8000/
When app is launched for the first time, it will load sample database from GPCRdb Protein family query and sample CSV file from `/raw_data/` folder.
Explore REST api queires at following page: http://localhost:8000/api/

To post new data, go to database use the following API endpoint:
http://localhost:8000/api/post_question_answer/
```

The JSON object for post must following this format:
```json
{
	"text": "What is the meaning of life?",
	"type": "general",
	"answers": [
		{
			"type": "ChatGPT",
			"text": "Menaing of life is to be happy.",
			"score": "positive"
		},
		{
			"type": "BioGPT",
			"text": "Meaning of life is to achieve your goals.",
			"score": "neutral"
		},
		{
			"type": "AI21",
			"text": "Meaning of life is to not die.",
			"score": "negative"
		},
		{
			"type": "OpenAssistant",
			"text": "Meaning of life is to be always learning.",
			"score": "positive"
		}
	]
}
```

<p align="right">(<a href="#top">back to top</a>)</p>