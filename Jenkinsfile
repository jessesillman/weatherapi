pipeline {
    agent any

    environment {
        OWM_API_KEY = credentials('owm-api-key')
    }

    stages {
        stage('Testaa') {
            steps {
                sh 'pip install pytest'
                sh 'python -m pytest tests/ -v'
            }
        }
        
        stage('Rakenna Docker-image') {
            steps {
                script {
                    docker.build("saa-sovellus:${env.BUILD_ID}")
                }
            }
        }
        
        stage('Pushaa Docker Hubiin') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-creds') {
                        docker.image("saa-sovellus:${env.BUILD_ID}").push("latest")
                    }
                }
            }
        }
    }
}