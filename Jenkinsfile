pipeline {
    agent any
    
    stages {
        stage('clone repo') {
            steps {
                git 'https://github.com/Protestator-Research/cpp-dependencies'
                sh script: '''conan profile detect'''
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