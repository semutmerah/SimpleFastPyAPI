pipeline {
    agent { label 'agent-1' }

    stages {
        stage('Build') {
            steps {
                pipenv install
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
