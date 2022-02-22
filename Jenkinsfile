pipeline {
    agent any

    stages {
        stage('Source') {
            steps {
                git url:'https://github.com/heathz/ocusto.git', branch:'main'
            }
        }
        
        stage('Docker Install'){
            steps {
                sh "apt-get update"
                sh "if ! dpkg-query -W -f='${Status}' docker  | grep 'ok installed'; then apt install docker -y; fi"
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