pipeline {
    agent any

    stages {
        stage('Source') {
            steps {
                git url:'https://github.com/heathz/ocusto.git', branch:'main'
            }
        }
        
        stage('Build Image'){
            steps{
                script{
                    dockerapp = docker.build("timeuz/ocusto:${env.BUILD_ID}", '-f ./Dockerfile .')
                }
            }
        }

        stage('Push Image'){
            steps{
                script{
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub'){
                        dockerapp.push('latest')
                        dockerapp.push("${env.BUILD_ID}")
                    }
                }
            }
        }
    }
}