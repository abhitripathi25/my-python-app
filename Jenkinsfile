pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/<your-username>/my-python-app.git'
            }
        }

        stage('Run Script') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}

