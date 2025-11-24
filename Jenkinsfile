pipeline {
    agent any
    
    stages {
        stage('clone repo') {
            steps {
                git 'https://github.com/Protestator-Research/cpp-dependencies'
            }
        }
        stage('prep runner') {
            environment {
                SERVICE_CREDS = credentials('builder')
            }
            steps {
                sh script: '''conan remote add protestator-conan https://protestatorresearch.jfrog.io/artifactory/api/conan/protestator-conan'''
                sh script: '''conan remote login -p $SERVICE_CREDS_PSW protestator-conan $SERVICE_CREDS_USR'''
            }
        }
        stage('build m4') {
            steps {
                sh script: '''conan create ./libpq/meson --name=libpq --version=17.5'''
                sh script: '''conan create ./libpq/meson --name=libpq --version=17.5 -s build_type=Debug'''
                sh script: '''conan upload "*" -r protestator-conan -c'''
            }
        }
    }
}