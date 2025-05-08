pipeline {
    agent any

    environment {
        OWM_API_KEY = credentials('owm-api-key')  # OpenWeatherMap-avain Jenkinsin salaisuutena
    }

    stages {
        stage('Checkout koodi') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/jessesillman/weatherapi.git'
            }
        }

        stage('Luo virtuaaliympäristö') {
            steps {
                sh 'python -m venv venv'
            }
        }

        stage('Asenna riippuvuudet') {
            steps {
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Testaa') {
            steps {
                sh 'source venv/bin/activate && python -m pytest tests/ -v'
            }
        }
    }

    post {
        failure {
            slackSend channel: '#alerts', 
                     color: 'danger', 
                     message: "Build ${env.BUILD_URL} epäonnistui!"
        }
    }
}