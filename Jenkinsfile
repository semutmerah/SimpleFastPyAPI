pipeline {
    agent { label 'agent-1' }

    stages {
        stage('Build') {
            steps {
                pipenv --python /usr/bin/python3 install
            }
        }
        stage('Dev Deploy') {
            steps {
                pipenv run uvicorn main:app --reload&
            }
        }
        stage('Test') {
            steps {
                pipenv run pytest tests
            }
        }
    }
}
