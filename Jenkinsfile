pipeline {
    agent { label 'agent-1' }

    stages {
        stage('Build') {
            steps {
                ls -la
                echo 'Building..'
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
