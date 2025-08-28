pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'abhishek',
                    url: 'https://github.com/abhitripathi25/my-python-app.git'
            }
        }

        stage('Run Script') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}

