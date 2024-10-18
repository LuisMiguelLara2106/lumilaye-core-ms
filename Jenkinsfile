pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "laraman/system-metrics-app-core-ms"
        DOCKER_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push("latest")
                    }
                }
            }
        }

        stage('Deploy to Staging') {
            steps {
                sh "docker stop fastapi-backend-staging || true"
                sh "docker rm fastapi-backend-staging || true"
                sh "docker run -d --name fastapi-backend-staging -p 8000:8000 ${DOCKER_IMAGE}:${DOCKER_TAG}"
            }
        }

        stage('Run Tests') {
            steps {
                sh "docker exec fastapi-backend-staging pytest /app/tests"
            }
        }

        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                input message: '¿Desplegar a producción?'
                sh "docker stop fastapi-backend-prod || true"
                sh "docker rm fastapi-backend-prod || true"
                sh "docker run -d --name fastapi-backend-prod -p 80:8000 ${DOCKER_IMAGE}:${DOCKER_TAG}"
            }
        }
    }

    post {
        always {
            sh 'docker image prune -f'
        }
        success {
            echo 'Pipeline ejecutado con éxito!'
        }
        failure {
            echo 'El pipeline ha fallado.'
        }
    }
}