pipeline {
    agent any

    tools {
        nodejs 'NODE' 
    }
 
    stages { 
        
  
        stage('Install Backend Dependencies') {
            steps {
                dir('backend') {
                    sh 'pip install -r requirements.txt'  
                }
            }
        }

        stage('Install Frontend Dependencies') {
            steps {
                dir('frontend') {
                    sh 'npm install '  
                }
            } 
        } 
 
        stage('Lint Frontend Code') {
            steps {
                dir('client') {
                    sh 'npm run lint'
                }
            } 
        } 
 
        

stage('Build Frontend') {
            steps {
                dir('client') {
                    sh 'npm run build'
                }
            }
        }
        
    }
    post {
        always {
            echo 'Pipeline execution complete!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs for details.'
        }
        success {
            echo 'Pipeline executed successfully.'
        }
    }
}